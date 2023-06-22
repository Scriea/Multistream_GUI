# import pygame
# from pygame.locals import *
import cv2
import numpy as np
import sys
import tkinter
import cv2
import os
from ultralytics import YOLO
from pathlib import Path
import time
from utils.app import App
from utils.detector import Detector


"""
Paths
"""
ROOT = os.getcwd();
MODEL_PATH = os.path.join(ROOT, 'models', 'yolov8n_ppe.pt')
#SOURCE_PATH = "samples\detection.mp4"
FILE_NAME = "Result"
SOURCE_PATH = "rtsp://rtsp:Rtsp1234@158.0.17.109:554/streaming/channels/1"
SOURCE_PATH = 0


"""
Variables

"""
prev_time = 0
curr_time = 0
frame_width = 1024
frame_height = 720
font = cv2.FONT_HERSHEY_SIMPLEX
size = (frame_width, frame_height)

"""
Detector Instance

"""
detector = Detector(MODEL_PATH, SOURCE_PATH)

"""
GUI

"""

App(tkinter.Tk(), detector, "New")
  













# model = YOLO(MODEL_PATH)
# camera = cv2.VideoCapture(SOURCE_PATH)
# camera.set(3,frame_width)
# camera.set(4,frame_height)
# writer = cv2.VideoWriter('results\\filename.mkv', 
#                          cv2.VideoWriter_fourcc(*'MJPG'),
#                          10, size)



# pygame.init()
# pygame.display.set_caption("Camera stream")
# screen = pygame.display.set_mode([1024,720])

# while True:
#     if not camera.isOpened():
#         frame = np.zeros(size, dtype=float)
#     else:
#         ret, frame = camera.read()
#         results = model(frame)
#         frame = results[0].plot()
#         if not ret:
#             print("Exitting Feed!!")
#             break
#     screen.fill([0,0,0])
    
#     frame = cv2.flip(frame, 1)
#     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     frame = np.rot90(frame)
#     frame = pygame.surfarray.make_surface(frame)
#     screen.blit(frame, (0,0))
#     pygame.display.update()

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit(0)    

# pygame.quit()
# cv2.destroyAllWindows()