import cv2
import torch
import os
import time
from pathlib import Path
from skimage import io
from face_alignment.detection.sfd.sfd_detector import SFDDetector
from app.fer.emonet.models import EmoNet
import numpy as np
from torch import nn

# Parameters
n_expression = 8  # Number of emotion classes
device = "cuda:0" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"
image_size = 256
emotion_classes = {
    0: "Neutral",
    1: "Happy",
    2: "Sad",
    3: "Surprise",
    4: "Fear",
    5: "Disgust",
    6: "Anger",
    7: "Contempt",
}

# Create logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

def get_log_filename(base_name="logs/emotion_log"):
    """Generate a unique log filename by appending a counter if files already exist."""
    counter = 0
    while True:
        filename = f"{base_name}_{counter}.txt"
        if not os.path.exists(filename):
            return filename
        counter += 1

def load_emonet(n_expression, device):
    """Load the EmoNet model."""
    state_dict_path = Path("app/fer/pretrained/emonet_8.pth")  # Adjust path if needed
    print(f"Loading EmoNet model from {state_dict_path}")
    state_dict = torch.load(state_dict_path, map_location=device)
    state_dict = {k.replace("module.", ""): v for k, v in state_dict.items()}

    net = EmoNet(n_expression=n_expression).to(device)
    net.load_state_dict(state_dict, strict=False)
    net.eval()
    return net

# Load Face Detector and EmoNet
print("Loading face detector...")
sfd_detector = SFDDetector(device)
print("Loading EmoNet...")
emonet = load_emonet(n_expression, device)

def fill_missing_emotions(emotions):
    # Creare una nuova lista per contenere gli oggetti con gli elementi aggiunti
    filled_emotions = []

    # Iterare sulla lista ordinata per timestamp
    for i in range(len(emotions) - 1):
        # Aggiungere l'elemento corrente alla lista riempita
        filled_emotions.append(emotions[i])

        # Calcolare la differenza tra il timestamp corrente e quello successivo
        current_timestamp = emotions[i]["timestamp"]
        next_timestamp = emotions[i + 1]["timestamp"]

        # Inserire elementi mancanti ogni 200 ms
        while next_timestamp - current_timestamp > 0.2:
            current_timestamp += 0.2
            filled_emotions.append({
                "timestamp": round(current_timestamp, 2),
                "warning": "no face detected"
            })

    # Aggiungere l'ultimo elemento della lista originale
    filled_emotions.append(emotions[-1])

    return filled_emotions

def process_video(video_file, show_preview=True):
    """Process video for emotion detection, valence, and arousal logging."""
    video_source = 0 if video_file == "camera" else video_file

    cap = cv2.VideoCapture(video_source)
    if not cap.isOpened():
        print(f"Error: Could not open video source '{video_source}'.")
        return

    # Initialize log file
    log_filename = get_log_filename()
    log_file = open(log_filename, "w")
    log_file.write("Timestamp,Emotion,Confidence,Valence,Arousal\n")

    # Variables for FPS calculation
    frame_count = 0
    start_time = time.time()
    
    emotions = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect faces
        with torch.no_grad():
            detected_faces = sfd_detector.detect_from_image(rgb_frame)

        for bbox in detected_faces:
            x1, y1, x2, y2 = map(int, bbox[:4])  # Extract bounding box
            if x2 - x1 <= 0 or y2 - y1 <= 0:
                continue
            face_crop = rgb_frame[y1:y2, x1:x2]
            if face_crop.size == 0:
                continue

            # Preprocess the face
            resized_face = cv2.resize(face_crop, (image_size, image_size))
            face_tensor = torch.Tensor(resized_face).permute(2, 0, 1).unsqueeze(0).to(device) / 255.0

            with torch.no_grad():
                prediction = emonet(face_tensor)

            # Get valence, arousal, and predicted emotion
            valence = prediction["valence"].clamp(-1.0, 1.0).cpu().item()
            arousal = prediction["arousal"].clamp(-1.0, 1.0).cpu().item()
            probs = nn.functional.softmax(prediction["expression"], dim=1).cpu().numpy()
            predicted_class = np.argmax(probs)
            predicted_emotion = emotion_classes[predicted_class]
            confidence = probs[0, predicted_class]

            if video_file == "camera":
                # Get the current timestamp
                timestamp = time.time()
            else:
                timestamp = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000.0
            
            # Log results
            log_file.write(f"{timestamp:.2f},{predicted_emotion},{confidence:.2f},{valence:.3f},{arousal:.3f}\n")
            
            emotions.append({
                "timestamp": float(timestamp),
                "emotion": predicted_emotion,
                "confidence": float(confidence),
                "valence": float(valence),
                "arousal": float(arousal)
            })

            # Draw bounding box and emotion label
            if show_preview:
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(
                    frame, f"{predicted_emotion} ({valence:.2f}, {arousal:.2f})",
                    (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2
                )

        # Display the video
        if show_preview:
            cv2.imshow("EmoNet Emotion Recognition", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
            if cv2.getWindowProperty("EmoNet Emotion Recognition", cv2.WND_PROP_VISIBLE) < 1:
                break

        frame_count += 1

    # Calculate FPS
    end_time = time.time()
    total_time = end_time - start_time
    fps = frame_count / total_time
    print(f"Processed {frame_count} frames in {total_time:.2f} seconds. FPS: {fps:.2f}")
    log_file.write(f"\nProcessed {frame_count} frames in {total_time:.2f} seconds.\n")
    log_file.write(f"FPS: {fps:.2f}\n")
    log_file.close()

    cap.release()
    if show_preview:
        cv2.destroyAllWindows()
        cv2.waitKey(1)
        
    return fill_missing_emotions(emotions)