import cv2
import os
from ultralytics import YOLO
from pathlib import Path
import re
import time
import tkinter
import PIL



class Detector:
    def __init__(self,MODEL_PATH, SOURCE_PATH= None, width = 1024, height = 720) -> None:
        self.SOURCE_PATH = SOURCE_PATH
        self.MODEL_PATH = MODEL_PATH
        self.width = width
        self.height = height
        
        self.cap = cv2.VideoCapture(self.SOURCE_PATH) if SOURCE_PATH else None
        if self.cap:
            self.cap.set(3, width)
            self.cap.set(4, height)
        self.model = YOLO(self.MODEL_PATH)

    
    def __del__(self):
        if self.cap:
            if self.cap.isOpened():
                self.cap.release()

    def change_stream(self, SOURCE_PATH):
        self.SOURCE_PATH = SOURCE_PATH
        try:
            self.cap.release()
        except Exception as e:
            print(e)
            pass
        self.cap = cv2.VideoCapture(self.SOURCE_PATH)
        self.cap.set(3, self.width)
        self.cap.set(4, self.height)
        
    def get_frame_size(self):
        return self.width, self.height

    def get_frame(self):
        if self.cap:
            if self.cap.isOpened():
                ret, frame = self.cap.read()
                if ret:
                    frame = cv2.resize(frame, (self.width, self.height), interpolation= cv2.INTER_LINEAR)
                    return ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return False, None
    
    def predict(self):
        if not self.cap:
            return False, None
        if self.cap.isOpened():
            ret, frame = self.cap.read()         
            if not ret:
                return ret, None
            frame = cv2.resize(frame, (self.width, self.height), interpolation= cv2.INTER_LINEAR)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
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