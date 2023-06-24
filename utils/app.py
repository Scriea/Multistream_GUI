from tkinter import *
import customtkinter
import time
from utils.detector import Detector
from utils.general import get_stream_list
import cv2
import PIL
from PIL import ImageTk, Image


class App:
    def __init__(self, window, detector, window_title = "Hello World", delay = 1, source = None) -> None:
        self.detector = detector
        self.window = window
        self.window.title(window_title)

        self.width, self.height = detector.get_frame_size()
        ## Video Canvas

        self.canvas = customtkinter.CTkCanvas(window, width= self.width, height= self.height)
        self.canvas.grid(row= 0, column=0, sticky="W")

        ## Drop-Down Menu
        
        if source:
            self.stream_list = get_stream_list(source)
        else:
            self.stream_list = get_stream_list()
        self.menu = customtkinter.StringVar(value= self.stream_list[0])
        self.drop = customtkinter.CTkOptionMenu(master= self.window, values= self.stream_list, variable= self.menu, command=self.onMenuClick)
        self.drop.grid(row=0, column= 1)
        
        """
        ## Entry Widget and Button
        self.entry_label = customtkinter.CTkLabel(self.window, text="Enter Stream URL or Path to File")
        self.entry_label.grid(row=0, column= 1, sticky="N", pady= 5)
        self.entry = customtkinter.CTkEntry(window, width = 50, border_width= 5)
        self.entry.grid(column=1, row= 1, padx= 10, pady= 10)
        #self.entry.pack()
        self.button_entry = customtkinter.CTkButton(window, text = "Play", width = 50, command=self.play)
        self.button_entry.grid(row=0, column=1)
        """        

        self.delay = delay
        self.update()
        self.window.mainloop()

        
    def onMenuClick(self, args):

        self.menu.set(args)
        self.detector.change_stream(str(args))

    def update(self):
        ret, frame = self.detector.get_frame()
        if ret:
            #self.photo = customtkinter.CTkImage(dark_image= Image.fromarray(frame))
            self.photo = ImageTk.PhotoImage(image =  Image.fromarray(frame))
            self.canvas.create_image(0,0,image= self.photo, anchor = customtkinter.NW)
        self.window.after(self.delay, self.update)
    def play(self, args):
        pass

