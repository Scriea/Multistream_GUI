import tkinter
import time
from utils.detector import Detector
from utils.general import get_stream_list
import cv2
import PIL
from PIL import ImageTk, Image


class App:
    def __init__(self, window, detector, window_title = "Hello World", delay = 1, source = None) -> None:
        if source:
            self.stream_list = get_stream_list(source)
        else:
            self.stream_list = get_stream_list()
        self.window = window
        self.window.title(window_title)
        self.detector = detector
        self.width, self.height = detector.get_frame_size()
        self.canvas = tkinter.Canvas(window, width= self.width, height= self.height)
        self.canvas.pack()
        self.menu = tkinter.StringVar()
        self.menu.set(self.stream_list[0])
        self.entry = tkinter.Entry(window, width = 50, borderwidth= 5)
        self.entry.pack()
        # self.button_snap = tkinter.Button(window, text = "Snapshot", width = 50, command=self.snapshot, pady= 50)
        self.delay = delay
        self.drop = tkinter.OptionMenu(self.window, self.menu, *self.stream_list, command=self.onMenuClick)
        self.drop.pack()
        self.update()
        self.window.mainloop()
        
    def onMenuClick(self, args):

        self.menu.set(args)
        self.detector.change_stream(str(args))

    def update(self):
        ret, frame = self.detector.get_frame()
        if ret:
            self.photo = ImageTk.PhotoImage(image =  Image.fromarray(frame))
            self.canvas.create_image(0,0,image= self.photo, anchor =tkinter.NW)
        self.window.after(self.delay, self.update)

