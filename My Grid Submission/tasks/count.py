import cv2
from yolov5 import YOLOv5

# Load YOLOv5 model
yolo = YOLOv5("yolov5s6.pt")  # Adjust the path as needed

def count_objects(image):
    """Count objects in an image using YOLOv5."""
    results = yolo.predict(image, size=640)
    detections = results.xyxy[0]
    return len(detections)
