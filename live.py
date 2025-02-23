from ultralytics import YOLO
import cv2
import math 

# Start webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# List of models to switch between
models = [
    "runs/detect/SciFairFightDetection3/weights/best.pt",
    "./best.pt"  # Add more models if needed
]

# Load the first model
model_index = 0
model = YOLO(models[model_index])

# Object classes (ensure correct list usage)
classNamesList = [
    ["Aggressive", "Non-Aggressive"],  # First model class names
    ["Firearm"]  # Second model class names (adjust as needed)
]

print(f"✅ Loaded model: {models[model_index]}")

while True:
    success, img = cap.read()
    if not success:
        print("❌ Failed to grab frame.")
        break

    # Run model detection
    results = model(img)

    # Process detections
    for r in results:
        boxes = r.boxes

        for box in boxes:
            if box.conf is not None and box.cls is not None:
                confidence = math.ceil((box.conf[0] * 100)) / 100
                print("Confidence --->", confidence)

                # Confidence threshold check
                if confidence < 0.5:
                    continue  # Skip low-confidence detections

                # Bounding box
                x1, y1, x2, y2 = map(int, box.xyxy[0])  

                # Draw bounding box
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

                # Class name
                cls = int(box.cls[0])
                classNames = classNamesList[model_index]  # Get class names for the current model
                
                if cls < len(classNames):  # Ensure index is valid
                    print("Class name -->", classNames[cls])

                    # Display class name on frame
                    org = (x1, y1 - 10)
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    fontScale = 1
                    color = (255, 0, 0)
                    thickness = 2
                    cv2.putText(img, classNames[cls], org, font, fontScale, color, thickness)

    # Display the output
    cv2.imshow("Fight Detector - Live", img)

    # Key controls
    key = cv2.waitKey(1) & 0xFF  

    if key == ord('q'):  # Quit
        print("🚪 Exiting...")
        break
    elif key == ord('m'):  # Switch model
        model_index = (model_index + 1) % len(models)  # Cycle through models
        model = YOLO(models[model_index])  # Reload the new model
        print(f"🔄 Switched to model: {models[model_index]}")

# Release resources
cap.release()
cv2.destroyAllWindows()
