import tkinter
import time
from utils.detector import Detector
import cv2
import PIL
from PIL import ImageTk, Image


class App:
    def __init__(self, window, detector, window_title = "Hello World", delay = 3) -> None:
        self.window = window
        self.window.title(window_title)
        self.detector = detector
        self.width, self.height = detector.get_frame_size()
        self.canvas = tkinter.Canvas(window, width= self.width, height= self.height)
        self.canvas.pack()

        self.button_snap = tkinter.Button(window, text = "Snapshot", width = 50, command=self.snapshot)
        self.delay = delay

        self.update()
        self.window.mainloop()

    def update(self):
        ret, frame = self.detector.predict()
        if ret:
            self.photo = ImageTk.PhotoImage(image =  Image.fromarray(frame))
            self.canvas.create_image(0,0,image= self.photo, anchor =tkinter.NW)
        self.window.after(self.delay, self.update)

    def snapshot(self):
        ret, frame = self.detector.get_frame()
        if ret:
            print("Saave karo photo chutiye")