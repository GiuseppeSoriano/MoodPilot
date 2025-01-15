![MoodPilot](MoodPilot.png)

**MoodPilot** combines "mood" and "pilot" to emphasize emotional monitoring for improved guidance in ride-hailing and autonomous driving services.

## Project Overview

MoodPilot is an innovative system designed to assess passenger satisfaction and emotional responses during trips in self-driving cars or ride-hailing services. By leveraging Facial Expression Recognition (FER) and passenger feedback, the system evaluates driving quality and passenger comfort, paving the way for adaptive, emotion-aware mobility solutions.

The system includes the following objectives:
- Evaluate passengers' emotions using advanced FER models.
- Rate drivers or autonomous systems based on user satisfaction.
- Collect and analyze emotional data for future system enhancements.
- Explore real-time performance on edge devices like Raspberry Pi.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/GiuseppeSoriano/Progetto_IndustrialApplications.git
    ```

2. **Navigate to the project directory:**
    ```bash
    cd Progetto_IndustrialApplications
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

## Palette

MoodPilot’s design draws on the following color palette for its visuals:
![Palette](Palette.png)
Palette created using [coolors.co](https://coolors.co/palette/f9dbbd-fca17d-da627d-9a348e-0d0628).

## References

For more details on the models and methodologies, see the full academic documentation available in `Prototype/Documentation`.
