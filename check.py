from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from time import strftime
import os

class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.configure(bg="#f0f0f0")

        # Background Image
        self.bg_img = ImageTk.PhotoImage(Image.open("C:/Users/ASUS/OneDrive/Desktop/face_recognition system/college_images/bg_image.jpg").resize((1530, 710), Image.LANCZOS))
        Label(self.root, image=self.bg_img).place(x=0, y=130, width=1530, height=710)

        # Title Bar
        title_lbl = Label(self.root, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("Montserrat", 25, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Time Display
        def time():
            lbl.config(text=strftime('%H:%M:%S %p'))
            lbl.after(1000, time)
        
        lbl = Label(title_lbl, font=('Times New Roman', 14, 'bold'), background='white', foreground='blue')
        lbl.place(x=10, y=5, width=110, height=30)
        time()

        # Button Data
        self.buttons_data = [
            ("Student Details", "student_datails.jpg", self.student_details, 200, 100),
            ("Face Detector", "face_recognition.jpg", self.face_data, 500, 100),
            ("Attendance", "attendence.jpg", self.attendance_data, 800, 100),
            ("Help", "help.jpg", self.help_data, 1100, 100),
            ("Train Data", "train_data.jpg", self.train_data, 200, 380),
            ("Photos", "photos.jpg", self.open_img, 500, 380),
            ("Developer", "developer.jpg", self.developer_data, 800, 380),
            ("Exit", "exit.jpg", self.iExit, 1100, 380),
        ]

        self.button_objects = []

        for text, img_path, command, x, y in self.buttons_data:
            self.create_button(text, img_path, command, x, y)

    def create_button(self, text, img_path, command, x, y):
        """Creates an interactive button with hover effects."""
        img = Image.open(f"C:/Users/ASUS/OneDrive/Desktop/face_recognition system/college_images/{img_path}").resize((220, 220), Image.LANCZOS)
        photo_img = ImageTk.PhotoImage(img)

        b = Button(self.root, image=photo_img, cursor="hand2", command=command, bd=0, relief=FLAT)
        b.image = photo_img
        b.place(x=x, y=y, width=220, height=220)

        b_text = Button(self.root, text=text, cursor="hand2", command=command, font=("Montserrat", 15, "bold"), bg="lightskyblue", fg="black", bd=0, relief=FLAT)
        b_text.place(x=x, y=y+200, width=220, height=40)

        # Hover Effects
        b.bind("<Enter>", lambda e: b_text.config(bg="blue", fg="white"))
        b.bind("<Leave>", lambda e: b_text.config(bg="lightskyblue", fg="black"))

        self.button_objects.append((b, b_text))

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        if messagebox.askyesno("Face Recognition", "Are you sure you want to exit?", parent=self.root):
            self.root.destroy()

    def student_details(self):
        messagebox.showinfo("Student Details", "This feature will display student details.")

    def train_data(self):
        messagebox.showinfo("Train Data", "This feature will train face recognition data.")

    def face_data(self):
        messagebox.showinfo("Face Detector", "This feature will recognize faces.")

    def attendance_data(self):
        messagebox.showinfo("Attendance", "This feature will track attendance.")

    def developer_data(self):
        messagebox.showinfo("Developer", "This feature will show developer information.")

    def help_data(self):
        messagebox.showinfo("Help", "This feature will provide help and FAQs.")

if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()
add functionalities of button in this code
which was previously linked to or redirecting to another window