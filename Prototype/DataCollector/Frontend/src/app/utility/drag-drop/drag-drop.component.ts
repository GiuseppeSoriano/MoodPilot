import { CommonModule } from '@angular/common';
import { Component, EventEmitter, HostListener, Output, ElementRef, ViewChild, OnInit, OnDestroy, ChangeDetectorRef } from '@angular/core';

@Component({
  selector: 'app-drag-drop',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './drag-drop.component.html',
  styleUrls: ['./drag-drop.component.css']
})
export class DragDropComponent implements OnInit, OnDestroy {
  @Output() fileUploaded = new EventEmitter<File | Blob>();
  @ViewChild('fileInput', { static: false }) fileInput!: ElementRef;
  @ViewChild('videoPlayer', { static: false }) videoPlayer!: ElementRef<HTMLVideoElement>;
  @ViewChild('liveVideo', { static: false }) liveVideo!: ElementRef<HTMLVideoElement>;

  isDragOver = false;
  isError = false;
  errorMessage = '';
  droppedFile: File | null = null;

  videoUrl: string | null = null; // URL del video caricato o registrato
  isRecording = false; // Stato della registrazione
  mediaRecorder: MediaRecorder | null = null; // MediaRecorder per la registrazione
  recordedChunks: Blob[] = []; // Dati del video registrato
  mediaStream: MediaStream | null = null; // Stream della webcam

  constructor(private cdr: ChangeDetectorRef) {}

  ngOnInit(): void {}

  ngOnDestroy(): void {
    this.stopLiveStream(); // Interrompe lo stream alla distruzione del componente
  }

  triggerFileInput(): void {
    this.fileInput.nativeElement.click();
  }

  onFileSelected(event: Event): void {
    if (this.isRecording) {
      this.stopLiveStream(); // Ferma lo streaming se è in corso
    }

    const input = event.target as HTMLInputElement;
    if (input.files && input.files.length === 1) {
      this.droppedFile = input.files[0];
      this.videoUrl = URL.createObjectURL(this.droppedFile);
      this.fileUploaded.emit(this.droppedFile);
    } else {
      this.displayError('Please select only one file.');
    }
  }

  removeFile(): void {
    if (this.isRecording) {
      this.stopLiveStream(); // Ferma lo streaming se è in corso
    }

    this.droppedFile = null;
    this.videoUrl = null;
    this.clearError();
  }

  async startRecording(): Promise<void> {
    try {
      this.mediaStream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });

      this.isRecording = true;
      this.recordedChunks = [];

      this.cdr.detectChanges();

      console.log("Proviamo ad entrare nel ramo di startRecording");
      console.log("this.liveVideo: ", this.liveVideo);
      console.log("this.mediaStream: ", this.mediaStream);

      if (this.liveVideo && this.mediaStream) {
        console.log("Provo a fare partire lo stream");
        const videoElement = this.liveVideo.nativeElement;
        videoElement.srcObject = this.mediaStream;
        videoElement.muted = true; // Disattiva l'audio per evitare eco
        videoElement.play(); // Avvia il feed live
      }

      this.mediaRecorder = new MediaRecorder(this.mediaStream);

      this.mediaRecorder.ondataavailable = (event) => {
        if (event.data.size > 0) {
          this.recordedChunks.push(event.data);
        }
      };

      this.mediaRecorder.onstop = () => {
        const videoBlob = new Blob(this.recordedChunks, { type: 'video/webm' });

        const videoFile = new File([videoBlob], 'recorded_video.webm', { type: 'video/webm' });

        this.videoUrl = URL.createObjectURL(videoBlob);
        this.fileUploaded.emit(videoFile);

        this.stopLiveStream(); // Ferma lo stream live
        this.isRecording = false;
      };

      this.mediaRecorder.start();
    } catch (error) {
      this.displayError('Unable to access camera. Please check your permissions.');
    }
  }

  stopRecording(): void {
    if (this.mediaRecorder && this.isRecording) {
      this.mediaRecorder.stop();
    }
    this.stopLiveStream();
  }

  stopLiveStream(): void {
    if (this.mediaStream) {
      this.mediaStream.getTracks().forEach((track) => track.stop());
      this.mediaStream = null;
    }
  }

  displayError(message: string): void {
    this.isError = true;
    this.errorMessage = message;
  }

  clearError(): void {
    this.isError = false;
    this.errorMessage = '';
  }

  @HostListener('dragover', ['$event'])
  @HostListener('dragenter', ['$event'])
  onDragEnter(event: DragEvent): void {
    event.preventDefault();
    event.stopPropagation();
    this.isDragOver = true;
  }

  @HostListener('dragleave', ['$event'])
  @HostListener('dragend', ['$event'])
  onDragLeave(event: DragEvent): void {
    event.preventDefault();
    event.stopPropagation();
    this.isDragOver = false;
  }

  @HostListener('drop', ['$event'])
  onDrop(event: DragEvent): void {
    event.preventDefault();
    event.stopPropagation();
    this.isDragOver = false;

    if (this.isRecording) {
      this.stopLiveStream(); // Ferma lo streaming se è in corso
    }

    const files = event.dataTransfer?.files;
    if (files && files.length === 1) {
      this.droppedFile = files[0];
      this.videoUrl = URL.createObjectURL(this.droppedFile);
      this.fileUploaded.emit(this.droppedFile);
    } else {
      this.displayError('Please drop only one file.');
    }
  }
}
