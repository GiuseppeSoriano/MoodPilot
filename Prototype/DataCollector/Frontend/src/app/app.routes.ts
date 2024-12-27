import { Routes } from '@angular/router';
import { FormPageComponent } from './form-page/form-page.component';

export const routes: Routes = [
    {path: 'home', component: FormPageComponent },
    {path: '', redirectTo: 'home', pathMatch: 'full'}
];
