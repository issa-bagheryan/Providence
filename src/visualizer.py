import cv2


class Visualizer:
    def __init__(self):
        pass


    def draw(self, frame, result):

        annotated = frame.copy()

        for box in result.boxes:

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            class_id = int(box.cls[0])
            name = result.names[class_id]

            confidence = float(box.conf[0])

            cv2.rectangle(
                annotated,
                (x1,y1),
                (x2,y2),
                (0,255,0),
                2
            )

            label = f"{name} {confidence:.2f}"

            cv2.putText(
                annotated,
                label,
                (x1,y1-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0,255,0),
                2
            )

        return annotated