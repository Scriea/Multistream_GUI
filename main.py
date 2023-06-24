# import pygame
# from pygame.locals import *
import cv2
import numpy as np
import sys
from tkinter import *
import customtkinter
import cv2
import os
from ultralytics import YOLO
from pathlib import Path
import time
from utils.app import App
from utils.detector import Detector
from utils.general import get_stream_list


"""
Paths
"""
ROOT = os.getcwd();
MODEL_PATH = os.path.join(ROOT, 'models', 'yolov8n_ppe.pt')

FILE_NAME = "Result"
STREAM_LIST = get_stream_list()
SOURCE_PATH = STREAM_LIST[0]

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
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')

root = customtkinter.CTk()
#root  = tkinter.Tk()
root.geometry("1280x720")
# root.resizable()



## Call GUI
App(root, detector, "PPE Detector")
  

