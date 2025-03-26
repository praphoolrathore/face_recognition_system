from tkinter import *
from PIL import Image, ImageTk
from time import strftime
from tkinter import messagebox
import os
import subprocess

class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        self.root.geometry("1280x720")

        # **Check if image exists**
        image_path = "college_images/main_bg.jpg"
        if not os.path.exists(image_path):
            print(f"Error: Background image '{image_path}' not found!")

        # **Set Background Image**
        self.bg_image = Image.open(image_path)
        self.bg_image = self.bg_image.resize((1100, 720), Image.LANCZOS)  
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.bg_label = Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, width=1100, height=720)  

        # **Navbar Frame**
        navbar_width = 200  
        self.navbar = Frame(self.root, bg="#1a1a2e", width=navbar_width)  # Dark theme navbar
        self.navbar.place(x=1100, y=0, width=navbar_width, height=720)  

        # **Circular Time Display Frame**
        self.time_frame = Frame(self.navbar, bg="#16213E", bd=4, relief=SOLID)
        self.time_frame.pack(pady=20, padx=30)

        # **Time Labels (Stacked Format)**
        self.time_hours = Label(self.time_frame, text="00", font=("Digital-7", 30, "bold"), fg="cyan", bg="#16213E")
        self.time_hours.pack()

        self.time_minutes = Label(self.time_frame, text="00", font=("Digital-7", 30, "bold"), fg="lime", bg="#16213E")
        self.time_minutes.pack()

        self.time_seconds = Label(self.time_frame, text="00", font=("Digital-7", 20, "bold"), fg="yellow", bg="#16213E")
        self.time_seconds.pack()

        self.time_ampm = Label(self.time_frame, text="AM", font=("Digital-7", 15, "bold"), fg="white", bg="#16213E")
        self.time_ampm.pack()

        self.update_time()

        # **Navbar Buttons Data**
        self.buttons_data = [
            ("📚 Student", "student.py"),
            ("🔍 Detect  Face", "face_recognition.py"),
            ("📋 Attendance", "attendance.py"),
            ("📂 Train", "train.py"),
            ("🖼 Photos", "data"),
            #("👨‍💻 Developer", "developer.py"),
            ("❓ Help", "helpp.py"),
            ("Exit", "exit")
        ]

        self.create_navbar_buttons()

    def update_time(self):
        """Updates the time display with a futuristic stacked design."""
        current_time = strftime('%I %M %S %p').split()
        self.time_hours.config(text=current_time[0])
        self.time_minutes.config(text=current_time[1])
        self.time_seconds.config(text=current_time[2])
        self.time_ampm.config(text=current_time[3])
        self.time_hours.after(1000, self.update_time)

    def create_navbar_buttons(self):
        """Creates styled navbar buttons dynamically (Vertical Layout)."""
        for text, command in self.buttons_data:
            if command == "exit":  # Place Exit Button at Exact Position
                btn = Button(self.root, text=text, font=("Montserrat", 12, "bold"),
                            bg="white", fg="black", bd=0, relief=FLAT, padx=10, pady=6,
                            width=1, cursor="hand2", command=lambda cmd=command: self.execute_command(cmd))
                btn.place(x=1045, y=22)  # ✅ Set exact position on screen
            else:
                btn = Button(self.navbar, text=text, font=("Montserrat", 12, "bold"),
                            bg="#34495e", fg="white", bd=0, relief=FLAT, padx=10, pady=12,
                            width=15, cursor="hand2", command=lambda cmd=command: self.execute_command(cmd))
                btn.pack(pady=10)

                # **Hover Effects**
                btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#1abc9c"))
                btn.bind("<Leave>", lambda e, b=btn: b.config(bg="#34495e"))


    def execute_command(self, command):
        """Executes the respective command for each button."""
        if command == "data":
            os.startfile(command)  # Opens Photos
        elif command == "exit":
            if messagebox.askyesno("Face Recognition", "Are you sure you want to exit?", parent=self.root):
                self.root.destroy()
        else:
            subprocess.Popen(["python", command])

if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()
