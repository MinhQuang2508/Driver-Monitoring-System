import cv2
import threading
from ultralytics import YOLO

# Load pre-trained YOLO face detection model
model_yolo = YOLO(r"best_face_detection.pt")

# Open the default camera (camera index 0)
cap = cv2.VideoCapture(0)

# Set the desired dimensions
resize_width = 640
resize_height = 480

# Flag to signal when to stop the threads
stop_threads = False

def process_frame():
    global stop_threads
    while not stop_threads:
        ret, frame = cap.read()

        if not ret:
            print("Failed to capture frame. Exiting.")
            break

        try:
            # Resize the frame to the desired dimensions
            frame = cv2.resize(frame, (resize_width, resize_height))

            # Make predictions using YOLO face detection model
            results = model_yolo.predict(source=frame, show=False, save=False, conf=0.5)

            # Display the results
            for result in results[0]:
                # Extract bounding box coordinates for the face
                x, y, w, h = result['bbox']

                # Draw bounding box around the face
                cv2.rectangle(frame, (int(x), int(y)), (int(x + w), int(y + h)), (0, 255, 0), 2)

            # Show the frame
            cv2.imshow('Camera Feed with YOLO', frame)

        except Exception as e:
            print(f"An error occurred: {str(e)}")

        if cv2.waitKey(1) & 0xFF == ord('q'):
            stop_threads = True
            break

# Start the processing thread
thread = threading.Thread(target=process_frame)
thread.start()

# Main loop to show resized camera feed
while not stop_threads:
    ret, frame = cap.read()

    # Resize the frame to the desired dimensions
    frame = cv2.resize(frame, (resize_width, resize_height))

    cv2.imshow('Resized Camera Feed', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        stop_threads = True
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
