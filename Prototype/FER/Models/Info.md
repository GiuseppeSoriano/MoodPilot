#### **Overview**

This project integrates multiple Facial Emotion Recognition (FER) models, such as **HSEmotionONNX**, **ViT (Vision Transformer)**, **DeepFace**, **EmoNet**, **RMN (Residual Masking Network)**, and logs the recognized emotions and their confidence scores during real-time video processing. The `process_video` function is designed to handle video inputs, detect faces, predict emotions, and log the results.

### **Key Features**

- **Real-Time Emotion Detection**: The models are capable of recognizing emotions (and in some cases, other related attributes like valence and arousal) from faces in real-time via a webcam or video feed.
  
- **Logging**: All predictions, including timestamps, detected emotions, and confidence scores, are logged to a text file. The log filenames are unique to avoid overwriting previous logs. The log file will be saved in the `logs/` directory.

- **Preview Control**: You can control whether the video preview with bounding boxes and emotion labels is shown. This allows optimization during deployment where preview is unnecessary.

- **Customizable Inputs**: The function accepts both video file inputs and live camera feeds. If the input is `"camera"`, the function will access the webcam for live processing.

- **Smoothing**: For more stable emotion predictions, recent predictions are smoothed. A buffer of previous results is maintained, and the most frequent emotion and average confidence are used for the final output. Note that this smoothing process is not applied to EmoNet.

### **Functionality of `process_video`**

The `process_video` function processes a video (either a file or webcam feed) for real-time emotion recognition using any of the FER models and logs the results. It has the following parameters:

#### **`process_video(video_file, show_preview=True)`**

**Parameters:**

- `video_file`: 
  - Type: `str`
  - **Description**: Path to a video file or `"camera"` to use the webcam for live emotion detection.
  - **Example**: `"video.mp4"` or `"camera"`.

- `show_preview`: 
  - Type: `bool`
  - **Description**: Flag to control whether the video preview with emotion bounding boxes and labels is displayed.
  - **Example**: `True` (show preview), `False` (no preview).
  - **Default**: `True`.

**Behavior:**
- If `video_file == "camera"`, the webcam will be used as the video source. Press `"q"` or close the window to stop.
- If `video_file` is a file path (e.g., `"video.mp4"`), it will process the video frame by frame.
- The processed frame is displayed in a window if `show_preview=True` with bounding boxes drawn around detected faces and emotion labels.
- If `show_preview=False`, the video feed will not be displayed, improving performance when preview is not needed.
- Predictions are smoothed by using the most frequent emotion detected in recent frames and averaging the confidence score.
- Each frame's emotion and confidence, along with the timestamp, are logged to a unique log file in the `logs/` directory.

**Logging Behavior:**
- The log file name is automatically generated to avoid overwriting by checking the existing files in the `logs/` folder. Log file names follow the format `emotion_log_<counter>.txt` (e.g., `emotion_log_0.txt`).
- The log contains in general (specific models may have additional information):
  - `Timestamp`: The timestamp of the current frame.
  - `Emotion`: The predicted emotion (e.g., "Happy", "Sad", "Anger").
  - `Confidence`: The confidence score of the predicted emotion.

**FPS Calculation:**
- The function calculates the frames per second (FPS) during the video processing and logs it at the end.

### **Supported Models and their Specific Behavior**

Each emotion recognition model has its own detection capabilities and works within the same framework, but there are some differences in how they handle the detection process and what they log.

#### **1. HSEmotionONNX**
- **Model Type**: ONNX-based deep learning model.
- **Outputs**: Predicted emotion (from 8 classes), confidence score.
- **Log Entry**: Logs the emotion and confidence score.

#### **2. ViT (Vision Transformer)**
- **Model Type**: Vision Transformer model for emotion classification.
- **Outputs**: Predicted emotion (from a set of 7 classes), confidence score.
- **Log Entry**: Logs the emotion and confidence score.

#### **3. DeepFace**
- **Model Type**: Deep learning model from the `DeepFace` library.
- **Outputs**: Predicted emotion (from 7 classes), confidence score.
- **Log Entry**: Logs the dominant emotion and confidence score.

#### **4. EmoNet**
- **Model Type**: Deep learning model for emotion, valence, and arousal detection.
- **Outputs**: Predicted emotion, confidence score, valence, and arousal scores.
- **Log Entry**: Logs the predicted emotion, confidence, and optionally valence and arousal.

#### **5. RMN (Residual Masking Network)**
- **Model Type**: Residual Masking Network (RMN).
- **Outputs**: Predicted emotion, confidence score.
- **Log Entry**: Logs the predicted emotion and confidence score.


### **Error Handling**

- If a model encounters an error during prediction (e.g., no face detected or an invalid frame), the function gracefully handles it without crashing, logging the error message if needed.
  
- If the `video_file` path is invalid or the webcam cannot be accessed, an error message is displayed and the function terminates.


### **Examples of Usage**

1. **Processing a video file:**
   ```python
   process_video("video.mp4", show_preview=True)
   ```

2. **Processing a live webcam feed:**
   ```python
   process_video("camera", show_preview=False)
   ```

3. **Processing a video file with logging but without preview:**
   ```python
   process_video("video.mp4", show_preview=False)
   ```


### **Conclusion**

This setup allows for seamless real-time emotion detection using multiple models, logging the results for further analysis. The `process_video` function provides flexibility in terms of video input sources (webcam or file), preview control, and logs the detected emotions along with their confidence values for each frame processed.