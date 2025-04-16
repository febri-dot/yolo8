from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # You can use yolov8n, yolov8s, etc.
model.train(data="datasets/data.yaml", epochs=50, imgsz=640)
# model.train(data="datasets/data.yaml", epochs=50, imgsz=640)
