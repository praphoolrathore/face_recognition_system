from tkinter import *
from PIL import Image, ImageTk

class Developer:
    def __init__(self, root):
        self.root = root

        # Get screen width and height dynamically
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        # Set window size dynamically
        self.root.geometry(f"{self.screen_width}x{self.screen_height}+-10+0")
        self.root.title("Face Recognition System")

        # **Dynamic Sizing Variables**
        self.title_height = int(self.screen_height * 0.07)  # 7% of screen height for title bar
        self.frame_width = int(self.screen_width * 0.35)    # 35% of screen width for right-side frame
        self.frame_height = int(self.screen_height * 0.75)  # 75% of screen height for the frame

        # **Title Bar**
        title_lbl = Label(self.root, text="Developer Window",
                          font=("Montserrat", int(self.screen_width * 0.018), "bold"),
                          bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=self.screen_width, height=self.title_height)

        # **Background Image (Scaled Dynamically)**
        img_top = Image.open("C:/Users/ASUS/OneDrive/Desktop/face_recognition system/college_images/bg_image.webp")
        img_top = img_top.resize((self.screen_width, self.screen_height - self.title_height), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        # **Display Background Image**
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=self.title_height, width=self.screen_width, height=self.screen_height - self.title_height)

        # **Frame for Developer Info (Positioned Dynamically)**
        main_frame = Frame(f_lbl, bd=2, bg="white")
        main_frame.place(x=self.screen_width - self.frame_width - 30, y=int(self.screen_height * 0.10),
                         width=self.frame_width, height=self.frame_height)

        # **Developer Profile Image (Scaled Dynamically)**
        img_top1 = Image.open("C:/Users/ASUS/OneDrive/Desktop/face_recognition system/college_images/second_image.jpeg")
        img_top1 = img_top1.resize((int(self.frame_width * 0.4), int(self.frame_height * 0.33)), Image.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl1 = Label(main_frame, image=self.photoimg_top1)
        f_lbl1.place(x=int(self.frame_width * 0.55), y=0, width=int(self.frame_width * 0.4), height=int(self.frame_height * 0.33))

        # **Developer Info Labels (Positioned Dynamically)**
        Label(main_frame, text="This is the about page for", font=("Montserrat", int(self.screen_width * 0.01), "bold"), bg="white").place(x=10, y=int(self.frame_height * 0.05))
        Label(main_frame, text="Developers, stay tuned!", font=("Montserrat", int(self.screen_width * 0.01), "bold"), bg="white").place(x=10, y=int(self.frame_height * 0.12))

        # **Additional Image (Scaled Dynamically)**
        img2 = Image.open("C:/Users/ASUS/OneDrive/Desktop/face_recognition system/college_images/third_image.jpeg")
        img2 = img2.resize((self.frame_width, int(self.frame_height * 0.65)), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl2 = Label(main_frame, image=self.photoimg2)
        f_lbl2.place(x=0, y=int(self.frame_height * 0.35), width=self.frame_width, height=int(self.frame_height * 0.65))

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
