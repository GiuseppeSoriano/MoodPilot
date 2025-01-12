import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule } from '@angular/forms';
import { MatExpansionModule } from '@angular/material/expansion';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatIcon } from '@angular/material/icon';
import { MatRadioModule } from '@angular/material/radio';
import { MatButtonModule } from '@angular/material/button';
import { DragDropComponent } from "../utility/drag-drop/drag-drop.component";
import { ReportService } from '../services/report/report.service';
import { LoadingComponent } from "../utility/loading/loading.component";

@Component({
  selector: 'app-form-page',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule, MatExpansionModule, MatFormFieldModule, MatInputModule, MatIcon, MatRadioModule, MatButtonModule, DragDropComponent, LoadingComponent],
  templateUrl: './form-page.component.html',
  styleUrl: './form-page.component.css'
})
export class FormPageComponent {
  rideFeedbackForm: FormGroup;
  ratings = [1, 2, 3, 4, 5];
  stars = [1, 2, 3, 4, 5];

  loading = false; // Per mostrare il loading spinner

  videoFile: File | Blob | null = null; // Per salvare il video caricato

  constructor(private fb: FormBuilder, private reportService: ReportService) {
    this.rideFeedbackForm = this.fb.group({
      comfort: [0],
      safety: [0],
      experience: [0],
      specificMoments: [0]
    });
  }

  setRating(controlName: string, rating: number): void {
    this.rideFeedbackForm.get(controlName)?.setValue(rating);
  }


  ngOnInit(): void {
    
  }

  handleVideoUpload(file: File | Blob): void {
    console.log('Video file uploaded:', file);
    this.videoFile = file; // Salva il video caricato
  }

  onSubmit(): void {
    this.rideFeedbackForm.value.specificMoments = Number(this.rideFeedbackForm.value.specificMoments);
    console.log(this.rideFeedbackForm.value);


    if (!this.videoFile) {
      alert('Carica un video prima di inviare il report.');
      return;
    }

    const formData = new FormData();

    // Aggiungi i dati del form
    Object.entries(this.rideFeedbackForm.value).forEach(([key, value]) => {
      if (value !== null && value !== undefined) {
        formData.append(key, value.toString());
      }
    });

    // Aggiungi il video al FormData
    formData.append('video', this.videoFile);

      // Debug
    formData.forEach((value, key) => {
      console.log(`${key}:`, value);
    });

    console.log('Invio del report:', formData);

    this.loading = true; // Mostra il loading spinner

    // Invia la richiesta tramite il service
    this.reportService.sendReport(formData).subscribe({
      next: (response) => {
        this.loading = false; // Nasconde il loading spinner
        console.log('Report inviato con successo:', response);
        alert('Report inviato con successo!');
      },
      error: (error) => {
        this.loading = false; // Nasconde il loading spinner
        console.error('Errore nell\'invio del report:', error);
        alert('Errore durante l\'invio del report.');
      },
    });
  }
}
