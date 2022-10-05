import os
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
import face_recognition
from PIL import Image, ImageTk
import time

# gui
root = Tk()
frm = Frame(root)
frm.pack(side=BOTTOM, padx=15, pady=15)


def showimage():
    fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="select image", filetypes=(
        ("JPG File", "*.jpg"), ("PNG File", "*.png"), ("All Files", "*.*")))
    img = Image.open(fln)
    img.thumbnail((400, 400))
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image = img
    known_image = face_recognition.load_image_file(fln)
    face_encoding = face_recognition.face_encodings(known_image)[0]
    return face_encoding


def showimage2():
    fln2 = filedialog.askopenfilename(initialdir=os.getcwd(), title="select image", filetypes=(
        ("JPG File", "*.jpg"), ("PNG File", "*.png"), ("All Files", "*.*")))
    img2 = Image.open(fln2)
    img2.thumbnail((400, 400))
    img2 = ImageTk.PhotoImage(img2)
    lbl2.configure(image=img2)
    lbl2.image = img2
    image_to_test = face_recognition.load_image_file(fln2)
    image_to_test_encoding = face_recognition.face_encodings(image_to_test)[0]
    return image_to_test_encoding


def compare1(a, b):
    global sonuc
    global text1
    known_encodings = [
        a]
    face_distances = face_recognition.face_distance(known_encodings, b)
    for i, face_distance in enumerate(face_distances):
        print("fotografin orjinal fotografa olan uzakligi {:.2} #{}".format(
            face_distance, i))
        calc = 100-(face_distance*100)
        
        print("% ", calc, " benzerlik var")
        text1='% {} benzerlik var'.format(round(calc,2))
        sonuc.config(font=("Android",18))
        sonuc.config(text=text1)
        print()
        
sonuc = Label(root, text='')
sonuc.pack(side=BOTTOM,pady=10)

def buttonclick():
    global a
    a = showimage()


def button2click():
    global b
    b = showimage2()


# rs2
lbl = Label(root)
lbl.pack(side=LEFT)
# rs1
lbl2 = Label(root)
lbl2.pack(side=RIGHT)

# ilk resim
btn = Button(frm, text="first image", command=buttonclick)
btn.pack(side=tk.LEFT)

# exit
btn2 = Button(frm, text="exit", command=lambda: exit())
btn2.pack(side=tk.LEFT, padx=10)

# ikinci resim
btn3 = Button(frm, text="second image", command=button2click)
btn3.pack(side=tk.LEFT, padx=10)

# karsilastirma
btn4 = Button(frm, text="compare", command=lambda: compare1(a, b))
btn4.pack(side=tk.LEFT, padx=10)

root.title("face compare - batuhan rapata")
root.geometry("820x580")
root.mainloop()
