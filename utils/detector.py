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
        if not self.cap:
            return False, None
        if self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.resize(frame, (self.width, self.height), interpolation= cv2.INTER_LINEAR)
                return ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return ret, None
    
    def predict(self):
        if not self.cap:
            return False, None
        if self.cap.isOpened():
            ret, frame = self.cap.read()         
            if not ret:
                return ret, None
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.model.predict(frame, iou = 0.5, verbose = False)
            frame = results[0].plot(line_width = 1, font_size = 0.1)
            frame = cv2.resize(frame, (self.width, self.height), interpolation= cv2.INTER_LINEAR)
            return ret, frame
        
        return False, None 