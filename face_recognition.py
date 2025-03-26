from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
import cv2
import os
import time
from datetime import datetime
import re  # For subject name validation
from PIL import Image, ImageTk  # ✅ Import for Background Image

class FaceRecognition:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        self.root.state('zoomed')  # Open in fullscreen mode

        # ✅ Load and Set Background Image
        image_path = "college_images/attendence_bg.jpg"  # Make sure this file exists
        if not os.path.exists(image_path):
            messagebox.showerror("Error", "Background image not found!")
            return

        self.bg_image = Image.open(image_path)
        self.bg_image = self.bg_image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.bg_label = Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # ✅ Fullscreen background

        # ✅ Transparent Frame for Inputs
        frame = Frame(self.root, bg="#ffffff", bd=2, relief=RIDGE)
        frame.place(relx=0.3, rely=0.3, relwidth=0.4, relheight=0.3)

        lbl_subject = Label(frame, text="Enter Subject Name:", font=("montserrat", 14, "bold"), bg="#ffffff")
        lbl_subject.pack(pady=10)

        self.subject = StringVar()
        self.entry_subject = Entry(frame, textvariable=self.subject, font=("montserrat", 14))
        self.entry_subject.pack(pady=5, ipadx=10, ipady=5, fill=X, padx=50)

        # ✅ Styled Start Attendance Button
        btn_submit = Button(frame, text="Start Attendance", font=("montserrat", 14, "bold"), bg="green", fg="white",
                            command=self.get_subject)
        btn_submit.pack(pady=10)
        btn_submit.bind("<Enter>", lambda e: btn_submit.config(bg="#006400"))  # Darker green on hover
        btn_submit.bind("<Leave>", lambda e: btn_submit.config(bg="green"))

    def sanitize_subject(self, subject_name):
        """Sanitize subject name for database table naming."""
        return re.sub(r'[^a-zA-Z0-9_]', '_', subject_name)

    def get_subject(self):
        """Retrieve and validate subject name before starting attendance."""
        subject_name = self.sanitize_subject(self.subject.get().strip())
        if not subject_name:
            messagebox.showerror("Error", "Please enter a valid subject name.")
            return
        self.subject.set(subject_name)
        self.create_table()
        self.face_recog()

    def create_table(self):
        """Create a table for the subject if it doesn't exist and add the date column."""
        try:
            conn = mysql.connector.connect(user="root", password="praful", host="localhost", database="face_recognizer", port=3305)
            my_cursor = conn.cursor()
            today_date = datetime.now().strftime("%Y-%m-%d")
            subject_name = self.subject.get()

            create_query = f"""
            CREATE TABLE IF NOT EXISTS `{subject_name}` (
                student_id INT PRIMARY KEY,
                name VARCHAR(255),
                roll VARCHAR(50),
                dep VARCHAR(100)
            );
            """
            my_cursor.execute(create_query)

            # Add today's attendance column if it doesn't exist
            my_cursor.execute(f"SHOW COLUMNS FROM `{subject_name}` LIKE '{today_date}'")
            if not my_cursor.fetchone():
                my_cursor.execute(f"ALTER TABLE `{subject_name}` ADD COLUMN `{today_date}` ENUM('Present', 'Absent') DEFAULT 'Absent'")

            conn.commit()
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error: {str(e)}")
        finally:
            conn.close()

    def mark_attendance(self, student_id, roll, name, dep):
        """Mark attendance for recognized students."""
        if student_id == "Unknown":
            return  # ✅ Skip unknown faces

        try:
            conn = mysql.connector.connect(user="root", password="praful", host="localhost", database="face_recognizer", port=3305)
            my_cursor = conn.cursor()
            today_date = datetime.now().strftime("%Y-%m-%d")
            subject_name = self.subject.get()

            check_query = f"SELECT * FROM `{subject_name}` WHERE student_id = %s"
            my_cursor.execute(check_query, (student_id,))
            result = my_cursor.fetchone()

            if result:
                update_query = f"UPDATE `{subject_name}` SET `{today_date}` = 'Present' WHERE student_id = %s"
                my_cursor.execute(update_query, (student_id,))
            else:
                insert_query = f"INSERT INTO `{subject_name}` (student_id, name, roll, dep, `{today_date}`) VALUES (%s, %s, %s, %s, 'Present')"
                my_cursor.execute(insert_query, (student_id, name, roll, dep))

            conn.commit()
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error: {str(e)}")
        finally:
            conn.close()

    def face_recog(self):
        """Perform face recognition and mark attendance for recognized students."""
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            try:
                conn = mysql.connector.connect(user="root", password="praful", host="localhost", database="face_recognizer", port=3305)
                my_cursor = conn.cursor()
            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", f"Error: {str(e)}")
                return

            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int(100 * (1 - predict / 300))

                my_cursor.execute("SELECT student_id, name, roll, dep FROM student WHERE student_id = %s", (id,))
                result = my_cursor.fetchone()

                if result and confidence > 80:
                    student_id, name, roll, dep = result
                    color = (0, 255, 0)  # Green for recognized faces

                    # Get Current Time
                    current_time = datetime.now().strftime("%H:%M:%S")

                    # **Show ID, Name, and Time on Camera**
                    cv2.putText(img, f"ID: {student_id}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 2)
                    cv2.putText(img, f"Name: {name}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 2)
                    cv2.putText(img, f"Time: {current_time}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 2)

                    # Mark Attendance
                    self.mark_attendance(student_id, roll, name, dep)

            conn.close()

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")  # ✅ Load trained model

        video_cap = cv2.VideoCapture(0)
        if not video_cap.isOpened():
            messagebox.showerror("Error", "Camera not detected. Please check your webcam.")
            return

        while True:
            ret, img = video_cap.read()
            draw_boundary(img, faceCascade, 1.1, 10, clf)
            cv2.imshow("Face Recognition", img)
            if cv2.waitKey(1) == 13:  # Press Enter to Exit
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognition(root)
    root.mainloop()
