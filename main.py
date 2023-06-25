import os
import cv2
import sys
import numpy as np
from tkinter import *
import customtkinter
from pathlib import Path
from ultralytics import YOLO
from utils.app import App
from utils.detector import Detector
from utils.general import get_stream_list

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')


"""
Paths

"""
ROOT = Path(__file__).resolve().parents[0]
STREAM_SOURCE = os.path.join(ROOT,'stream.txt')
ROOT = os.getcwd();
MODEL_PATH = os.path.join(ROOT, 'models', 'yolov8n_e100_newdataset.pt')

FILE_NAME = "Result"

STREAM_LIST = get_stream_list(source= STREAM_SOURCE)
try:
    SOURCE_PATH = STREAM_LIST[0]
except Exception as e:
    print(e)
    print("Please enter a video path/url in stream.txt")
    exit()


"""
Variables

"""
frame_width = 1200
frame_height = 800




"""
Detector Instance

An object created for initializing video feed.
Contains detection code as well.

"""
detector = Detector(MODEL_PATH, width= frame_width, height= frame_height)

"""
GUI

"""

app = App(detector, "PPE Detector", source= STREAM_SOURCE)
app.update()
app.mainloop()
  

