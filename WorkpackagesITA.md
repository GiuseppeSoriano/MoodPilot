### **WP1: Configurazione e Progettazione del Database (DB)**

#### **Classificazione**  
- **RI (Research and Innovation)**

#### **Motivazione**  
Un database ben progettato è fondamentale per archiviare e gestire in modo efficiente i dati raccolti dal sistema, tra cui valutazioni FER, feedback manuali e dati sensoriali provenienti dai veicoli. La struttura deve garantire velocità nelle query, integrità dei dati e scalabilità per gestire un numero crescente di veicoli e utenti.

#### **Activity Start / Activity End**  
- **Inizio**: Mese 1  
- **Fine**: Mese 2  

#### **Mesi uomo**  
- 1 project manager per 2 mesi (2 mesi/uomo).
- 1 sviluppatore senior (db) per 2 mesi (2 mesi/uomo).  

#### **Obiettivi**  
1. Progettare uno schema di database robusto, normalizzato e ottimizzato per le query principali.  
2. Implementare il database su un server locale o cloud.  
3. Garantire la scalabilità e l’integrità dei dati.  
4. Ottimizzare le query per il backend e il sistema di reportistica.  

#### **Task**  
1. **Analisi dei requisiti**:
   - Raccolta dei dati necessari per il sistema (FER, valutazioni, feedback, dati sensoriali).  
   - Identificazione delle relazioni tra le entità principali.  
2. **Progettazione dello schema**:
   - Definizione delle tabelle principali (es. `Passengers`, `Drivers`, `Trips`, `FER_Data`, `Evaluations`).  
   - Normalizzazione dello schema per eliminare ridondanze e garantire coerenza.  
3. **Implementazione del database**:
   - Creazione delle tabelle e definizione delle relazioni (es. 1:N, N:N).  
   - Configurazione di indici per ottimizzare le query principali.  
4. **Ottimizzazione delle query**:
   - Sviluppo delle query per operazioni comuni (es. inserimento valutazioni, calcolo della media delle ultime 500 valutazioni).  
   - Ottimizzazione delle prestazioni su dataset simulati.  
5. **Testing e validazione**:
   - Verifica dell’integrità referenziale e funzionalità delle query.  
   - Simulazione di carichi crescenti per valutare la scalabilità.  

#### **Deliverables**  
1. **Schema del database**: Modello ER diagram documentato.  
2. **Database implementato**: Database funzionante con tutte le tabelle e relazioni definite.  
3. **Script SQL**: Script per la creazione delle tabelle, vincoli e indici.  
4. **Report**: Documentazione delle query principali e delle ottimizzazioni applicate.  

#### **Punti di controllo (Milestone)**  
1. Consegna dello schema ER diagram (fine Mese 1).  
2. Implementazione del database e script SQL funzionanti (metà Mese 2).  
3. Validazione delle query e report finale (fine Mese 2).  

#### **Dipendenze tra WP**  
- **WP2 (Backend)**: Necessario per testare la comunicazione tra il database e gli endpoint API. Bisogna completarne la progettazione prima di procedere con il backend.
- **WP5 (Integrazione)**: Il database deve essere completo e funzionante prima di procedere all’integrazione dei componenti.


#### **Tool o Software Necessari**  
- **Database Relazionale**: MySQL o PostgreSQL (già disponibili).  
- **Strumenti di Modellazione**: DbSchema o MySQL Workbench (già disponibili).  
- **Linguaggio SQL**: Per implementare e ottimizzare il database (nessun costo aggiuntivo).  
- **Strumenti di Profilazione**: EXPLAIN per analizzare query (disponibile nel DBMS scelto).  

#### **Ruoli richiesti**  

- **Database Developer**: Esperto in progettazione e ottimizzazione di database relazionali (MySQL o PostgreSQL).  

#### **Costo per ognuno (calcolato in funzione del mese/uomo)**  
- **Database Developer**: €5.000/mese  
- **Project Manager**: €6.000/mese

#### **Costo totale WP1**  
- **€22.000**

---

### **WP2: Sviluppo del Backend**

#### **Classificazione**
- **RI (Research and Innovation)**

#### **Motivazione**
Il backend è il cuore del sistema, responsabile della gestione del flusso di dati tra i vari componenti: database, car controller, e frontend. Deve integrare il modello FER, esporre endpoint API RESTful e garantire una gestione efficiente delle valutazioni e dei dati raccolti, con particolare attenzione alla sicurezza e alla scalabilità.

#### **Activity Start / Activity End**
- **Inizio**: Mese 2  
- **Fine**: Mese 4  

#### **Mesi uomo**
- 1 project manager per 3 mesi (3 mesi/uomo).
- 2 sviluppatori backend per 3 mesi (6 mesi/uomo).

#### **Obiettivi**
1. Implementare un backend robusto e scalabile in Python per gestire il flusso di dati.  
2. Integrare il modello FER per la gestione delle valutazioni automatiche.  
3. Esporre endpoint API RESTful per comunicare con il frontend e il car controller.  
4. Garantire sicurezza e conformità alle normative sulla privacy (es. GDPR).  

#### **Task**
1. **Setup dell’ambiente di sviluppo**:
   - Configurazione del framework backend (es. Flask o FastAPI).
   - Strutturazione del progetto.  
2. **Implementazione delle API RESTful**:
   - Creazione degli endpoint per la comunicazione con car controller, frontend e database (es. `/sendEvaluation`, `/getUserData`).  
   - Validazione e autenticazione delle richieste API.  
3. **Integrazione del database**:
   - Connessione al database utilizzando un ORM (es. SQLAlchemy).  
   - Sviluppo di query backend per gestire dati complessi (es. calcolo della media delle ultime 500 valutazioni).  
4. **Integrazione del modello FER**:
   - Implementazione delle funzioni per ricevere input dal car controller.  
   - Elaborazione e memorizzazione dei dati FER nel database.  
5. **Sicurezza e privacy**:
   - Implementazione di protocolli di sicurezza (es. TLS 1.3 per le comunicazioni).  
   - Crittografia dei dati sensibili.  
   - Creazione di policy di gestione dei dati conformi al GDPR.  
6. **Testing e validazione**:
   - Test delle API (unit test e integration test).  
   - Simulazione di carichi per garantire scalabilità.  

#### **Deliverables**
1. **Backend funzionante**: Codice sorgente completo con API e integrazione del modello FER.  
2. **Documentazione tecnica**: Dettagli sull’implementazione, endpoint API e istruzioni per l’uso.  
3. **Logica di gestione dati**: Funzioni implementate per interagire con il database e il car controller.  
4. **Test report**: Risultati dei test di integrazione e delle simulazioni di carico.  

#### **Punti di controllo (Milestone)**
1. Consegna delle API di base funzionanti (fine Mese 2).  
2. Integrazione del database completata (fine Mese 3).    
3. Validazione del backend in ambiente simulato (fine Mese 4).  

#### **Dipendenze tra WP**
- **WP1 (Database)**: La progettazione del database deve essere completata per sviluppare il backend.
- **WP5 (Integrazione)**: Il backend deve essere completato per consentire l’integrazione dei componenti.  

#### **Tool o Software Necessari**
- **Framework Backend**: Flask o FastAPI (disponibili).  
- **Librerie di sicurezza**: PyJWT per autenticazione, OpenSSL per crittografia.  
- **ORM**: SQLAlchemy o equivalente per interazione con il database.  
- **Strumenti di testing**: Postman per API testing, pytest per test automatici.  

#### **Ruoli richiesti**
- **Backend Developer**: Specialista in Python con esperienza nello sviluppo di API RESTful e integrazione di modelli AI.  
- **Data Engineer**: Per ottimizzare il flusso di dati tra backend e database.  

#### **Costo per ognuno (calcolato in funzione del mese/uomo)**
- **Backend Developer**: €5.000/mese  
- **Project Manager**: €6.000/mese

#### **Costo totale WP2**
- **€48.000**

---

### **WP3: Sviluppo del Car Controller**

#### **Classificazione**
- **RI (Research and Innovation)**

#### **Motivazione**
Il car controller è responsabile dell’esecuzione del modello FER a bordo del veicolo. Deve raccogliere dati sensoriali, elaborare le espressioni facciali in tempo reale, e comunicare i risultati al backend. La sua progettazione deve garantire efficienza, affidabilità e bassi consumi, essendo una componente essenziale per l’intero sistema.

#### **Activity Start / Activity End**
- **Inizio**: Mese 3  
- **Fine**: Mese 5  

#### **Mesi uomo**
- 1 project manager per 3 mesi (3 mesi/uomo).
- 2 sviluppatori embedded per 3 mesi (6 mesi/uomo).

#### **Obiettivi**
1. Implementare il software del car controller per eseguire il modello FER in tempo reale.  
2. Stabilire la comunicazione sicura tra il controller e il backend.  
3. Raccogliere dati sensoriali (es. velocità, frenate) e inviarli al backend.  
4. Ottimizzare le prestazioni per l’hardware specifico del veicolo.  

#### **Task**
1. **Setup dell’hardware**:
   - Configurazione dell’ambiente hardware (es. edge device, GPU, o TPU).  
   - Installazione di librerie necessarie per eseguire il modello FER.  
2. **Deployment del modello FER**:
   - Adattamento del modello FER per l’esecuzione su hardware embedded.  
   - Testing delle prestazioni del modello in scenari simulati.  
3. **Raccolta dati sensoriali**:
   - Sviluppo di driver o script per leggere dati dal veicolo (es. CAN bus).  
   - Validazione dei dati raccolti e loro conversione in formati utilizzabili.  
4. **Comunicazione con il backend**:
   - Configurazione della comunicazione sicura tramite API RESTful o WebSocket.  
   - Implementazione di un protocollo per trasmettere i risultati FER e i dati sensoriali al backend.  
5. **Ottimizzazione e testing**:
   - Ottimizzazione delle prestazioni per garantire latenza ridotta (<500 ms).  
   - Test in ambienti reali e simulazioni di carico.  

#### **Deliverables**
1. **Software del car controller**: Codice completo per eseguire il modello FER, raccogliere dati e comunicare con il backend.  
2. **Report tecnico**: Dettagli sull’implementazione, configurazione hardware e ottimizzazioni applicate.  
3. **Log di test**: Risultati dei test effettuati in simulazioni e scenari reali.  

#### **Punti di controllo (Milestone)**
1. Configurazione hardware completata (fine Mese 3).  
2. Deployment del modello FER completato (metà Mese 4).  
3. Comunicazione con il backend funzionante (fine Mese 4).  
4. Validazione in ambiente reale (fine Mese 5).  

#### **Dipendenze tra WP**
- **WP2 (Backend)**: Devono essere completate le API per consentire la comunicazione con il car controller.
- **WP5 (Integrazione)**: Il car controller deve essere sviluppato e funzionante per consentire l’integrazione con il resto del sistema.  

#### **Tool o Software Necessari**
- **Framework per AI**: TensorFlow Lite o PyTorch per eseguire il modello FER (già disponibili).  
- **Librerie di comunicazione**: Requests o aiohttp per RESTful API.  
- **Hardware per il car controller**: Edge device con supporto GPU (es. NVIDIA Jetson Nano, Coral TPU).  
- **Strumenti di simulazione**: Simulatori CAN per testare la raccolta dati sensoriali.  

#### **Ruoli richiesti**
- **Embedded Developer**: Specialista in dispositivi edge con esperienza in AI e ottimizzazione hardware.  

#### **Costo per ognuno (calcolato in funzione del mese/uomo)**
- **Project Manager**: €6.000/mese
- **Embedded Developer**: €5.500/mese

#### **Costo totale WP3**
- **€51.000**

---

### **WP4: Sviluppo del Frontend (Mobile App)**

#### **Classificazione**
- **RI (Research and Innovation)**

#### **Motivazione**
La mobile app è il punto di contatto principale tra gli utenti (passeggeri e conducenti) e il sistema. Deve fornire un'interfaccia intuitiva e user-friendly per visualizzare valutazioni, completare questionari, gestire dati personali e interagire con il backend. Una progettazione efficace è essenziale per garantire un’ottima esperienza utente.

#### **Activity Start / Activity End**
- **Inizio**: Mese 6  
- **Fine**: Mese 7  

#### **Mesi uomo**
- 1 project manager per 2 mesi (2 mesi/uomo).
- 2 sviluppatori frontend per 2 mesi (4 mesi/uomo).  

#### **Obiettivi**
1. Creare un’interfaccia utente intuitiva per passeggeri e conducenti.  
2. Implementare le funzionalità per la visualizzazione e modifica delle valutazioni e questionari.  
3. Garantire un’esperienza utente fluida e compatibilità con dispositivi Android e iOS.  

#### **Task**
1. **Progettazione UI/UX**:
   - Creazione di wireframe e mockup per le principali sezioni dell’app (es. schermate di valutazione, profilo utente).  
   - Validazione del design con un campione di utenti.  
2. **Implementazione funzionalità principali**:
   - Integrazione con il backend tramite API RESTful.  
   - Schermata per la visualizzazione e modifica dei questionari generati dal FER.  
   - Sezione per fornire valutazioni manuali (passeggeri) e valutazioni dei passeggeri (conducenti).  
3. **Gestione dati personali**:
   - Creazione di una schermata per la gestione del profilo utente, con possibilità di aggiornare e visualizzare i propri dati.  
   - Implementazione delle policy GDPR (es. richiesta di cancellazione dati).  
4. **Testing dell’app**:
   - Test su dispositivi Android e iOS per garantire compatibilità e prestazioni.  
   - Identificazione e risoluzione di bug.  
5. **Ottimizzazione finale**:
   - Miglioramento delle prestazioni (es. tempi di caricamento).  
   - Applicazione di feedback raccolti dai test con gli utenti.  

#### **Deliverables**
1. **Mobile app funzionante**: Applicazione completa per dispositivi Android e iOS.  
2. **Documentazione tecnica**: Dettagli sull’implementazione, API utilizzate e istruzioni per la distribuzione.  
3. **Report di test**: Risultati dei test effettuati su dispositivi reali.  

#### **Punti di controllo (Milestone)**
1. Consegna dei wireframe e mockup finali (fine Mese 4).  
2. Implementazione delle funzionalità principali (fine Mese 5).  
3. Testing completo e consegna della versione finale dell’app (fine Mese 6).  

#### **Dipendenze tra WP**
- **WP2 (Backend)**: Necessario per implementare e testare la comunicazione con il backend.  
- **WP5 (Integrazione)**: Il frontend deve essere completato e testato per procedere all'integrazione completa del sistema.  

#### **Tool o Software Necessari**
- **Framework di sviluppo**: Flutter o React Native (già disponibili).  
- **Strumenti di progettazione**: Figma o Adobe XD per UI/UX design.  
- **Librerie di comunicazione**: Axios o HTTP per integrazione API.  
- **Strumenti di testing**: BrowserStack o dispositivi reali per test cross-platform.  

#### **Ruoli richiesti**
- **Frontend Developer**: Specialista in sviluppo mobile, esperto in Flutter/React Native.  

#### **Costo per ognuno (calcolato in funzione del mese/uomo)**
- **Project Manager**: €6.000/mese
- **Frontend Developer**: €4.000/mese   

#### **Costo totale WP4**
- **€20.000**

---

### **WP5: Integrazione del Sistema**

#### **Classificazione**
- **SS (Support and Services)**

#### **Motivazione**
L’integrazione del sistema è essenziale per garantire che tutte le componenti (DB, backend, car controller, e mobile app) comunichino correttamente tra loro. Il focus di questo WP è assicurare che il sistema funzioni come un’unità coesa e che i dati fluiscano senza interruzioni tra le varie parti.

#### **Activity Start / Activity End**
- **Inizio**: Mese 8  
- **Fine**: Mese 9  

#### **Mesi uomo**
- 1 project manager per 2 mesi (2 mesi/uomo).
- 1 system integrator per 2 mesi (2 mesi/uomo).  

#### **Obiettivi**
1. Assicurare la comunicazione fluida tra le componenti del sistema.  
2. Validare il flusso di dati in scenari reali e simulati.  
3. Identificare e risolvere eventuali problemi di interoperabilità.  

#### **Task**
1. **Preparazione per l’integrazione**:
   - Revisione delle interfacce e delle API esposte da backend e mobile app.  
   - Configurazione di un ambiente di test per l’integrazione.  
2. **Integrazione backend-database**:
   - Verifica della corretta gestione delle query e archiviazione dati.  
   - Test delle operazioni principali (es. lettura/scrittura dati valutazioni).  
3. **Integrazione backend-car controller**:
   - Validazione della trasmissione sicura dei dati FER e sensoriali dal car controller al backend.  
   - Test della latenza nella comunicazione.  
4. **Integrazione backend-frontend**:
   - Verifica del funzionamento delle API RESTful per il frontend.  
   - Test di funzionalità principali (es. recupero questionari, invio valutazioni).   
5. **Risoluzione problemi e ottimizzazione**:
   - Risoluzione di bug rilevati durante i test.  
   - Ottimizzazione del flusso di dati per ridurre latenza e migliorare le prestazioni.  

#### **Deliverables**
1. **Sistema integrato**: Tutte le componenti funzionanti in modo coeso.  
2. **Report tecnico**: Dettaglio dell’integrazione, test effettuati e problemi risolti.  
3. **Log di test end-to-end**: Risultati delle simulazioni e test reali.  

#### **Punti di controllo (Milestone)**
1. Integrazione backend-database completata (fine Settimana 2, Mese 6).  
2. Integrazione backend-car controller completata (fine Mese 6).  
3. Integrazione backend-frontend completata (metà Mese 7).  
4. Testing end-to-end completato (fine Mese 7).  

#### **Dipendenze tra WP**
- **WP1 (Database)**: Il database deve essere completo e funzionante per l’integrazione con il backend.  
- **WP2 (Backend)**: Il backend deve essere operativo per integrarsi con tutte le altre componenti.  
- **WP3 (Car Controller)**: Il car controller deve essere pronto per trasmettere i dati al backend.  
- **WP4 (Frontend)**: La mobile app deve essere sviluppata per testare la comunicazione con il backend.  

#### **Tool o Software Necessari**
- **Strumenti di monitoraggio**: Postman per test API, Grafana per monitorare il flusso di dati.  
- **Ambiente di integrazione**: Server locale o cloud con configurazione dedicata.  
- **Simulatori e test reali**: Simulatori CAN per dati del car controller e dispositivi mobili reali per test del frontend.  

#### **Ruoli richiesti**
- **System Integrator**: Esperto in integrazione di sistemi complessi, con competenze in backend, API e infrastrutture.  

#### **Costo per ognuno (calcolato in funzione del mese/uomo)**
- **System Integrator**: €6.000/mese  
- **Project Manager**: €6.000/mese

#### **Costo totale WP5**
- **€24.000**

---

### **WP6: Sicurezza e Privacy**

#### **Classificazione**
- **SS (Support and Services)**

#### **Motivazione**
La protezione dei dati sensibili raccolti dal sistema è fondamentale per rispettare la normativa GDPR e garantire la sicurezza delle informazioni personali degli utenti. Questo WP si concentra sull’implementazione di protocolli di sicurezza avanzati, crittografia dei dati e policy di gestione conformi alle normative.

#### **Activity Start / Activity End**
- **Inizio**: Mese 10  
- **Fine**: Mese 11  

#### **Mesi uomo**
- 1 project manager per 2 mesi (2 mesi/uomo).
- 1 esperto di sicurezza per 2 mesi (2 mesi/uomo).

#### **Obiettivi**
1. Garantire la sicurezza delle comunicazioni tra le componenti del sistema.  
2. Proteggere i dati sensibili mediante crittografia e accesso controllato.  
3. Assicurare la conformità con il GDPR e altre normative applicabili.  

#### **Task**
1. **Crittografia dei dati**:
   - Implementazione di crittografia AES-256 per i dati archiviati nel database.  
   - Configurazione di TLS 1.3 per le comunicazioni tra car controller, backend e frontend.  
2. **Gestione delle credenziali e autenticazione**:
   - Sviluppo di un sistema di autenticazione basato su token (es. JWT) per le API RESTful.  
   - Creazione di meccanismi per la gestione sicura delle credenziali (es. Hashing con bcrypt).  
3. **Policy di privacy e conformità GDPR**:
   - Creazione di strumenti per consentire agli utenti di visualizzare, modificare e cancellare i propri dati.  
   - Implementazione di logiche di anonimizzazione per i dati storici.  
4. **Monitoraggio e audit**:
   - Configurazione di strumenti di monitoraggio per rilevare attività sospette.  
   - Audit del sistema per verificare la conformità alle policy di sicurezza e privacy.  
5. **Testing e validazione**:
   - Test di vulnerabilità sulle API e sui dati archiviati.  
   - Simulazione di attacchi comuni (es. SQL injection, man-in-the-middle) per garantire la robustezza del sistema.  

#### **Deliverables**
1. **Policy di sicurezza e privacy**: Documento dettagliato delle misure adottate e delle procedure per gestire i dati sensibili.  
2. **Sistema sicuro**: Tutte le comunicazioni e i dati protetti da crittografia e accesso controllato.  
3. **Report di audit**: Valutazione della conformità GDPR e della sicurezza del sistema.  
4. **Log di test**: Risultati dei test di vulnerabilità e sicurezza.  

#### **Punti di controllo (Milestone)**
1. Crittografia dei dati archiviati e delle comunicazioni completata (fine Mese 7).  
2. Sistema di autenticazione e gestione credenziali implementato (metà Mese 8).  
3. Audit del sistema e testing di sicurezza completati (fine Mese 8).  

#### **Dipendenze tra WP**
- **WP1 (Database)**: Il database deve essere completo per implementare la crittografia dei dati archiviati.  
- **WP2 (Backend)**: Necessario per implementare meccanismi di autenticazione e sicurezza nelle API.  
- **WP5 (Integrazione)**: Deve essere completato per verificare la sicurezza e la privacy del sistema integrato.  

#### **Tool o Software Necessari**
- **Strumenti di crittografia**: OpenSSL per TLS, PyCryptodome per AES.  
- **Framework di autenticazione**: PyJWT per gestione dei token.  
- **Strumenti di audit**: OWASP ZAP o Burp Suite per test di sicurezza.  
- **Monitoraggio**: Grafana o equivalente per rilevare attività sospette.  

#### **Ruoli richiesti**
- **Security Engineer**: Esperto in sicurezza informatica e conformità GDPR.  

#### **Costo per ognuno (calcolato in funzione del mese/uomo)**
- **Security Engineer**: €5.500/mese  
- **Project Manager**: €6.000/mese

#### **Costo totale WP6**
- **€23.000**

---

### **WP7: Testing e Validazione**

#### **Classificazione**
- **SS (Support and Services)**

#### **Motivazione**
Il testing e la validazione sono fondamentali per verificare che il sistema soddisfi i requisiti funzionali e non funzionali definiti. Questo WP si concentra sull’esecuzione di test unitari, di integrazione e end-to-end, garantendo che il sistema funzioni correttamente in scenari reali e che sia robusto, affidabile e sicuro.

#### **Activity Start / Activity End**
- **Inizio**: Mese 12  
- **Fine**: Mese 15  

#### **Mesi uomo**
- 1 project manager per 4 mesi (4 mesi/uomo).
- 2 ingegneri QA per 4 mesi (8 mesi/uomo).

#### **Obiettivi**
1. Validare che tutte le componenti rispettino i requisiti funzionali e non funzionali.  
2. Identificare e risolvere bug o problematiche nelle varie parti del sistema.  
3. Assicurare che il sistema integri correttamente tutte le componenti.  
4. Verificare la robustezza del sistema in condizioni di carico e stress.  

#### **Task**
1. **Testing unitario**:
   - Creazione e esecuzione di test unitari per ciascuna componente (DB, backend, frontend, car controller).  
   - Verifica della copertura del codice (almeno 80%).  
2. **Testing di integrazione**:
   - Test delle interazioni tra il backend e il database.  
   - Verifica della comunicazione tra car controller e backend.  
   - Validazione dell’interazione tra frontend e backend tramite API.  
3. **Testing end-to-end**:
   - Simulazione di scenari completi, come un viaggio con raccolta dati FER, elaborazione e feedback.  
   - Verifica del flusso completo dei dati e della loro integrità.  
4. **Testing delle prestazioni**:
   - Simulazione di carichi elevati per testare la scalabilità del sistema.  
   - Misurazione dei tempi di risposta delle API (<200 ms sotto carico normale).  
5. **Testing di sicurezza**:
   - Verifica dell’efficacia delle misure di sicurezza implementate (es. crittografia, autenticazione).  
   - Simulazione di attacchi comuni (SQL injection, brute force, man-in-the-middle).  
6. **Risoluzione dei problemi**:
   - Analisi dei risultati dei test per identificare bug o colli di bottiglia.  
   - Risoluzione dei problemi e ripetizione dei test per confermare le correzioni.  

#### **Deliverables**
1. **Report di testing**: Documentazione dettagliata dei test effettuati, risultati e problemi risolti.  
2. **Sistema validato**: Conferma che il sistema soddisfa i requisiti funzionali e non funzionali.  
3. **Log di test**: Registrazioni dettagliate di tutti i test eseguiti, inclusi i risultati di test di carico e vulnerabilità.  

#### **Punti di controllo (Milestone)**
1. Testing unitario completato per tutte le componenti (fine Mese 8).  
2. Testing di integrazione completato (metà Mese 9).  
3. Testing end-to-end e di sicurezza completati (fine Mese 9).  

#### **Dipendenze tra WP**
- **WP1 (Database)**: Necessario per eseguire i test di integrazione con il backend.  
- **WP2 (Backend)**: Deve essere pronto per verificare le API e le logiche di gestione dati.  
- **WP3 (Car Controller)**: Deve essere operativo per validare la trasmissione dei dati FER.  
- **WP4 (Frontend)**: La mobile app deve essere completata per i test end-to-end.  
- **WP5 (Integrazione)**: L’intero sistema deve essere integrato per il testing finale.  
- **WP6 (Sicurezza e Privacy)**: Le misure di sicurezza devono essere implementate per i test di vulnerabilità.   

#### **Tool o Software Necessari**
- **Strumenti di testing unitario**: pytest per backend, Jest per frontend.  
- **Strumenti di simulazione**: Apache JMeter per test di carico e stress.  
- **Strumenti di sicurezza**: OWASP ZAP o Burp Suite per test di vulnerabilità.  
- **Ambiente di test**: Server dedicati o ambienti virtualizzati per test end-to-end.  

#### **Ruoli richiesti**
- **Quality Assurance Engineer**: Esperto in testing manuale e automatico, con conoscenza di strumenti di testing avanzati.  
- **System Engineer**: Per supportare i test di carico, stress e integrazione complessa.  

#### **Costo per ognuno (calcolato in funzione del mese/uomo)**
- **Quality Assurance Engineer**: €5.000/mese  
- **Project Manager**: €6.000/mese

#### **Costo totale WP7**
- **€64.000**

---


## RISCHI

#### **Rischi e Mitigazioni WP1**
1. **Ritardi nella definizione dei requisiti**:
   - *Rischio*: Mancanza di chiarezza sui dati necessari potrebbe ritardare la progettazione.  
   - *Mitigazione*: Pianificazione di riunioni iniziali con il team per chiarire tutti i requisiti.  
2. **Scarsa ottimizzazione delle query**:
   - *Rischio*: Query lente che possono degradare le prestazioni del sistema.  
   - *Mitigazione*: Eseguire benchmark con dataset simulati e utilizzare strumenti di profilazione (es. EXPLAIN).  
3. **Incompatibilità con altri componenti**:
   - *Rischio*: Il database potrebbe non essere compatibile con il backend o il car controller.  
   - *Mitigazione*: Collaborazione continua con gli sviluppatori backend per allineare formati e strutture.  

#### **Rischi e Mitigazioni WP2**
1. **Integrazione del modello FER complicata**:
   - *Rischio*: Complessità tecnica nell’adattare il modello FER al backend.  
   - *Mitigazione*: Collaborazione stretta con il team che ha sviluppato il modello e test incrementali.  
2. **Problemi di performance delle API**:
   - *Rischio*: Lentezza nella gestione delle richieste in scenari con alto carico.  
   - *Mitigazione*: Ottimizzazione delle API con caching e tecniche di load balancing.  
3. **Problemi di sicurezza**:
   - *Rischio*: Possibili vulnerabilità nelle comunicazioni.  
   - *Mitigazione*: Utilizzo di protocolli sicuri (es. HTTPS) e test di vulnerabilità regolari.  

#### **Rischi e Mitigazioni WP3**
1. **Incompatibilità hardware/software**:
   - *Rischio*: Il modello FER potrebbe non essere ottimizzato per il dispositivo scelto.  
   - *Mitigazione*: Scelta di hardware compatibile fin dalle fasi iniziali e test incrementali.  
2. **Raccolta dati sensoriali incompleta**:
   - *Rischio*: Problemi di accesso ai dati del veicolo tramite CAN bus.  
   - *Mitigazione*: Collaborazione con esperti di integrazione veicolare e simulazioni preliminari.  
3. **Comunicazione lenta con il backend**:
   - *Rischio*: Latenza eccessiva nella trasmissione dei dati.  
   - *Mitigazione*: Utilizzo di protocolli ottimizzati (es. compressione dei dati, batch requests).  

#### **Rischi e Mitigazioni WP4**
1. **Problemi di compatibilità multi-piattaforma**:
   - *Rischio*: L’app potrebbe non funzionare correttamente su tutti i dispositivi.  
   - *Mitigazione*: Utilizzo di framework come Flutter o React Native per garantire compatibilità nativa.  
2. **UI/UX non intuitiva**:
   - *Rischio*: Gli utenti potrebbero trovare l’app difficile da usare.  
   - *Mitigazione*: Validazione del design tramite test con utenti reali e iterazioni sul design.  
3. **Problemi di comunicazione con il backend**:
   - *Rischio*: API non ottimizzate potrebbero causare ritardi o errori nell’app.  
   - *Mitigazione*: Collaborazione costante con il team backend per ottimizzare le API.  

#### **Rischi e Mitigazioni WP5**
1. **Problemi di compatibilità tra componenti**:
   - *Rischio*: API o protocolli non allineati tra backend e car controller/frontend.  
   - *Mitigazione*: Revisione delle specifiche API prima dell’integrazione e test incrementali.  
2. **Colli di bottiglia nelle comunicazioni**:
   - *Rischio*: Lentezza nella trasmissione dei dati tra le componenti.  
   - *Mitigazione*: Ottimizzazione delle API e utilizzo di strumenti di monitoraggio delle prestazioni.  
3. **Errori nei test end-to-end**:
   - *Rischio*: Problemi imprevisti che rallentano l’integrazione.  
   - *Mitigazione*: Allocare tempo extra per debugging e iterazioni.  

#### **Rischi e Mitigazioni WP6**
1. **Problemi di performance dovuti alla crittografia**:
   - *Rischio*: La crittografia potrebbe aumentare i tempi di risposta del sistema.  
   - *Mitigazione*: Utilizzo di hardware ottimizzato per crittografia (es. HSM) e ottimizzazione delle query.  
2. **Conformità incompleta al GDPR**:
   - *Rischio*: Alcuni aspetti delle policy potrebbero non rispettare completamente la normativa.  
   - *Mitigazione*: Collaborazione con un consulente legale esperto in GDPR e revisione continua.  
3. **Vulnerabilità nel sistema**:
   - *Rischio*: Possibili falle di sicurezza nel backend o nelle API.  
   - *Mitigazione*: Test di vulnerabilità regolari e simulazione di attacchi.  
  
#### **Rischi e Mitigazioni WP7**
1. **Bug critici rilevati in fase avanzata**:
   - *Rischio*: Problemi significativi potrebbero emergere durante il testing finale.  
   - *Mitigazione*: Eseguire test incrementali e continui durante l’intero ciclo di sviluppo.  
2. **Difficoltà nei test di carico**:
   - *Rischio*: Simulazioni di carico potrebbero non rappresentare scenari reali.  
   - *Mitigazione*: Utilizzo di strumenti avanzati per simulare traffico realistico.  
3. **Tempi di testing insufficienti**:
   - *Rischio*: Ritardi nelle fasi precedenti potrebbero ridurre il tempo disponibile per i test.  
   - *Mitigazione*: Riservare tempo extra per il testing nel piano di progetto. 