from tkinter import *

root=Tk()
myLabel1=Label(root,text="hello world!").grid(row=0,column=0)
myLabel2=Label(root,text="batuhan rapata").grid(row=1,column=1)

myButton=Button(root,text="bas")


myButton.grid(row=3,column=3)
root.mainloop()