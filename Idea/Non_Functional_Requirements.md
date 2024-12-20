### **Non-Functional Requirements (NFRs)**

#### **NFR1: Accuracy and Consistency**
- The model must achieve a minimum accuracy of 80% in emotion recognition on a diverse and balanced dataset.

#### **NFR2: System Usability**
- The user interface for passengers and drivers should require no more than 3 steps to complete evaluations or provide feedback.  
- The system setup for new users or vehicles must be completed within 10 minutes.

#### **NFR3: Scalability and Extensibility**
- The architecture must support the addition of new models to detect facial expressions or customized forms without more than 1 hour of downtime during updates.

#### **NFR4: Privacy Protection**
- Sensitive data must not be stored for more than 30 days, unless explicitly authorized by users for specific purposes.

#### **NFR5: Resilience and Security**
- The system must ensure 99.9% uptime on a monthly basis, with scheduled downtime limited to a maximum of 4 hours per month.  
- All communications between the frontend and backend must be encrypted using TLS 1.3 standards.

#### **NFR6: Resource Efficiency**
- The system must consume a maximum of 120 Wh of energy per day on onboard devices, ensuring minimal impact on electric vehicle batteries.  
- The model for facial expression recognition must operate within 2 GB of RAM on embedded vehicle systems.

#### **NFR7: Backend Technology**
- The backend must be implemented in Python to ensure compatibility with the pre-developed models for facial expression recognition.  
- It should be compatible with Python frameworks like Flask for high performance and easy extensibility.