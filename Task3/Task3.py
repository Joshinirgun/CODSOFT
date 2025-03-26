import cv2
import numpy as np
import os

# Set absolute paths for the DNN model files
prototxt_path = r"N:\Codsoft\Tasks\Task3\deploy.prototxt"
model_path = r"N:\Codsoft\Tasks\Task3\res10_300x300_ssd_iter_140000.caffemodel"

# Check if model files exist
if not os.path.exists(prototxt_path) or not os.path.exists(model_path):
    print("Error: One or both DNN model files are missing!")
    print(f"Check these paths:\n  {prototxt_path}\n  {model_path}")
    exit()

# Load DNN model
net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # DNN Face Detection
    h, w = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), (104.0, 177.0, 123.0), swapRB=False, crop=False)
    net.setInput(blob)
    detections = net.forward()

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
            label = f"DNN: {confidence*100:.2f}%"
            cv2.putText(frame, label, (startX, startY - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the output
    cv2.imshow("Real-Time Face Detection (DNN)", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
