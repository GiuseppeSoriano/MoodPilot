import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { MatExpansionModule } from '@angular/material/expansion';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatIcon } from '@angular/material/icon';
import { MatRadioModule } from '@angular/material/radio';
import { MatButtonModule } from '@angular/material/button';
import { DragDropComponent } from "../utility/drag-drop/drag-drop.component";

@Component({
  selector: 'app-form-page',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule, MatExpansionModule, MatFormFieldModule, MatInputModule, MatIcon, MatRadioModule, MatButtonModule, DragDropComponent],
  templateUrl: './form-page.component.html',
  styleUrl: './form-page.component.css'
})
export class FormPageComponent {
  rideFeedbackForm: FormGroup;
  ratings = [1, 2, 3, 4, 5];
  stars = [1, 2, 3, 4, 5];

  constructor(private fb: FormBuilder) {
    this.rideFeedbackForm = this.fb.group({
      comfort: [0],
      safety: [null],
      experience: [null],
      specificMoments: [null]
    });
  }

  setRating(controlName: string, rating: number): void {
    this.rideFeedbackForm.get(controlName)?.setValue(rating);
  }


  ngOnInit(): void {
    
  }

  onSubmit() {
    // this.formService.submitForm(this.rideFeedbackForm.value).subscribe(
    //   (response: any) => {
    //     if (response) {
    //       this.router.navigate(['/table']);
    //     } else {
    //       alert('Errore durante l\'invio del form');
    //     }
    //   },
    //   (error: any) => {
    //     console.error(error);
    //     alert('Errore durante l\'invio del form');
    //   }
    // );
    
  }

  onFileChange(event: any) {
    const files: FileList = event.target.files;
    if (!files) return;
  
    const fileArray = Array.from(files);
    const currentMedias = this.rideFeedbackForm?.get('media')?.value || [];
  
    if (fileArray.length + currentMedias.length > 5) {
      alert('Puoi caricare fino a 5 foto.');
      return;
    }
  
    let updatedMedias = [...currentMedias];
    let readersCompleted = 0;
  
    fileArray.forEach(file => {
      const reader = new FileReader();
      reader.onload = () => {
        const base64 = reader.result as string;
        updatedMedias.push(base64);
        readersCompleted++;
  
        // Aggiorna il form solo quando tutti i FileReader sono completati
        if (readersCompleted === fileArray.length) {
          this.rideFeedbackForm?.patchValue({ foto: updatedMedias });
        }
      };
      reader.readAsDataURL(file as Blob);
    });
  }
  

  removeMedia(index: number) {
    const currentMedias = this.rideFeedbackForm?.get('foto')?.value || [];
    const updatedMedias = currentMedias.filter((_:any, i:any) => i !== index);
    this.rideFeedbackForm?.patchValue({ foto: updatedMedias });
  }
}
