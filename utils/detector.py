import cv2
import os
from ultralytics import YOLO
from pathlib import Path
import re
import time
import tkinter
import PIL



class Detector:
    def __init__(self,MODEL_PATH, SOURCE_PATH = 0, width = 800, height = 600) -> None:
        self.SOURCE_PATH = SOURCE_PATH
        self.MODEL_PATH = MODEL_PATH
        self.width = width
        self.height = height
        self.cap = cv2.VideoCapture(self.SOURCE_PATH)
        self.cap.set(3, width)
        self.cap.set(4, height)
        self.model = YOLO(self.MODEL_PATH)

    
    def __del__(self):
        if self.cap.isOpened():
            self.cap.release()

    def get_frame_size(self):
        return self.width, self.height

    def get_frame(self):
        if self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                return ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return ret, None
    
    def predict(self):
        ret, frame = self.get_frame()
        if not ret:
            return ret, None
        results = self.model(frame)
        annotated_frame = results[0].plot()
        return ret, annotated_frame

# """
# Paths
# """
# ROOT = os.getcwd();
# MODEL_PATH = os.path.join(ROOT, 'models', 'yolov8s_new.pt')
# #SOURCE_PATH = "samples\detection.mp4"
# FILE_NAME = "Result"
# SOURCE_PATH = "rtsp://rtsp:Rtsp1234@158.0.17.109:554/streaming/channels/1"


# """
# Variables

# """
# prev_time = 0
# curr_time = 0
# frame_width = 640
# frame_height = 480
# font = cv2.FONT_HERSHEY_SIMPLEX


# def detect(frame):
#     pass

# model = YOLO(MODEL_PATH)
# cap = cv2.VideoCapture(SOURCE_PATH)
# cap.set(3,frame_width)
# cap.set(4,frame_height)

# size = (frame_width, frame_height)
# writer = cv2.VideoWriter('results\\filename.mkv', 
#                          cv2.VideoWriter_fourcc(*'MJPG'),
#                          10, size)
# # fps = int(cap.get(5))

# while cap.isOpened():
#     curr_time = time.time()
#     ret, im = cap.read()
#     if not ret:
#         print("Reading Complete or Can't read from source")
#         break
#     results = model(im)
#     annotated_frame = results[0].plot()
#     writer.write(annotated_frame)
#     fps = int(1/(curr_time - prev_time))
#     prev_time = curr_time
#     cv2.putText(annotated_frame, str(fps), (20, 20), font, 1, (255, 0, 0), 2, cv2.LINE_AA)
#     cv2.imshow("Output", annotated_frame)
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break

# cap.release()
# writer.release()
# cv2.destroyAllWindows()