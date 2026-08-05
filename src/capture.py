import cv2
from threading import Thread, Lock


class VideoCapture:

    def __init__(self, source):
        self.cap = cv2.VideoCapture(source)

        self.frame = None
        self.running = False
        self.thread = None

        self.lock = Lock()

    def get_fps(self):
        return self.cap.get(cv2.CAP_PROP_FPS)

    def start(self):
        self.running = True

        self.thread = Thread(
            target=self.update,
            daemon=True
        )

        self.thread.start()


    def update(self):

        while self.running:

            ret, frame = self.cap.read()

            if ret:

                with self.lock:
                    self.frame = frame


    def read(self):

        with self.lock:

            if self.frame is None:
                return None

            return self.frame.copy()


    def stop(self):

        self.running = False

        if self.thread:
            self.thread.join()

        self.cap.release()