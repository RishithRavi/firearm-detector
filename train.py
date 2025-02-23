import torch
from ultralytics import YOLO


# Load YOLOv8 Pose model
model = YOLO("yolov8n.pt")  # Using nano model for efficiency

# Train the model
model.train(
    data="./data.yaml",
    epochs=27,
    imgsz=640,
    batch=16,
    device=0 if torch.cuda.is_available() else "cpu",
    name="SciFairFightDetection",
    workers=4,
)

# Export trained model
model.export(format="onnx")  # Convert model to ONNX for deployment
