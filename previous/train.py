from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:  # Create class
    def __init__(self, root):  # Constructor
        self.root = root    # Initialize
        self.root.geometry("1530x790+0+0")  # Window size
        self.root.title("face recognition system")  

        title_lbl=Label(self.root,text="Train DataSet",font=("montserrat",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top = Image.open("C:/Users/ASUS/OneDrive/Desktop/face_recognition system/college_images/third_image.jpeg")
        img_top = img_top.resize((1530, 325), Image.LANCZOS)  # resize syntax
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        # # Display image
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=325)

        #button
        b1_1=Button(self.root,text="Train data",command=self.train_classifier,cursor="hand2",font=("montserrat",30,"bold"),bg="lightskyblue",fg="black")
        b1_1.place(x=0,y=380,width=1530,height=60)


        img_bottom = Image.open("C:/Users/ASUS/OneDrive/Desktop/face_recognition system/college_images/third_image.jpeg")
        img_bottom = img_bottom.resize((1530, 325), Image.LANCZOS)  # resize syntax
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        # # Display image
        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=440, width=1530, height=325)

    def train_classifier(self):
        data_dir=("data")

        path=[os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #Gray scale image
            imageNp=np.array(img, 'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1)==13

        ids=np.array(ids)
    
    
        #=====Train the classifies and save==========
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)

        clf.write("classifier.xml")
        cv2.destroyAllWindows()

        messagebox.showinfo("Result", "Training datasets completed!!")



        



if __name__ == "__main__":  # Main function
    root = Tk()
    obj = Train(root)
    root.mainloop()