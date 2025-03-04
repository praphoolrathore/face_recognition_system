from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os 


class Developer:  # Create class
    def __init__(self, root):  # Constructor
        self.root = root    # Initialize
        self.root.geometry("1530x790+0+0")  # Window size
        self.root.title("face recognition system")  

        title_lbl=Label(self.root,text="Developer window",font=("montserrat",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top = Image.open("C:/Users/ASUS/OneDrive/Desktop/face_recognition system/college_images/bg_image.webp")
        img_top = img_top.resize((1530, 720), Image.LANCZOS)  # resize syntax
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        # # Display image
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=720)

        # Frame
        main_frame=Frame(f_lbl, bd=2, bg="white")

        main_frame.place(x=1000, y=0, width=500, height=600)

        img_top1=Image.open("C:/Users/ASUS/OneDrive/Desktop/face_recognition system/college_images/second_image.jpeg")
        img_top1=img_top1.resize((200,200), Image.LANCZOS)

        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame, image=self.photoimg_top1)
        f_lbl.place(x=300, y=0, width=200, height=200)

        # Developer info
        dev_label= Label(main_frame,text="This is about page for",font=("montserrat",15,"bold"),bg="white")
        dev_label.place(x=0,y=5)

        dev_label= Label(main_frame,text="Developers ,stay tuned ",font=("montserrat",15,"bold"),bg="white")
        dev_label.place(x=0,y=40)

         # # third image
        img2 = Image.open("C:/Users/ASUS/OneDrive/Desktop/face_recognition system/college_images/third_image.jpeg")
        img2 = img2.resize((500, 390), Image.LANCZOS)  # resize syntax
        self.photoimg2 = ImageTk.PhotoImage(img2)

        # # Display image
        f_lbl = Label(main_frame, image=self.photoimg2)
        f_lbl.place(x=0, y=210, width=500, height=390)







if __name__ == "__main__":  # Main function
    root = Tk()
    obj = Developer(root)
    root.mainloop()

