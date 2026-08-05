from src.capture import VideoCapture
from src.detector import Detector
from src.analytics import Analytics
from src.config import VIDEO_SOURCE, MODEL, SAVE_VIDEO, OUTPUT_VIDEO
from rich.console import Console
from rich.live import Live
from src.dashboard import Dashboard
from src.visualizer import Visualizer
import cv2
from src.logger import EventLogger


logger = EventLogger(
    "logs/events.jsonl"
)


visualizer = Visualizer()

console = Console()

dashboard = Dashboard()

camera = VideoCapture(VIDEO_SOURCE) # Make a cam

detector = Detector(MODEL) # Create a detector

analytics = Analytics() # Create an anal engine

camera.start() # Sets self.running to True amd then creats a thread and starts the read and then another thread keeps updating

writer = None # for video saving cap
fps = camera.get_fps()

with Live(
    dashboard.build({
        "cars": 0,
        "people": 0,
        "traffic": "Initializing",
        "alert": False
    }),
    refresh_per_second=2
) as live:

    while True:

        frame = camera.read()

        if frame is None:
            continue

        result = detector.detect(frame)

        annotated = visualizer.draw(frame, result)


        # Save annotated video
        if SAVE_VIDEO:

            if writer is None:

                height, width, _ = annotated.shape

                writer = cv2.VideoWriter(
                str(OUTPUT_VIDEO),
                cv2.VideoWriter_fourcc(*"mp4v"),
                fps,
                (width, height)
            )
                

            writer.write(annotated)


        cv2.imshow(
            "CCTV Analytics",
            annotated
        )


        stats = analytics.analyze(result)
        logger.log(stats)
        
        live.update(
            dashboard.build(stats)
        )


        if cv2.waitKey(1) & 0xFF == ord("q"):
            break




