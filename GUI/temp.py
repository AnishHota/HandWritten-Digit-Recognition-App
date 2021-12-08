#!/usr/bin/python3
# -*- coding: utf-8 -*-

from tkinter import Tk, Text, BOTH, W, N, E, S
from tkinter.ttk import Frame, Button, Label, Style
from random import randint

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

from PIL import Image, ImageTk
import pyscreenshot as ImageGrab


class Application(Frame):

    def __init__(self,master):
        super().__init__(master)
        self.toolsThickness = 20
        self.rgb = "#%02x%02x%02x" % (255, 255, 255)
        self.cv = tk.Canvas(self)

        self.initUI()


    def initUI(self):

        self.master.title("Digit Recognition")
        self.pack(fill=BOTH, expand=True)

        self.myCanvas = tk.Canvas(self, width = 800,height = 500,bg="black", borderwidth=5)
        self.myCanvas.grid(rowspan = 500,columnspan = 800)
        self.myCanvas.bind("<B1-Motion>", self.draw)
        self.myCanvas.bind("<Button-1>", self.setPreviousXY)

        self.Button1 = Button(self, text = "Predict", width=30, command=self.SAVE)
        self.Button1.grid(row = 200, column = 802,columnspan = 5)

        self.Button2 = Button(self, text = "Clear Screen", width=30, command=self.deleteAll)
        self.Button2.grid(row = 210, column = 802,columnspan = 5)

    def setThickness(self, event):
        print("Thickness is set to 20")
        self.toolsThickness = 20

    def setColor(self):
            val1 = int(255)
            val2 = int(255)
            val3 = int(255)
            self.rgb = "#%02x%02x%02x" % (val1, val2, val3)

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

    def SAVE(self):
        print('\n def _snapsaveCanvas(self):')
        canvas = self._canvas()  # Get Window Coordinates of Canvas
        self.grabcanvas = ImageGrab.grab(bbox=canvas).save("out_snapsave.jpg")
        print('Screenshot tkinter canvas and saved as "out_snapsave.jpg w/o displaying screenshot."')

    def _canvas(self):
        print('  def _canvas(self):')
        print('self.cv.winfo_rootx() = ', root.winfo_rootx())
        print('self.cv.winfo_rooty() = ', root.winfo_rooty())
        print('self.cv.winfo_x() =', root.winfo_x())
        print('self.cv.winfo_y() =', root.winfo_y())
        print('self.cv.winfo_width() = 1000')
        print('self.cv.winfo_height() =', root.winfo_height())
        x=root.winfo_rootx()+371
        y=root.winfo_rooty()+5
        x1=x+802
        y1=y+root.winfo_height()-12
        box=(x,y,x1,y1)
        print('box = ', box)
        return box

    def deleteAll(self):
        self.myCanvas.delete("all")


if __name__ == '__main__':

    root = Tk()
    root.geometry("1005x500+300+300")
    app = Application(root)
    root.mainloop()
