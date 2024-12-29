import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ReportService {
  private serverUrl = 'http://localhost:8080/api/fer'; // Sostituisci con l'URL del backend

  constructor(private http: HttpClient) {}

  sendReport(reportData: FormData): Observable<any> {
    return this.http.post<any>(this.serverUrl + "/report", reportData);
  }
}
