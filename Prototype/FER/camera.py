from picamera2 import Picamera2
import cv2

def camera_preview():
    # Initialize the camera
    picam2 = Picamera2()
    picam2.configure(picam2.create_still_configuration())

    # Start the camera preview
    picam2.start()

    while True:
        # Capture a frame from the camera
        frame = picam2.capture_array()

        # Resize the frame using OpenCV (to 640x480, for example)
        frame_resized = cv2.resize(frame, (640, 480))

        # Display the resized frame using OpenCV
        cv2.imshow("Camera Preview", frame_resized)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Closing camera preview.")
            break

    # Release resources
    picam2.stop()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    camera_preview()
