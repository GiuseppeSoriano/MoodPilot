import cv2
import numpy as np
from collections import deque
from app.fer.hsemotion_onnx.facial_emotions import HSEmotionRecognizer
import time
import os

# Initialize Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize the emotion recognizer
model_name = 'enet_b0_8_best_vgaf'
emotion_recognizer = HSEmotionRecognizer(model_name=model_name)

# Define a buffer for recent emotion scores
maxlen = 15
recent_scores = deque(maxlen=maxlen)

def get_log_filename(base_name="logs/emotion_log"):
    """Generate a unique log filename by appending a counter if files already exist."""
    os.makedirs("logs", exist_ok=True)  # Ensure the logs folder exists
    counter = 0
    while True:
        filename = f"{base_name}_{counter}.txt"
        if not os.path.exists(filename):
            return filename
        counter += 1

def process_video(video_file, show_preview=True):
    # Determine video source
    video_source = 0 if video_file == "camera" else video_file

    # Open video capture
    cap = cv2.VideoCapture(video_source)
    if not cap.isOpened():
        print(f"Error: Could not open video source '{video_source}'.")
        return

    # Generate a unique log filename
    log_filename = get_log_filename()
    log_file = open(log_filename, "w")
    log_file.write("Timestamp,Emotion,Score\n")

    # Variables for FPS calculation
    frame_count = 0
    start_time = time.time()
    
    emotions = []

    while True:
        success, frame = cap.read()
        if not success:
            break

        # Convert to grayscale for Haar Cascade
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            # Crop and preprocess the face
            face_img = frame[y:y+h, x:x+w]
            if np.prod(face_img.shape) == 0:
                continue

            # Predict emotions
            try:
                emotion, scores = emotion_recognizer.predict_emotions(face_img, logits=True)
                recent_scores.append(scores)

                # Compute the average score across recent frames
                avg_scores = np.mean(recent_scores, axis=0)
                emotion_idx = np.argmax(avg_scores)
                emotion_label = emotion_recognizer.idx_to_class[emotion_idx]

                # Get the current timestamp
                timestamp = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000.0  # Convert to seconds

                # Log emotion and score
                log_file.write(f"{timestamp:.2f},{emotion_label},{avg_scores.tolist()}\n")
                
                emotions.append({
                    "timestamp": timestamp,
                    "emotion": emotion_label
                })

                # Display the detected emotion on the video (if preview is enabled)
                if show_preview:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                    cv2.putText(frame, emotion_label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            except Exception as e:
                print(f"Error processing face: {e}")

        # Increment frame count
        frame_count += 1

        # Show the video frame with emotion labels (if preview is enabled)
        if show_preview:
            cv2.imshow('HSEmotionONNX Emotion Detection', frame)

            # Break on 'q' key press or window close
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            if cv2.getWindowProperty('HSEmotionONNX Emotion Detection', cv2.WND_PROP_VISIBLE) < 1:
                break

    # Calculate FPS
    end_time = time.time()
    total_time = end_time - start_time
    fps = frame_count / total_time
    print(f"Processed {frame_count} frames in {total_time:.2f} seconds. FPS: {fps:.2f}")

    # Log the FPS
    log_file.write(f"\nProcessed {frame_count} frames in {total_time:.2f} seconds.\n")
    log_file.write(f"FPS: {fps:.2f}\n")
    log_file.close()

    # Release resources
    cap.release()
    if show_preview:
        cv2.destroyAllWindows()
        
    return emotions

# if __name__ == '__main__':
#     # Replace 'input_video.mp4' with the path to your video file or use "camera" for live feed
#     process_video('../ExampleVideos/surry.mp4', show_preview=True)
