from ultralytics import YOLO
from src.config import CONFIDENCE


class Detector:

    def __init__(self, model_path):
        self.model = YOLO(model_path)


    def detect(self, frame):

        results = self.model(
            frame,
            conf=CONFIDENCE,
            imgsz=320,      
            verbose=False
        )

        return results[0]