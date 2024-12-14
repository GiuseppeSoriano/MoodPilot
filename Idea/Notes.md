# 1. Just some notes

## 1.1. Ideas

- Regarding the privacy issue, we can ensure that each car has models that directly calculate the rating to be given to the driver. At the end of the ride, only the rating is sent to the server without transmitting all the footage.

## 1.2. Slides structure

Architecture with modules
Work Package and Task.
Plan the development.
Programming to implement the system.
Profiles needed to develop the project.
General profile + specific skills.
How much does it cost to implement this project?
How many hours? And when do we need the resources?
And what about Testing?

WHAT ARE THE RISKS? It is not credible that a project has no risks.
We do not produce all the components.
Eliminate the risk or reduce its effects, we need to find a strategy.
This involves a cost.
Follow this scheme for the slides: RISK -> STRATEGY -> RESULTING COST.

Sensors: only what is needed (relative to the characteristics).

--- 

### 1.2.1. II PART: MoodPilot System Design and Implementation

#### 1.2.1.1. **System Architecture**  

The system will be divided into the following key modules:  
- **Mood Detection Module**: Leverages computer vision and machine learning for real-time analysis of passengers' facial expressions.  
- **Sensor Integration Module**: Collects and processes physiological data using connected sensors.  
- **Driver Evaluation Module**: Compiles passenger feedback and mood data to assess driving performance.  
- **User Interface Module**: Provides an intuitive frontend for passengers to rate their experience and leave comments.  
- **Data Management Module**: Ensures secure storage and processing of data for further analysis and improvement.

#### 1.2.1.2. **Work Packages and Tasks**  

- **WP1: Requirements Gathering and Design**  
  - Task 1.1: Identify system requirements.  
  - Task 1.2: Design the architecture and data flow.  

- **WP2: Development of Core Modules**  
  - Task 2.1: Implement Mood Detection Module.  
  - Task 2.2: Develop Sensor Integration and Data Management Modules.  

- **WP3: User Interface Development**  
  - Task 3.1: Design and build a user-friendly frontend.  
  - Task 3.2: Integrate the feedback system.  

- **WP4: Testing and Validation**  
  - Task 4.1: Conduct unit and integration testing.  
  - Task 4.2: Validate system performance with real-world data.

- **WP5: Deployment and Monitoring**  
  - Task 5.1: Deploy the system in a test environment.  
  - Task 5.2: Monitor and refine based on feedback.

#### 1.2.1.3. **Project Planning and Resources**  

- **Development Timeline**: Estimate of 6-9 months.  
- **Resource Requirements**:  
  - Software engineers (backend and frontend specialists).  
  - Data scientists (machine learning and AI expertise).  
  - UX/UI designers.  
  - Hardware specialists (sensor integration).  

- **Budget Considerations**:  
  - Equipment and sensors.  
  - Cloud infrastructure for data storage and processing.  
  - Development and testing costs.

- **Testing Strategy**:  
  - Employ iterative testing cycles, focusing on:  
    - Functional testing of individual modules.  
    - Usability testing with sample users.  
    - Stress testing under different environmental conditions.

#### 1.2.1.4. **Risk Management**  

- **Identified Risks**:  
  - **Data Privacy and Security**: Ensuring compliance with regulations (e.g., GDPR).  
  - **Technical Challenges**: Integration of sensors and real-time data processing.  
  - **User Acceptance**: Potential reluctance from passengers regarding biometric monitoring.  

- **Mitigation Strategies**:  
  - **Risk**: Data Privacy Concerns.  
    - **Strategy**: Use federated learning and anonymization techniques.  
    - **Cost Impact**: Moderate investment in privacy-preserving technologies.  

  - **Risk**: Sensor Malfunction or Inaccuracy.  
    - **Strategy**: Implement redundant systems and regular calibration.  
    - **Cost Impact**: Increased maintenance and equipment costs.  

  - **Risk**: System Performance Under Real-World Conditions.  
    - **Strategy**: Conduct pilot tests and gather feedback for continuous improvement.  
    - **Cost Impact**: Allocating resources for extended testing phases.

#### 1.2.1.5. **Sensor Selection and Usage**  

Only essential sensors will be used to maintain cost-effectiveness and efficiency, focusing on features critical to mood detection and safety evaluation.



--- 

Specifica.
Vita di ogni parte del sistema cambia in base alla parte in esame.
Tolleranza ai guaasti di ogni parte del sistema cambia.
Un progetto non è mai omogeneo. 
Mai considerare un progetto omogeneo.
Mancano ancora i requisiti non funzionali (imaginare qualche requisito per la nostra applicazione)
Fanno sempre riferimento alle caratteristiche che deve avere una o più funzionalità. 
Bisogna anche speicifcare i Vincoli di progettazione. 
Vado a progettare architettura. 
Ci sono infinite architetture.
Non tutte vanno bene in termini di requisiti e vincoli. 
Ne scelgo due e porto avanti due.
E' una tecnica di gestione dei rischi.

Sottosistemi del nostro sistema (architettura)
Ognuno deve essere specificato con quanto detto prima
Work package per ogni sottosistema. 
Software system engineering in ogni work package.
Ogni work package mi deve dare un prototipo da collaudare 
Pesi ad ogni requisito e vincolo. Molte volte requisiti non funzionali sono in conflitto tra loro.
Capire quale è più importante. 
Sottoparti che hanno caratteristiche specifiche. 
Scegliere cosa fare: 
- Compro un componente
- Progetto un componente
- o Riuso (componente già fatto mio).

Per ogni workpackage devo individuare caratteristiche.
Definire componente, in modo da valutare stato di lavoro su esso.
Individuarlo nel tempo e nelle risorse. 
Ha inizio e fine.
Quante risorse uso e quando le uso.
Farlo per tutti i workpackage.
Piano completo di progetto raggiunto.
Distinguere profili utenti:
- competenze 
- tempo e costo
- probabilità di errore

Utente:
- cosa deve fare
- competenze applicative
- conoscenze informatiche

Copiare soluzioni già testate.
Sforzo cognitivo nel capire applicazione è importante.
Considerare la frequenza di ogni operazione. 


Una specifica deve essere:
- esaustiva
- misurabile
- Etichettare in maniera univoca funzionalità

Diversi task dentro ogni workpackage.
Task sono attività che richiedono risorse o competenze specifiche. 

Specifica incompleta è errata. Porta sicuramente a errori.

Emulatore serve in ambienti dove posso fare danni
A volte è più complesso del sistema reale.
Due collaudi: presso produzione e in uso.



Here's an updated and integrated version of your system design and planning for **MoodPilot**, incorporating the additional lecture notes:

---

## **II PART: MoodPilot System Design and Implementation**

### **System Architecture**  
The system will follow a modular architecture, designed to meet functional and non-functional requirements, while also accommodating fault tolerance and specific operational lifecycles. Key subsystems include:

1. **Mood Detection Subsystem**  
   - **Functionality**: Analyze passenger emotions in real-time using facial expression recognition and physiological data.  
   - **Non-Functional Requirements**: High accuracy, low latency, privacy compliance.  
   - **Constraints**: Limited computational resources within the vehicle.

2. **Driver Evaluation Subsystem**  
   - **Functionality**: Aggregate mood data and passenger feedback to provide a comprehensive driver assessment.  
   - **Non-Functional Requirements**: Scalability, robustness.  
   - **Constraints**: Integration with external databases for long-term data storage.

3. **User Interface Subsystem**  
   - **Functionality**: Enable passengers to rate the trip and submit feedback.  
   - **Non-Functional Requirements**: Intuitive design, accessibility.  
   - **Constraints**: Must work across different devices.

4. **Data Management Subsystem**  
   - **Functionality**: Securely store and manage data.  
   - **Non-Functional Requirements**: Data security, redundancy.  
   - **Constraints**: Compliance with GDPR and other data protection regulations.

### **Work Packages and Tasks**  
Each work package (WP) targets a subsystem and contains multiple tasks to deliver a testable prototype:

- **WP1: Mood Detection Subsystem**  
  - **Task 1.1**: Develop facial recognition algorithms.  
  - **Task 1.2**: Integrate physiological sensors.  
  - **Task 1.3**: Test and validate detection accuracy.  
  - **Deliverable**: Prototype of real-time mood detection module.

- **WP2: Driver Evaluation Subsystem**  
  - **Task 2.1**: Develop data aggregation logic.  
  - **Task 2.2**: Implement evaluation metrics.  
  - **Task 2.3**: Run simulations with collected data.  
  - **Deliverable**: Driver performance evaluation prototype.

- **WP3: User Interface Subsystem**  
  - **Task 3.1**: Design wireframes and mockups.  
  - **Task 3.2**: Develop frontend application.  
  - **Task 3.3**: Conduct usability testing.  
  - **Deliverable**: Interactive user interface prototype.

- **WP4: Data Management Subsystem**  
  - **Task 4.1**: Set up databases.  
  - **Task 4.2**: Implement encryption and data protection.  
  - **Task 4.3**: Ensure compliance with legal frameworks.  
  - **Deliverable**: Secure data storage and processing module.

- **WP5: Integration and Testing**  
  - **Task 5.1**: Integrate subsystems.  
  - **Task 5.2**: Perform end-to-end testing in simulated environments.  
  - **Task 5.3**: Conduct field testing in real-world conditions.  
  - **Deliverable**: Fully integrated, tested system.

### **Non-Functional Requirements**  
Non-functional requirements guide performance, usability, and reliability. Examples include:  
- **Performance**: System should process real-time data with minimal latency.  
- **Reliability**: Ensure fault tolerance with backup systems.  
- **Security**: Enforce strict data protection measures.  
- **Usability**: Design intuitive interfaces for passengers with diverse technical skills.

### **Design Constraints and Decision-Making**  
- **Constraints**: Limited onboard processing power, regulatory requirements, and budget limitations.  
- **Risk Mitigation Strategy**:  
   - Develop two alternative architectures, evaluate against requirements, and select the most suitable one.  
   - Use a mix of custom-designed, off-the-shelf, and reusable components to balance cost and functionality.

### **Resource Planning and Profiling**  
- **Team Profiles**:  
   - **Software Engineers**: Backend and frontend specialists.  
   - **Data Scientists**: Expertise in AI and machine learning.  
   - **Hardware Engineers**: Sensor integration and calibration.  
   - **UX Designers**: Focus on user experience and interface design.

- **Resource Allocation**:  
   - Allocate specific hours and resources for each task.  
   - Define start and end dates for each task to ensure proper scheduling.  

### **Risk Management**  
- **Identified Risks and Strategies**:  
   - **Risk**: Privacy concerns with biometric data.  
     - **Strategy**: Implement federated learning and anonymization techniques.  
     - **Cost Impact**: Investment in privacy-preserving technologies.  
   - **Risk**: Technical failures in real-time data processing.  
     - **Strategy**: Develop redundant systems and conduct regular maintenance.  
     - **Cost Impact**: Increased maintenance costs.  
   - **Risk**: User resistance to monitoring.  
     - **Strategy**: Provide transparency and clear consent mechanisms.  
     - **Cost Impact**: Minimal, but requires careful communication.

### **Testing and Prototyping**  
- **Emulation and Simulation**:  
   - Use emulators to simulate real-world conditions. Emulation can be more complex than the real system but essential to avoid risks during field tests.  
   - Conduct two levels of testing:  
     - **Production Site Testing**: Controlled environment.  
     - **In-Use Testing**: Real-world deployment with feedback collection.

---

Using the structure from the example provided, here’s a detailed breakdown of the **MoodPilot** work packages (WP) aligned with your project requirements and goals:

---


## **Work Package Overview**  

### **WP1: Mood Detection and Analysis**  
**Objective:** Develop and implement the system for real-time mood detection using facial expression recognition and physiological sensors.  

- **Tasks:**  
  - **Task 1.1:** Develop facial expression recognition algorithms.  
    - **Sub-tasks:**  
      - Collect datasets.  
      - Train machine learning models.  
  - **Task 1.2:** Integrate physiological sensors for emotion tracking.  
  - **Task 1.3:** Test and validate the detection module in controlled environments.  

- **Deliverables:**  
  - A functional mood detection prototype.  
  - Performance reports and accuracy benchmarks.

---

### **WP2: Driver Evaluation System**  
**Objective:** Aggregate passenger mood data and feedback to assess driver performance.  

- **Tasks:**  
  - **Task 2.1:** Develop a scoring system based on mood and safety metrics.  
  - **Task 2.2:** Implement algorithms for aggregating real-time data.  
  - **Task 2.3:** Simulate and evaluate driver performance based on sample datasets.  

- **Deliverables:**  
  - Driver evaluation module.  
  - Reports on aggregated data results.

---

### **WP3: User Feedback Interface**  
**Objective:** Design and deploy a user-friendly interface for passengers to provide feedback and rate trips.  

- **Tasks:**  
  - **Task 3.1:** Design interface wireframes and prototypes.  
  - **Task 3.2:** Develop and integrate the user interface with backend systems.  
  - **Task 3.3:** Conduct usability testing with a focus group.  

- **Deliverables:**  
  - Interactive frontend.  
  - Usability test results.

---

### **WP4: Data Management and Security**  
**Objective:** Ensure secure storage and processing of passenger and trip data.  

- **Tasks:**  
  - **Task 4.1:** Set up cloud-based data infrastructure.  
  - **Task 4.2:** Implement data encryption and access control mechanisms.  
  - **Task 4.3:** Conduct audits for GDPR compliance.  

- **Deliverables:**  
  - Secure data management platform.  
  - Compliance reports.

---

## **Project Timeline**  
- **Phase 1:** Initial design and development (Months 1-3).  
- **Phase 2:** Module integration and testing (Months 4-6).  
- **Phase 3:** Field testing and deployment (Months 7-9).

## **Resources and Budget**  
- **Roles:**  
  - Software Developers (Frontend & Backend).  
  - Data Scientists (AI & ML expertise).  
  - Hardware Engineers (Sensor Integration).  
  - Legal Advisor (Data Privacy Compliance).  
- **Cost Estimates:**  
  - Equipment and sensors: €XX,XXX.  
  - Cloud infrastructure: €XX,XXX.  
  - Development and personnel costs: €XX,XXX.

---

## **Risk Management**  
Following a structured approach for risk identification and mitigation:  

| **Risk**                          | **Strategy**                                          | **Cost Impact**            |  
|------------------------------------|------------------------------------------------------|----------------------------|  
| Privacy concerns                   | Use federated learning and anonymization.            | Moderate.                  |  
| Sensor inaccuracies                | Deploy redundant systems and regular calibrations.   | Increased maintenance.     |  
| User adoption issues               | Clear consent process and transparency campaigns.   | Minimal but requires time. |  

---












