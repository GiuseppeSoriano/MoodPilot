![MoodPilot](MoodPilot.png)

**MoodPilot** combines "mood" and "pilot" to emphasize emotional monitoring for improved guidance in ride-hailing and autonomous driving services.

## Project Overview

MoodPilot is an innovative system designed to assess passenger satisfaction and emotional responses during trips in self-driving cars or ride-hailing services. By leveraging Facial Expression Recognition (FER) and passenger feedback, the system evaluates driving quality and passenger comfort, paving the way for adaptive, emotion-aware mobility solutions.

The system includes the following objectives:
- Evaluate passengers' emotions using advanced FER models.
- Rate drivers or autonomous systems based on user satisfaction.
- Collect and analyze emotional data for future system enhancements.
- Explore real-time performance on edge devices like Raspberry Pi.

This project was developed for educational purposes as part of the *Industrial Applications* exam within the Master's program in Computer Engineering at the University of Pisa.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/GiuseppeSoriano/MoodPilot.git
    ```

2. **Navigate to the project directory:**
    ```bash
    cd MoodPilot
    ```

3. **Install dependencies for your environment:**
    - For Raspberry Pi:
        ```bash
        pip install -r requirements_raspberrypi.txt
        ```
    - For other platforms:
        ```bash
        pip install -r requirements.txt
        ```

## Demo Setup

### Raspberry Pi 3B+ Configuration
- **Hardware**: Raspberry Pi 3B+ with a Camera Module 2 for live video input.
- **Operating System**: Raspberry Pi OS 64-bit (Debian 12).
- **Emotion Detection**: HSEmotionONNX with Haar Cascade for face detection.

### Running the Demo
1. **Camera Preview**:
    ```bash
    python3 Prototype/FER/camera.py
    ```
2. **Real-Time Emotion Detection**:
    ```bash
    cd Prototype/FER/Models/HSEmotionONNX
    python3 hsemotion_onnx.py
    ```

---

## Data Collection System

The **Data Collection System** is a key component of MoodPilot, designed to capture passenger feedback and emotional data during rides. It consists of a backend for emotion recognition and data storage, and a frontend for user interaction.

### Backend

The backend system processes uploaded videos, performs emotion recognition using the HSEmotionONNX model, and stores the data in MongoDB. It also provides REST API endpoints for seamless communication with the frontend.

#### Features
- **Emotion Recognition**: 
  - Processes video inputs to detect emotions using the HSEmotionONNX model.
  - Supports real-time processing and logs valence/arousal metrics.
- **REST API Endpoints**:
  - `POST /report`: Uploads and processes video feedback from passengers.
  - `GET /`: Confirms that the API is working.
- **Database Integration**:
  - MongoDB is used to store user feedback, ride details, and emotion recognition logs.
  - Scalable structure to support large datasets and analytics.

#### Setup Instructions

1. **Install Dependencies**:
   - Using Conda (preferred):
     ```bash
     conda create -n datacollector_backend python=3.12 -y
     conda activate datacollector_backend
     pip install -r requirements.txt
     ```
   - Alternatively, use any other Python environment to install the required modules.

2. **Environment Configuration**:
   - Navigate to the backend directory:
     ```bash
     cd Prototype/DataCollector/Backend
     ```
   - Create a `.env` file with the following content:
     ```env
     MONGO_HOST=
     MONGO_PORT=
     MONGO_DB=
     CORS_ORIGINS=
     ```
   - Replace the placeholders with your MongoDB configuration.

3. **Run the Backend**:
   - Start the Flask server on port `8080`:
     ```bash
     flask run --host=:: --port=8080
     ```

---

### Frontend

The frontend provides a user-friendly interface for passengers to submit feedback and upload video data. It is built using Angular and communicates with the backend through secure API endpoints.

#### Features
1. **Feedback Form**:
   - Allows passengers to rate their ride experience using a star-based rating system.
   - Provides options to specify discomfort moments during the ride.
2. **Drag-and-Drop File Upload**:
   - An intuitive interface for uploading videos captured during the ride.
   - Ensures file validation (size and format) before submission.
3. **Backend Integration**:
   - Submits form data and videos to the backend for processing and storage.

#### Setup Instructions

##### Prerequisites
- **Node.js**: Ensure Node.js is installed. [Download here](https://nodejs.org).
- **npm**: Comes bundled with Node.js.

##### Installation Steps

1. **Install Angular CLI**:
   ```bash
   npm install -g @angular/cli
   ```

2. **Navigate to the Frontend Directory**:
   ```bash
   cd Prototype/DataCollector/Frontend
   ```

3. **Install Dependencies**:
   ```bash
   npm install
   ```

##### Running the Frontend

1. **Start the Angular Server**:
   ```bash
   ng serve
   ```

2. **Access the Application**:
   - Open your browser and go to:
     ```
     http://localhost:4200
     ```

##### Environment Specifications
- **Angular CLI**: 17.3.11
- **Node.js**: 20.5.1
- **npm**: 9.8.0

**Angular Package Versions**:
- Angular: 17.3.11
- rxjs: 7.8.1
- typescript: 5.4.5

---

### Workflow

1. **Passenger Interaction**:
   - The user fills out a form to rate their ride and uploads a video file through the drag-and-drop interface.
2. **Backend Processing**:
   - The video is analyzed for emotion recognition using the HSEmotionONNX model.
   - Feedback data and results are stored in MongoDB.

---

### Summary of API Endpoints

| Method | Endpoint     | Description                          |
|--------|--------------|--------------------------------------|
| GET    | `/`          | Verifies the backend is running.    |
| POST   | `/report`    | Uploads and processes feedback data.|

---

### Recommendations
- Ensure the `.env` file is correctly configured with the database details.
- Align with the specified Angular and backend dependencies to avoid compatibility issues.
- Use Conda for backend environment management to simplify dependency installation.

## Palette

MoodPilot’s design draws on the following color palette for its visuals:
![Palette](Palette.png)
Palette created using [coolors.co](https://coolors.co/palette/f9dbbd-fca17d-da627d-9a348e-0d0628).

## References

For more details on the models and methodologies, see the full academic documentation available in `Prototype/Documentation`.
