### **WP1: Database Configuration and Design (DB)**

#### **Classification**  
- **RI (Research and Innovation)**

#### **Motivation**  
A well-designed database is essential for efficiently storing and managing data collected by the system, such as FER evaluations, manual feedback, and sensor data from vehicles. Its structure must ensure query speed, data integrity, and scalability to handle an increasing number of vehicles and users.

#### **Activity Start / Activity End**  
- **Start**: Month 1  
- **End**: Month 2  

#### **Person-Months**  
- 1 project manager for 2 months (2 person-months).  
- 1 senior developer (DB) for 2 months (2 person-months).  

#### **Objectives**  
1. Design a robust, normalized database schema optimized for primary queries.  
2. Deploy the database on a local or cloud server.  
3. Ensure data scalability and integrity.  
4. Optimize queries for the backend and reporting system.  

#### **Tasks**  
1. **Requirements Analysis**:
   - Collect system-required data (FER, evaluations, feedback, sensor data).  
   - Identify relationships between main entities.  
2. **Schema Design**:
   - Define main tables (e.g., `Passengers`, `Drivers`, `Trips`, `FER_Data`, `Evaluations`).  
   - Normalize the schema to eliminate redundancies and ensure consistency.  
3. **Database Implementation**:
   - Create tables and define relationships (e.g., 1:N, N:N).  
   - Configure indexes to optimize primary queries.  
4. **Query Optimization**:
   - Develop queries for common operations (e.g., insert evaluations, calculate the average of the last 500 evaluations).  
   - Optimize performance on simulated datasets.  
5. **Testing and Validation**:
   - Verify referential integrity and query functionality.  
   - Simulate increasing loads to assess scalability.  

#### **Deliverables**  
1. **Database Schema**: Documented ER diagram model.  
2. **Implemented Database**: Fully operational database with all tables and defined relationships.  
3. **SQL Scripts**: Scripts for table creation, constraints, and indexes.  
4. **Report**: Documentation of primary queries and applied optimizations.  

#### **Milestones**  
1. ER diagram delivery (end of Month 1).  
2. Database implementation and working SQL scripts (mid-Month 2).  
3. Query validation and final report (end of Month 2).  

#### **Dependencies Among WPs**  
- **WP2 (Backend)**: Required to test communication between the database and API endpoints. Database design must be completed before proceeding with the backend.  
- **WP5 (Integration)**: Database must be complete and functional before system integration.

#### **Required Tools or Software**  
- **Relational Database**: MySQL or PostgreSQL (already available).  
- **Modeling Tools**: DbSchema or MySQL Workbench (already available).  
- **SQL Language**: For database implementation and optimization (no additional cost).  
- **Profiling Tools**: EXPLAIN for query analysis (available in chosen DBMS).  

#### **Required Roles**  
- **Database Developer**: Expert in relational database design and optimization (MySQL or PostgreSQL).  

#### **Cost Per Role (Based on Person-Months)**  
- **Database Developer**: €5,000/month  
- **Project Manager**: €6,000/month  

#### **Total WP1 Cost**  
- **€22,000**  

---

Ecco la traduzione completa degli altri WP:

---

### **WP2: Backend Development**

#### **Classification**  
- **RI (Research and Innovation)**

#### **Motivation**  
The backend is the core of the system, managing data flow between various components: database, car controller, and frontend. It must integrate the FER model, expose RESTful API endpoints, and ensure efficient management of evaluations and collected data, with a strong focus on security and scalability.

#### **Activity Start / Activity End**  
- **Start**: Month 2  
- **End**: Month 4  

#### **Person-Months**  
- 1 project manager for 3 months (3 person-months).  
- 2 backend developers for 3 months (6 person-months).  

#### **Objectives**  
1. Implement a robust and scalable backend in Python to manage data flow.  
2. Integrate the FER model for automatic evaluations.  
3. Expose RESTful API endpoints to communicate with the frontend and car controller.  

#### **Tasks**  
1. **Development Environment Setup**:
   - Configure the backend framework (e.g., Flask or FastAPI).  
   - Structure the project.  
2. **RESTful API Implementation**:
   - Create endpoints for communication with the car controller, frontend, and database (e.g., `/sendEvaluation`, `/getUserData`).  
   - Validate and authenticate API requests.  
3. **Database Integration**:
   - Connect to the database using an ORM (e.g., SQLAlchemy).  
   - Develop backend queries to handle complex data operations (e.g., calculate the average of the last 500 evaluations).  
4. **FER Model Integration**:
   - Implement functions to receive input from the car controller.  
   - Process and store FER data in the database.  
5. **Security and Privacy**:
   - Implement security protocols (e.g., TLS 1.3 for communications).  
   - Encrypt sensitive data.  
   - Create data management policies compliant with GDPR.  
6. **Testing and Validation**:
   - Test APIs (unit tests and integration tests).  
   - Simulate workloads to ensure scalability.  

#### **Deliverables**  
1. **Operational Backend**: Complete source code with API and FER model integration.  
2. **Technical Documentation**: Details on implementation, API endpoints, and usage instructions.  
3. **Data Management Logic**: Functions implemented to interact with the database and car controller.  
4. **Test Report**: Results of integration tests and load simulations.  

#### **Milestones**  
1. Delivery of basic working APIs (end of Month 2).  
2. Completed database integration (end of Month 3).  
3. Backend validation in a simulated environment (end of Month 4).  

#### **Dependencies Among WPs**  
- **WP1 (Database)**: Database design must be completed to develop the backend.  
- **WP5 (Integration)**: The backend must be completed to integrate components.

#### **Required Tools or Software**  
- **Backend Framework**: Flask or FastAPI (available).  
- **Security Libraries**: PyJWT for authentication, OpenSSL for encryption.  
- **ORM**: SQLAlchemy or equivalent for database interaction.  
- **Testing Tools**: Postman for API testing, pytest for automated tests.  

#### **Required Roles**  
- **Backend Developer**: Specialist in Python, experienced in RESTful API development and AI model integration.  
- **Data Engineer**: To optimize data flow between the backend and database.  

#### **Cost Per Role (Based on Person-Months)**  
- **Backend Developer**: €5,000/month  
- **Project Manager**: €6,000/month  

#### **Total WP2 Cost**  
- **€48,000**  

---

### **WP3: Car Controller Development**

#### **Classification**  
- **RI (Research and Innovation)**

#### **Motivation**  
The car controller is responsible for running the FER model onboard the vehicle. It must collect sensor data, process facial expressions in real-time, and communicate results to the backend. Its design must ensure efficiency, reliability, and low power consumption, as it is a critical system component.

#### **Activity Start / Activity End**  
- **Start**: Month 3  
- **End**: Month 5  

#### **Person-Months**  
- 1 project manager for 3 months (3 person-months).  
- 2 embedded developers for 3 months (6 person-months).  

#### **Objectives**  
1. Implement car controller software to run the FER model in real-time.  
2. Establish secure communication between the controller and the backend.  
3. Collect sensor data (e.g., speed, braking) and send it to the backend.  
4. Optimize performance for vehicle-specific hardware.  

#### **Tasks**  
1. **Hardware Setup**:
   - Configure the hardware environment (e.g., edge device, GPU, or TPU).  
   - Install libraries required to run the FER model.  
2. **FER Model Deployment**:
   - Adapt the FER model for embedded hardware.  
   - Test model performance in simulated scenarios.  
3. **Sensor Data Collection**:
   - Develop drivers or scripts to read data from the vehicle (e.g., CAN bus).  
   - Validate collected data and convert it into usable formats.  
4. **Backend Communication**:
   - Configure secure communication via RESTful APIs or WebSocket.  
   - Implement a protocol to transmit FER results and sensor data to the backend.  
5. **Optimization and Testing**:
   - Optimize performance to ensure low latency (<500 ms).  
   - Test in real environments and simulate workloads.  

#### **Deliverables**  
1. **Car Controller Software**: Complete code to run the FER model, collect data, and communicate with the backend.  
2. **Technical Report**: Implementation details, hardware configuration, and applied optimizations.  
3. **Test Logs**: Results from tests conducted in simulations and real scenarios.  

#### **Milestones**  
1. Completed hardware setup (end of Month 3).  
2. FER model deployment finalized (mid-Month 4).  
3. Backend communication functioning (end of Month 4).  
4. Validation in real environments (end of Month 5).  

#### **Dependencies Among WPs**  
- **WP2 (Backend)**: APIs must be completed to enable communication with the car controller.  
- **WP5 (Integration)**: The car controller must be developed and operational for system integration.

#### **Required Tools or Software**  
- **AI Framework**: TensorFlow Lite or PyTorch for running the FER model (available).  
- **Communication Libraries**: Requests or aiohttp for RESTful API.  
- **Car Controller Hardware**: Edge device with GPU support (e.g., NVIDIA Jetson Nano, Coral TPU).  
- **Simulation Tools**: CAN simulators for testing sensor data collection.  

#### **Required Roles**  
- **Embedded Developer**: Specialist in edge devices with expertise in AI and hardware optimization.  

#### **Cost Per Role (Based on Person-Months)**  
- **Project Manager**: €6,000/month  
- **Embedded Developer**: €5,500/month  

#### **Total WP3 Cost**  
- **€51,000**

### **WP4: Frontend Development (Mobile App)**

#### **Classification**  
- **RI (Research and Innovation)**

#### **Motivation**  
The mobile app is the main touchpoint between users (passengers and drivers) and the system. It must provide an intuitive and user-friendly interface to view evaluations, complete questionnaires, manage personal data, and interact with the backend. Effective design is essential for an excellent user experience.

#### **Activity Start / Activity End**  
- **Start**: Month 5  
- **End**: Month 6  

#### **Person-Months**  
- 1 project manager for 2 months (2 person-months).  
- 2 frontend developers for 2 months (4 person-months).  

#### **Objectives**  
1. Create an intuitive user interface for passengers and drivers.  
2. Implement features for viewing and modifying evaluations and questionnaires.  
3. Ensure a smooth user experience and compatibility with Android and iOS devices.  

#### **Tasks**  
1. **UI/UX Design**:
   - Create wireframes and mockups for key app sections (e.g., evaluation screens, user profiles).  
   - Validate design with a sample of users.  
2. **Implementation of Core Features**:
   - Integrate with the backend via RESTful APIs.  
   - Develop screens for viewing and modifying questionnaires generated by FER.  
   - Create sections for providing manual evaluations (passengers) and viewing evaluations (drivers).  
3. **Personal Data Management**:
   - Design a screen for user profile management, allowing data updates and visualization.  
   - Implement GDPR-compliant policies (e.g., data deletion requests).  
4. **App Testing**:
   - Test the app on Android and iOS devices to ensure compatibility and performance.  
   - Identify and fix bugs.  
5. **Final Optimization**:
   - Improve performance (e.g., loading times).  
   - Apply feedback from user tests.  

#### **Deliverables**  
1. **Functional Mobile App**: Fully operational for Android and iOS devices.  
2. **Technical Documentation**: Details on implementation, APIs used, and deployment instructions.  
3. **Test Report**: Results from tests on real devices.  

#### **Milestones**  
1. Delivery of finalized wireframes and mockups (end of Month 4).  
2. Core features implemented (end of Month 5).  
3. Complete testing and delivery of the final app version (end of Month 6).  

#### **Dependencies Among WPs**  
- **WP2 (Backend)**: Required to implement and test backend communication.  
- **WP5 (Integration)**: Frontend must be completed and tested for system integration.

#### **Required Tools or Software**  
- **Development Framework**: Flutter or React Native (available).  
- **Design Tools**: Figma or Adobe XD for UI/UX design.  
- **Communication Libraries**: Axios or HTTP for API integration.  
- **Testing Tools**: BrowserStack or real devices for cross-platform testing.  

#### **Required Roles**  
- **Frontend Developer**: Specialist in mobile development, proficient in Flutter/React Native.  

#### **Cost Per Role (Based on Person-Months)**  
- **Project Manager**: €6,000/month  
- **Frontend Developer**: €4,000/month  

#### **Total WP4 Cost**  
- **€20,000**

---

### **WP5: System Integration**

#### **Classification**  
- **SS (Support and Services)**

#### **Motivation**  
System integration ensures all components (DB, backend, car controller, and mobile app) communicate effectively. This WP focuses on making the system function cohesively and ensuring data flows seamlessly across components.

#### **Activity Start / Activity End**  
- **Start**: Month 7  
- **End**: Month 8  

#### **Person-Months**  
- 1 project manager for 2 months (2 person-months).  
- 1 system integrator for 2 months (2 person-months).  

#### **Objectives**  
1. Ensure smooth communication between system components.  
2. Validate data flow in real and simulated scenarios.  
3. Identify and resolve interoperability issues.  

#### **Tasks**  
1. **Preparation for Integration**:
   - Review interfaces and APIs exposed by the backend and mobile app.  
   - Configure a test environment for integration.  
2. **Backend-Database Integration**:
   - Validate query handling and data storage.  
   - Test primary operations (e.g., read/write evaluation data).  
3. **Backend-Car Controller Integration**:
   - Validate secure transmission of FER and sensor data from the car controller to the backend.  
   - Test communication latency.  
4. **Backend-Frontend Integration**:
   - Verify functionality of RESTful APIs for the frontend.  
   - Test core features (e.g., retrieving questionnaires, submitting evaluations).  
5. **Bug Fixing and Optimization**:
   - Resolve bugs identified during tests.  
   - Optimize data flow to reduce latency and improve performance.  

#### **Deliverables**  
1. **Integrated System**: All components functioning cohesively.  
2. **Technical Report**: Details on integration, tests performed, and resolved issues.  
3. **End-to-End Test Logs**: Results from real-world simulations and tests.  

#### **Milestones**  
1. Backend-database integration completed (end of Week 2, Month 7).  
2. Backend-car controller integration completed (end of Month 7).  
3. Backend-frontend integration completed (mid-Month 8).  
4. End-to-end testing completed (end of Month 8).  

#### **Dependencies Among WPs**  
- **WP1 (Database)**: Database must be complete and functional for backend integration.  
- **WP2 (Backend)**: Backend must be operational to integrate with other components.  
- **WP3 (Car Controller)**: Car controller must be ready to transmit data to the backend.  
- **WP4 (Frontend)**: Mobile app must be completed to test frontend-backend communication.

#### **Required Tools or Software**  
- **Monitoring Tools**: Postman for API testing, Grafana for monitoring data flow.  
- **Integration Environment**: Local or cloud server with dedicated configuration.  
- **Simulators and Real Tests**: CAN simulators for car controller data and real mobile devices for frontend tests.  

#### **Required Roles**  
- **System Integrator**: Specialist in complex system integration, with backend, API, and infrastructure expertise.  

#### **Cost Per Role (Based on Person-Months)**  
- **System Integrator**: €6,000/month  
- **Project Manager**: €6,000/month  

#### **Total WP5 Cost**  
- **€24,000**

---

### **WP6: Security and Privacy**

#### **Classification**  
- **SS (Support and Services)**

#### **Motivation**  
Protecting sensitive data collected by the system is essential to comply with GDPR and ensure user information security. This WP focuses on implementing advanced security protocols, data encryption, and GDPR-compliant policies.

#### **Activity Start / Activity End**  
- **Start**: Month 6  
- **End**: Month 7  

#### **Person-Months**  
- 1 project manager for 2 months (2 person-months).  
- 1 security expert for 2 months (2 person-months).  

#### **Objectives**  
1. Ensure secure communication between system components.  
2. Protect sensitive data through encryption and controlled access.  
3. Ensure compliance with GDPR and other applicable regulations.  

#### **Tasks**  
1. **Data Encryption**:
   - Implement AES-256 encryption for data stored in the database.  
   - Configure TLS 1.3 for communications between car controller, backend, and frontend.  
2. **Credential Management and Authentication**:
   - Develop a token-based authentication system (e.g., JWT) for RESTful APIs.  
   - Create mechanisms for secure credential management (e.g., bcrypt hashing).  
3. **GDPR Compliance and Privacy Policies**:
   - Create tools for users to view, modify, and delete their data.  
   - Implement anonymization logic for historical data.  
4. **Monitoring and Audit**:
   - Configure monitoring tools to detect suspicious activities.  
   - Conduct system audits to verify compliance with security and privacy policies.  
5. **Testing and Validation**:
   - Conduct vulnerability tests on APIs and stored data.  
   - Simulate common attacks (e.g., SQL injection, man-in-the-middle) to ensure system robustness.  

#### **Deliverables**  
1. **Security and Privacy Policies**: Detailed document of implemented measures and procedures for handling sensitive data.  
2. **Secure System**: All communications and data protected by encryption and controlled access.  
3. **Audit Report**: GDPR compliance and system security assessment.  
4. **Test Logs**: Results of vulnerability and security tests.  

#### **Milestones**  
1.	Completed the documentation of Security and Privacy Policies, including handling of sensitive data (end of Month 6).
2.	Achieved encryption of all communications and stored data, with controlled access (mid-Month 7).
3.	Conducted vulnerability tests and generated comprehensive test logs (end of Month 7).
4.	Finalized the GDPR compliance assessment and completed the Audit Report (end of Month 7).

#### **Dependencies Among WPs**  
- **WP1 (Database)**: Database must be complete for stored data encryption.  
- **WP2 (Backend)**: Necessary for implementing authentication and API security mechanisms.  

#### **Required Tools or Software**  
- **Encryption Tools**: OpenSSL for TLS, PyCryptodome for AES.  
- **Authentication Framework**: PyJWT for token management.  
- **Audit Tools**: OWASP ZAP or Burp Suite for security testing.  
- **Monitoring**: Grafana or equivalent for activity detection.  

#### **Required Roles**  
- **Security Engineer**: Expert in cybersecurity and GDPR compliance.  

#### **Cost Per Role (Based on Person-Months)**  
- **Security Engineer**: €5,500/month  
- **Project Manager**: €6,000/month  

#### **Total WP6 Cost**  
- **€23,000**

---

### **WP7: System Testing and Acceptance**

#### **Classification**  
- **SS (Support and Services)**

#### **Motivation**  
Testing and validation are essential to ensure the system meets functional and non-functional requirements. This WP focuses on unit, integration, and end-to-end testing, ensuring the system operates correctly in real scenarios and is robust, reliable, and secure.

#### **Activity Start / Activity End**  
- **Start**: Month 1  
- **End**: Month 9  

#### **Person-Months**  
- 1 project manager for 4 months (4 person-months).  
- 2 QA engineers for 4 months (8 person-months).  

#### **Objectives**  
1. Validate that all components meet functional and non-functional requirements.  
2. Identify and resolve bugs or issues across system components.  
3. Ensure the system integrates all components correctly.  
4. Test system robustness under load and stress conditions.  

#### **Tasks**  
1. **Unit Testing**:
   - Create and execute unit tests for each component (DB, backend, frontend, car controller).  
   - Verify code coverage (at least 80%).  
2. **Integration Testing**:
   - Test interactions between the backend and database.  
   - Verify communication between the car controller and backend.  
   - Validate frontend-backend interaction through APIs.  
3. **End-to-End Testing**:
   - Simulate complete scenarios, such as a trip with FER data collection, processing, and feedback.  
   - Verify complete data flow and integrity.  
4. **Performance Testing**:
   - Simulate high loads to test system scalability.  
   - Measure API response times (<200 ms under normal load).  
5. **Security Testing**:
   - Verify implemented security measures (e.g., encryption, authentication).  
   - Simulate common attacks (SQL injection, brute force, man-in-the-middle).  
6. **Issue Resolution**:
   - Analyze test results to identify bugs or bottlenecks.  
   - Resolve issues and retest to confirm fixes.  

#### **Deliverables**  
1. **Testing Report**: Detailed documentation of tests, results, and resolved issues.  
2. **Validated System**: Confirmation that the system meets functional and non-functional requirements.  
3. **Test Logs**: Detailed records of all tests, including load and vulnerability tests.  

#### **Milestones**  
<!-- Progettare casi di test per singoli componenti al primo mese -->
1. Complete design of test cases for all components (end of Month 1).
2. Completed unit testing for backend and car controller components (end of Month 6).  
3. Completed end-to-end and security testing (end of Month 8).  
4. Completed integration testing (mid-Month 9).  

#### **Dependencies Among WPs**  
- **WP1 (Database)**: Required for integration tests with the backend.  
- **WP2 (Backend)**: Must be ready to verify APIs and data handling logic.  
- **WP3 (Car Controller)**: Must be operational to validate FER data transmission.  
- **WP4 (Frontend)**: Mobile app must be completed for end-to-end testing.  
- **WP5 (Integration)**: Entire system must be integrated for final testing.  
- **WP6 (Security and Privacy)**: Security measures must be implemented for vulnerability testing.

#### **Required Tools or Software**  
- **Unit Testing Tools**: pytest for backend, Jest for frontend.  
- **Simulation Tools**: Apache JMeter for load and stress testing.  
- **Security Tools**: OWASP ZAP or Burp Suite for vulnerability testing.  
- **Testing Environment**: Dedicated servers or virtual environments for end-to-end tests.  

#### **Required Roles**  
- **Quality Assurance Engineer**: Expert in manual and automated testing, familiar with advanced testing tools.  
- **System Engineer**: To support load, stress, and complex integration tests.  

#### **Cost Per Role (Based on Person-Months)**  
- **Quality Assurance Engineer**: €5,000/month  
- **Project Manager**: €6,000/month  

#### **Total WP7 Cost**  
- **€64,000**

---

### TOTAL COST

#### **Total WP1 Cost**  
- **€22,000**  

#### **Total WP2 Cost**
- **€48,000**

#### **Total WP3 Cost**
- **€51,000**

#### **Total WP4 Cost**
- **€20,000**

#### **Total WP5 Cost**
- **€24,000**

#### **Total WP6 Cost**
- **€23,000**

#### **Total WP7 Cost**
- **€64,000**

#### **Grand Total**
- **€252,000**