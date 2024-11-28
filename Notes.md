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
