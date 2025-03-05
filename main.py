from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from time import strftime
import os
import subprocess

class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root

        # Get screen width and height dynamically
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()

        # Set window size dynamically
        self.root.geometry(f"{self.screen_width}x{self.screen_height}+-10+0")
        self.root.title("Face Recognition System")
        self.root.configure(bg="#f0f0f0")

        # **Dynamic Sizing Variables**
        self.title_height = int(self.screen_height * 0.07)  # 7% of screen height for title bar
        self.btn_width = int(self.screen_width * 0.14)  # 14% of screen width
        self.btn_height = int(self.screen_height * 0.22)  # 22% of screen height
        self.spacing_x = int(self.screen_width * 0.05)  # 5% of screen width for horizontal spacing
        self.spacing_y = int(self.screen_height * 0.08)  # **8% of screen height for row spacing (fix)**
        self.font_size = max(12, int(self.screen_width * 0.01))  # Adjust font size dynamically

        # **Background Image**
        self.bg_img = ImageTk.PhotoImage(
            Image.open("C:/Users/ASUS/OneDrive/Desktop/face_recognition system/college_images/bg_image.jpg")
            .resize((self.screen_width, self.screen_height - self.title_height), Image.LANCZOS)
        )
        Label(self.root, image=self.bg_img).place(x=0, y=self.title_height, width=self.screen_width, height=self.screen_height - self.title_height)

        # **Title Bar**
        title_lbl = Label(self.root, text="FACE RECOGNITION ATTENDANCE SYSTEM", 
                          font=("Montserrat", int(self.screen_width * 0.018), "bold"), 
                          bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=self.screen_width, height=self.title_height)

        # **Time Display**
        def time():
            lbl.config(text=strftime('%H:%M:%S %p'))
            lbl.after(1000, time)
        
        lbl = Label(title_lbl, font=('Times New Roman', int(self.screen_width * 0.008), 'bold'), 
                    background='white', foreground='blue')
        lbl.place(x=int(self.screen_width * 0.01), y=int(self.title_height * 0.1), 
                  width=int(self.screen_width * 0.07), height=int(self.title_height * 0.7))
        time()

        # **Button Data (Dynamically Placed)**
        self.buttons_data = [
            ("Student Details", "student_datails.jpg", self.student_details),
            ("Face Detector", "face_recognition.jpg", self.face_data),
            ("Attendance", "attendence.jpg", self.attendance_data),
            ("Help", "help.jpg", self.help_data),
            ("Train Data", "train_data.jpg", self.train_data),
            ("Photos", "photos.jpg", self.open_img),
            ("Developer", "developer.jpg", self.developer_data),
            ("Exit", "exit.jpg", self.iExit),
        ]

        # **Create Buttons Dynamically**
        self.create_buttons()

    def create_buttons(self):
        """Dynamically creates buttons in two rows with proper spacing."""
        num_cols = 4  # 4 buttons per row
        total_width = (self.btn_width * num_cols) + (self.spacing_x * (num_cols - 1))
        start_x = (self.screen_width - total_width) // 2  # Centering

        row1_y = int(self.screen_height * 0.20)  # First row position
        row2_y = row1_y + self.btn_height + self.spacing_y  # **Now row spacing is fixed**

        for index, (text, img_path, command) in enumerate(self.buttons_data):
            x = start_x + (index % num_cols) * (self.btn_width + self.spacing_x)
            y = row1_y if index < num_cols else row2_y  # Decide row based on index

            self.create_button(text, img_path, command, x, y)

    def create_button(self, text, img_path, command, x, y):
        """Creates an interactive button with hover effects."""
        img = Image.open(f"C:/Users/ASUS/OneDrive/Desktop/face_recognition system/college_images/{img_path}")\
                  .resize((self.btn_width, self.btn_height), Image.LANCZOS)
        photo_img = ImageTk.PhotoImage(img)

        b = Button(self.root, image=photo_img, cursor="hand2", command=command, bd=0, relief=FLAT)
        b.image = photo_img
        b.place(x=x, y=y, width=self.btn_width, height=self.btn_height)

        b_text = Button(self.root, text=text, cursor="hand2", command=command, 
                        font=("Montserrat", self.font_size, "bold"), 
                        bg="lightskyblue", fg="black", bd=0, relief=FLAT)
        b_text.place(x=x, y=y + self.btn_height, width=self.btn_width, height=int(self.screen_height * 0.05))

        # Hover Effects
        b.bind("<Enter>", lambda e: b_text.config(bg="blue", fg="white"))
        b.bind("<Leave>", lambda e: b_text.config(bg="lightskyblue", fg="black"))

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        if messagebox.askyesno("Face Recognition", "Are you sure you want to exit?", parent=self.root):
            self.root.destroy()

    def student_details(self):
        subprocess.Popen(["python", "student.py"])  # Opens the student details window

    def train_data(self):
        subprocess.Popen(["python", "train.py"])  # Opens the training module

    def face_data(self):
        subprocess.Popen(["python", "face_recognition.py"])  # Opens face recognition module

    def attendance_data(self):
        subprocess.Popen(["python", "attendance.py"])  # Opens attendance tracking

    def developer_data(self):
        subprocess.Popen(["python", "developer.py"])  # Opens developer info

    def help_data(self):
        subprocess.Popen(["python", "helpp.py"])  # Opens help and FAQs

if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()
