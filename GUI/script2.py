import pickle
import imageio
from skimage import transform
from scipy import misc
from PIL import Image
import numpy as np
import PIL
import pandas as pd
from tkinter import Tk, Text, BOTH, W, N, E, S
from tkinter.ttk import Frame, Button, Label, Style
from random import randint
from PIL import Image, ImageTk
import pyscreenshot as ImageGrab

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

from PIL import Image, ImageTk
import pyscreenshot as ImageGrab

from subprocess import call

str1 = "NO INPUT FOR PREDICTION"
chosen_option = "NO OPTION SELECTED"
choices = ['1505361', '1505205', '1505232', '1505137', '1505095']

class Application(Frame):

    def __init__(self,master):
        super().__init__(master)
        self.toolsThickness = 20
        self.rgb = "#%02x%02x%02x" % (255, 255, 255)
        self.cv = tk.Canvas(self)
        self.initUI()

    def initUI(self):

        self.frame = Frame(self,)
        self.master.title("Digit Recognition")
        self.pack(fill=BOTH, expand = True)
        #root.iconbitmap('Logo of Digital Reconigiion.ico')
        self.myCanvas = tk.Canvas(self, width = 800,height = 500,bg="black", borderwidth=5)
        self.myCanvas.grid(rowspan = 500,columnspan = 800)
        self.myCanvas.bind("<B1-Motion>", self.draw)
        self.myCanvas.bind("<Button-1>", self.setPreviousXY)

        self.img = tk.PhotoImage(file = "button.png")
        self.Button1 = Button(self, text = "Predict", width=40, command = self.Predict, image = self.img)
        self.Button1.grid(row = 100, column = 802,columnspan = 5)

        self.img2 = tk.PhotoImage(file = "button2.png")
        self.Button2 = Button(self, text = "Clear Screen", width=30, command=self.deleteAll, image = self.img2)
        self.Button2.grid(row = 120, column = 802,columnspan = 5)

        self.label = Label(self,width =30, text = str)
        self.label.grid(row = 140, column = 802)

        self.var = tk.StringVar(self)
        self.var.set("Team Members:")

        self.drop_menu = tk.OptionMenu(self, self.var,  *choices, command = self.assign)
        self.drop_menu.grid(row=260, column=802)

        self.label_chosen_variable= Label(self, text = chosen_option)
        self.label_chosen_variable.grid(row = 270, column = 802)

    def assign(self,event):
        chosen_option = self.var.get()
        if chosen_option == "1505205":
            chosen_option = "Name : CHAMPAK SINHA\nRoll no. : 1505205\nSection : CS3"
        elif chosen_option == "1505137":
            chosen_option = "Name : RISHAB\nRoll no. : 1505137\nSection : CS2"
        elif chosen_option == "1505232":
            chosen_option = "Name : PRANESH BISWAS\nRoll no. : 1505232\nSection : CS3"
        elif chosen_option == "1505095":
            chosen_option = "Name : ANISH HOTA\nRoll no. : 1505095\nSection : CS2"
        elif chosen_option == "1505361":
            chosen_option = "Name : ANAND KUMAR\nRoll no. : 1505361\nSection : CS5"

        self.label_chosen_variable.config(text = chosen_option)

    def setThickness(self, event):
        print("Thickness is set to 20")
        self.toolsThickness = 20

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
        x=root.winfo_rootx()+5
        y=root.winfo_rooty()+5
        x1=x+805
        y1=y+root.winfo_height()-11
        box=(x,y,x1,y1)
        print('box = ', box)
        return box

    def deleteAll(self):
        self.myCanvas.delete("all")

    def Predict(self):
        self.SAVE()
        custom_image_classification()
        file = open("output.txt","r")
        str1 = "The drawn digit is->\n" + file.read()
        file.close()
        self.label.config(text = str1)

def custom_image_classification():
    img = imageio.imread('out_snapsave.jpg')
    img = transform.resize(img, (28,28))
    img = img.astype(features_dtype)
    img = misc.bytescale(img)
    x_test = []
    for eachRow in img:
        for eachPixel in eachRow:
            x_test.append(sum(eachPixel)/3)
    x_test = np.array(x_test)
    #Binarization
    x_test[x_test<225]=0
    x_test[x_test>=225]=255
    #Removing rows
    x_test = x_test.reshape((28,28))
    del_arr=[]
    for i in range(len(x_test)):
        if 255 not in x_test[i]:
            del_arr.append(i)
    x_test = np.delete(x_test,del_arr,0)
    #Removing Columns
    x_test=x_test.T
    del_arr=[]
    for i in range(len(x_test)):
        if 255 not in x_test[i]:
            del_arr.append(i)
    x_test = np.delete(x_test,del_arr,0)
    x_test = x_test.T
    misc.imsave('error.jpg',x_test)
    img2 = Image.open('error.jpg')
    wpercent = (28/float(img2.size[0]))
    hsize = int((float(img2.size[1])*float(wpercent)))
    img3 = img2.resize((28,28),PIL.Image.ANTIALIAS)
    img3.save('error3.jpg',img2.format)

    img = imageio.imread('error3.jpg')
    img = transform.resize(img,(28,28))
    img = img.astype(features_dtype)
    img = misc.bytescale(img)
    img_test = []
    for eachRow in img:
        for eachPixel in eachRow:
            img_test.append(eachPixel)
    img_test = np.array(img_test)
    img_test = img_test.reshape([1,784])
    img_test[img_test<np.mean(img_test)]=0
    img_test[img_test>=np.mean(img_test)]=255
    file = open("output.txt","w+")
    file.write(str(int(classifier_model.predict(img_test)[0])))
    file.close()

if __name__ == '__main__':
    features_dtype = pd.Series.from_csv('features_dtypes.csv')
    classifier_model = pickle.load(open('final_model.sav','rb'))
    root = Tk()
    root.geometry("1005x514+300+300")
    app = Application(root)
    root.mainloop()
   
