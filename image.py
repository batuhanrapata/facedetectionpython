from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title('image')
#root.iconbitmap('') icon file için 


my_image1=ImageTk.PhotoImage(Image.open("known\Robert_Downey_Jr.jpg"))
my_image2=ImageTk.PhotoImage(Image.open("group/rdj.jpg"))

image_list=[my_image1,my_image2]


my_label=Label(image=my_image1)
my_label.grid(row=0,column=0,columnspan=3)
def ileri(image_n):
    global my_label
    global btb_back
    global btb_forward

    my_label.grid_forget() #resm delete
    my_label=Label(image=image_list[image_n-1])
    my_label.grid(row=0,column=0,columnspan=3)
    btb_forward=Button(root,text="ileri",command=lambda: ileri(image_n))
    btb_back=Button(root,text="geri",command=lambda:geri(image_n-1))
    btb_forward.grid(row=1,column=2)
    btb_back.grid(row=1,column=0)



def geri():
    return

btb_back=Button(root,text="geri",command=geri)
btb_back.grid(row=1,column=0)
btb_forward=Button(root,text="ileri",command=lambda:ileri(2))
btb_forward.grid(row=1,column=2)




button_quit=Button(root,text="exit",command=root.quit)
button_quit.grid(row=1,column=1)
root.mainloop()