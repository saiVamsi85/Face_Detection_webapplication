import cv2

# Load the Haar Cascade Classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open the default camera (usually the built-in webcam, camera index 0)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open the camera.")
    exit()

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read a frame.")
        break

    # Convert the frame to grayscale (required for face detection)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    # Define the blue color in RGB
    blue_color_rgb = (255, 0, 0)  # OpenCV uses BGR by default

    # Draw rectangles around the detected faces with RGB color and add "Face" text
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), blue_color_rgb, 2)  # Blue rectangle
        cv2.putText(frame, 'Face', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, blue_color_rgb, 2)

    # Display the frame with detected faces
    cv2.imshow("Face Detection", frame)

    # Exit the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
