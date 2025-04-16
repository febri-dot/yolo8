import cv2
from ultralytics import YOLO

model = YOLO("runs/detect/train2/weights/best.pt")  # Path to your trained model

cap = cv2.VideoCapture(0)  # Use 0 for webcam

while True:
   ret, frame = cap.read()
   if not ret:
      break

   results = model(frame)

   annotated_frame = results[0].plot()
   cv2.imshow("YOLOv8 Detection", annotated_frame)

   if cv2.waitKey(1) & 0xFF == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()
