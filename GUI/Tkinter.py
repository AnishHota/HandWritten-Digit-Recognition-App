from tkinter import *
root  = Tk()
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side = BOTTOM)
Button1 = Button(topFrame, text = "Button 1", fg = "red")
Button2 = Button(topFrame, text = "Button 2", fg = "yellow")
Button3 = Button(bottomFrame, text = "Button 3", fg = "purple")
Button4 = Button(bottomFrame, text = "Button 4", fg = "green")

Button1.pack()
Button2.pack()
Button3.pack()
Button4.pack()
root.mainloop()