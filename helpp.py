from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os 


class Help:  # Create class
    def __init__(self, root):  # Constructor
        self.root = root    # Initialize
        self.root.geometry("1530x790+0+0")  # Window size
        self.root.title("face recognition system")  

        title_lbl=Label(self.root,text="Help Desk",font=("montserrat",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top = Image.open("C:/Users/ASUS/OneDrive/Desktop/face_recognition system/college_images/bg_image.jpg")
        img_top = img_top.resize((1530, 720), Image.LANCZOS)  # resize syntax
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        # # Display image
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=720)
        
        dev_label1= Label(f_lbl,text="Email: praphoolrathore2003@gmail.com",font=("montserrat",15,"bold"),bg="white")
        dev_label1.place(x=550,y=220)

        dev_label2= Label(f_lbl,text="Email: harshvardhans809@gmail.com   ",font=("montserrat",15,"bold"),bg="white")
        dev_label2.place(x=550,y=270)

        dev_label3= Label(f_lbl,text="Email: pranavmakwanaop@gmail.com   ",font=("montserrat",15,"bold"),bg="white")
        dev_label3.place(x=550,y=320)


if __name__ == "__main__":  # Main function
    root = Tk()
    obj = Help(root)
    root.mainloop()

