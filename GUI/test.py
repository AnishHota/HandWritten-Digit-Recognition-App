#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

In this script, we use the grid
manager to create a more complicated
layout.

Author: Jan Bodnar
Last modified: July 2017
Website: www.zetcode.com
"""

from tkinter import Tk, Text, BOTH, W, N, E, S
from tkinter.ttk import Frame, Button, Label, Style
from random import randint

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

from PIL import Image, ImageTk
import pyscreenshot as ImageGrab


class Example(Frame):

    def __init__(self):
        super().__init__()
        self.toolsThickness = 20
        self.rgb = "#%02x%02x%02x" % (255, 255, 255)
        self.cv = tk.Canvas(self)

        self.initUI()


    def initUI(self):

        self.master.title("Windows")
        self.pack(fill=BOTH, expand=True)
        self.myCanvas = tk.Canvas(self, width = 800,height = 500,bg="black")
        self.myCanvas.grid(columnspan = 30)
        self.columnconfigure(31, weight = 0)
        self.myCanvas.bind("<B1-Motion>", self.draw)
        self.myCanvas.bind("<Button-1>", self.setPreviousXY)
        self.Button1 = Button(self, text = "test").grid(column = 32, columnspan = 6)


    def setPreviousXY(self, event):
            print("now")
            self.previousX = event.x
            self.previousY = event.y

    def draw(self, event):
        #line 2
        self.myCanvas.create_oval(event.x - self.toolsThickness,
                                  event.y - self.toolsThickness,
                                  event.x + self.toolsThickness,
                                  event.y + self.toolsThickness,
                                  fill = self.rgb, outline =""
                                  )



def main():

    root = Tk()
    root.geometry("2000x2000")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
