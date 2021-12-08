from tkinter import *
from random import randint
#  http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
#  http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html
#  http://zetcode.com/gui/tkinter/drawing/
class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.toolsThickness = 30
        self.rgb = "#%02x%02x%02x" % (255, 255, 255)
        self.pack()
        self.createWidgets()

    def SAVE():
        self.output_text="SAVE NOT DEFINED"
        return (self.output_text)

    def createWidgets(self):
        tk_rgb = "#%02x%02x%02x" % (128, 192, 200)

        self.leftFrame = Frame(self, bg = tk_rgb)
        self.leftFrame.pack(side = LEFT, fill = Y)
  ##BUTTON EDIT 1
        self.Button1 = Button(self.leftFrame, text = "SAVE IMAGE",width = 50,command =self.SAVE )
        self.Button1.grid(row = 0, column = 0, sticky = NW, pady = 2, padx = 3)
        #-----------------------------------------------
  ##BUTTON EDIT 2
        self.Button2 = Button(self.leftFrame,text = "PREDICT", width = 50)
        self.Button2.grid(row = 5, column =0, sticky = NW, pady = 2, padx = 3)
        #----------------------------------------------
        self.buttonDeleteAll = Button(self.leftFrame, text = "clear paper",
                                      command = self.delteAll,width = 50)
        self.buttonDeleteAll.grid(padx = 3, pady = 2,
                                    row = 11, column =0,
                                    sticky = NW)
#----------------------------------------------------------------------
        self.label1 = Label(self.leftFrame,text ="Text not defined",width = 50).grid(row =12,column = 0,sticky = S)
#----------------------------------------------------------------------
        self.myCanvas = Canvas(self, width = 800,height = 500,bg="black", relief=RAISED, borderwidth=5)
        self.myCanvas.pack(side = RIGHT)
        self.myCanvas.bind("<B1-Motion>", self.draw)
        self.myCanvas.bind("<Button-1>", self.setPreviousXY)

#----------------------------------------------------------------------
    def setThickness(self, event):
        print("Thickness is set to 20")
        self.toolsThickness = 30

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
        self.myCanvas.create_line(self.previousX, self.previousY,
                                      event.x, event.y,
                                      width = self.toolsThickness,
                                      fill = self.rgb)
        self.previousX = event.x
        self.previousY = event.y

    def delteAll(self):
        self.myCanvas.delete("all")




root = Tk()
root.title("Drawing program")
app = Application(root)
root.mainloop()
