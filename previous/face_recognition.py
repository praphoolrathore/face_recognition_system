from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
import cv2
import os
import threading
from datetime import datetime
import re

# Database Credentials
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "praful")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", 3305))
DB_NAME = "face_recognizer"

class FaceRecognition:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        self.root.state('zoomed')  
        self.root.configure(bg='#f0f0f0')

        self.subject = StringVar()

        frame = Frame(self.root, bg="#ffffff", bd=2, relief=RIDGE)
        frame.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.2)

        Label(frame, text="Enter Subject Name:", font=("montserrat", 14, "bold"), bg="#ffffff").pack(pady=10)
        self.entry_subject = Entry(frame, textvariable=self.subject, font=("montserrat", 14))
        self.entry_subject.pack(pady=5, ipadx=10, ipady=5, fill=X, padx=50)
        Button(frame, text="Start Attendance", font=("montserrat", 14, "bold"), bg="green", fg="white", command=self.get_subject).pack(pady=10)

    def sanitize_subject(self, subject_name):
        return re.sub(r'[^a-zA-Z0-9_]', '_', subject_name)

    def get_subject(self):
        subject_name = self.sanitize_subject(self.subject.get().strip())
        if not subject_name:
            messagebox.showerror("Error", "Please enter a valid subject name.")
            return
        self.subject.set(subject_name)
        self.create_table()
        self.start_face_recognition()

    def create_table(self):
        conn = mysql.connector.connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST, database=DB_NAME, port=DB_PORT)
        my_cursor = conn.cursor()
        today_date = datetime.now().strftime("%Y-%m-%d")
        subject_name = self.subject.get()

        my_cursor.execute(f"CREATE TABLE IF NOT EXISTS `{subject_name}` (student_id INT PRIMARY KEY, name VARCHAR(255), roll VARCHAR(50), dep VARCHAR(100))")
        my_cursor.execute(f"SHOW COLUMNS FROM `{subject_name}` LIKE '{today_date}'")
        if not my_cursor.fetchone():
            my_cursor.execute(f"ALTER TABLE `{subject_name}` ADD COLUMN `{today_date}` ENUM('Present', 'Absent') DEFAULT 'Absent'")

        conn.commit()
        conn.close()

    def start_face_recognition(self):
        threading.Thread(target=self.face_recog, daemon=True).start()

    def face_recog(self):
        if not os.path.exists("classifier.xml"):
            messagebox.showerror("Error", "Trained model (classifier.xml) not found. Train the model first!")
            return
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        video_cap = cv2.VideoCapture(1)
        if not video_cap.isOpened():
            messagebox.showerror("Error", "Camera not detected.")
            return
        while True:
            ret, img = video_cap.read()
            cv2.imshow("Face Recognition", img)
            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
