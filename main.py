import pygame
from pygame.locals import *
import cv2
import numpy as np
import sys

import cv2
import os
from ultralytics import YOLO
from pathlib import Path
import time

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
frame_width = 640
frame_height = 480
font = cv2.FONT_HERSHEY_SIMPLEX
size = (frame_width, frame_height)


model = YOLO(MODEL_PATH)
camera = cv2.VideoCapture(SOURCE_PATH)
camera.set(3,frame_width)
camera.set(4,frame_height)

pygame.init()
pygame.display.set_caption("OpenCV camera stream on Pygame")
screen = pygame.display.set_mode([640,480])
   

writer = cv2.VideoWriter('results\\filename.mkv', 
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10, size)

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



while True:
    ret, frame = camera.read()
    if not ret:
        print("Exitting Feed!!")
        break
    screen.fill([0,0,0])
    results = model(frame)
    frame = results[0].plot()
    frame = cv2.flip(frame, 1)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = np.rot90(frame)
    frame = pygame.surfarray.make_surface(frame)
    screen.blit(frame, (0,0))
    pygame.display.update()
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            sys.exit(0)

pygame.quit()
cv2.destroyAllWindows()