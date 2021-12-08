from tkinter import *
#keydownfunction
def click():
    entered_text = textentry.get()
    


##main
window = Tk()
window.title("The new App")
window.configure(background = "black")
##photo
photo1 = PhotoImage(file = "giphy.gif")
Label(window,image = photo1,bg = "blue").grid(row =0,column = 0,sticky = E)
#create label
Label(window,text = "Text anything:",bg = "white",fg = "black").grid(row = 1,column = 0,sticky = S)
#enter Text
textentry = Entry(window,width = 20,bg = "white")
textentry.grid(row = 2,column = 0,sticky = N)
#add submit button
Button(window,text = "submit",width = 6,command = click).grid(row = 3,column = 0,sticky = E)





##run the main loop
window.mainloop()
