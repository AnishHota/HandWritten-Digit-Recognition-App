from tkinter import *
from random import randint

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

from PIL import Image, ImageTk
import pyscreenshot as ImageGrab

#  http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
#  http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html
#  http://zetcode.com/gui/tkinter/drawing/

class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.toolsThickness = 20
        self.rgb = "#%02x%02x%02x" % (255, 255, 255)
        self.pack()
        self.createroots()
        self.cv = tk.Canvas(self)
        self.txt = "PICTURE NOT DRAWN"

    def createroots(self):
        tk_rgb = "#%02x%02x%02x" % (128, 192, 200)

        self.leftFrame = Frame(self, bg = tk_rgb)
        self.leftFrame.grid(row =0,column =0)
  ##BUTTON EDIT 2
        self.Button2 = Button(self.leftFrame,text = "PREDICT", width = 50,command = self.SAVE)
        self.Button2.grid(row = 0, column =0, sticky = NW, pady = 2, padx = 3)
        #----------------------------------------------
        self.buttonDeleteAll = Button(self.leftFrame, text = "clear paper",
                                      command = self.delteAll)
        self.buttonDeleteAll.grid(row = 2, column =0)
#----------------------------------------------------------------------
        self.label1 = Label(self.leftFrame,text ="Text not defined",width = 50).grid(row =12,column = 0,sticky = S)
#----------------------------------------------------------------------
        self.myCanvas = Canvas(self, width = 800,height = 500,bg="black", relief=RAISED, borderwidth=5)
        self.myCanvas.grid(row = 0,column = 5,columnspan = 800)
        self.myCanvas.bind("<B1-Motion>", self.draw)
        self.myCanvas.bind("<Button-1>", self.setPreviousXY)

#----------------------------------------------------------------------
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
        print('Screencshot tkinter canvas and saved as "out_snapsave.jpg w/o displaying screenshoot."')
        self.txt = "WORK NOT COMPLETE"

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

    def delteAll(self):
        self.myCanvas.delete("all")




if __name__ == '__main__':
    root = Tk()
    root.title("Drawing program")
    app = Application(root)
    root.mainloop()
