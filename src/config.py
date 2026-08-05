from pathlib import Path

# Every path in project is built relative to ROOT
ROOT = Path(__file__).resolve().parent.parent

OUTPUT_VIDEO = ROOT / "output" / "annotated_video.mp4"

# Video source / could be a local live stream too
VIDEO_SOURCE = ROOT / "parking.mp4"

# The model
MODEL = "yolov8n.pt"

# How confident the model is in detections
CONFIDENCE = 0.45

# Skipping some frames for YOLO to be faster
# FRAME_SKIP = 3

# Showing window
# SHOW_WINDOW = True

# Saves the annotated video
SAVE_VIDEO = True

# Saves alert images when heavy traffic happens
SAVE_ALRET_IMAGES = True

# Saves json log
JSON_LOG = True

# Saves CSV log
CSV_LOG = True

# Thereshold config
# HEAVY_THRESHOLD = 12
# MODERATE_THRESHOLD = 6