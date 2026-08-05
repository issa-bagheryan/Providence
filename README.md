# 👁 Providence: CCTV Analytics
A real-time computer vision project that analyzes CCTV footage using YOLOv8.

<img width="1920" height="1080" alt="Screenshot (12)" src="https://github.com/user-attachments/assets/7ea3f078-9ab7-47f5-b4bf-7e105b5cfb64" />

This project detects vehicles and people from a video source, estimates traffic conditions, creates annotated footage, and displays live analytics through a terminal dashboard.

The main goal of this project was learning how modern computer vision systems are structured — from video capture, model inference, and analytics logic to visualization and logging.

This is a **learning project**, built while exploring AI engineering, computer vision pipelines, and real-time inference systems.

AI tools were used as development assistance for debugging, explanations, and improving implementation decisions. The architecture, experiments, testing, and final integration were done as part of the learning process.

---

## 🎯 What This Project Does

<img width="435" height="340" alt="image" src="https://github.com/user-attachments/assets/c2188b89-41f8-4ea7-9708-4f65850c47b3" />


The system can:

- Read video from a file or camera source
- Capture frames using a threaded video pipeline
- Run object detection with YOLOv8
- Detect vehicles and pedestrians
- Analyze traffic density
- Display live statistics
- Generate annotated videos
- Log important events

---

## 🧠 How It Works

The pipeline is structured like a simple real-time AI system:

```mermaid
flowchart TD

A[Camera / Video Source]
--> B[Threaded Frame Capture]

B --> C[YOLOv8 Object Detection]

C --> D[Analytics Engine]

D --> E[Traffic Classification]

D --> F[Live Dashboard]

D --> G[Event Logger]

C --> H[Annotated Video Output]
````

The flow:

1. A video source provides frames.
2. Frames are captured in a separate thread to keep the pipeline responsive.
3. YOLOv8 analyzes each frame and returns detected objects.
4. The analytics layer converts detections into useful information.
5. Results are displayed, saved, and logged.
---

## 🛠️ Tech Stack

* Python
* OpenCV
* Ultralytics YOLOv8
* Rich (terminal dashboard)
* NumPy

---

## 📚 What I Learned

Building this project helped me understand:

* How real-time computer vision pipelines are structured
* How video frames are processed
* How object detection models are integrated into applications
* The difference between model output and application-level analytics
* Threading for handling live data streams
* Separating code into reusable components

---

## 🔮 Future Improvements

Possible improvements:

* Object tracking with ByteTrack
* RTSP camera support
* Web dashboard
* Database storage
* Docker deployment
* GPU optimization
* Edge device deployment

---

## 📌 Note

This project was created as part of my journey learning AI engineering and computer vision.

It is not intended as a finished or bug-free product, but as a practical exploration of how AI-powered vision applications are built.
