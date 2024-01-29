import cv2
import numpy as np
import joblib

# Load the trained SVM model
clf = joblib.load('svm_model125.plk')

def detect_eye_state(image_path):
    # Read the input image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Check if the image is empty
    if img is None:
        print("Error: Unable to read the image.")
        return

    # Resize the image
    img = cv2.resize(img, (80, 80))

    # Flatten and normalize the image
    img_1d = img.flatten() / 255

    # Make a prediction using the SVM model
    prediction = clf.predict([img_1d])

    # Display the result
    if prediction[0] == 1:
        print("Normal")
    else:
        print("Sleep")

    # Show the image without text
    cv2.imshow("Eye State Detection", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
image_path = r"C:\Users\CHE MINH QUANG\Downloads\frame_3537.jpg"
detect_eye_state(image_path)
