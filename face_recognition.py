from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
import cv2
import os
from datetime import datetime
import re  # For subject name validation

class FaceRecognition:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        self.root.state('zoomed')  # Open in fullscreen mode
        self.root.configure(bg='#f0f0f0')

        # Subject Selection UI
        self.subject = StringVar()

        frame = Frame(self.root, bg="#ffffff", bd=2, relief=RIDGE)
        frame.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.2)

        lbl_subject = Label(frame, text="Enter Subject Name:", font=("montserrat", 14, "bold"), bg="#ffffff")
        lbl_subject.pack(pady=10)

        self.entry_subject = Entry(frame, textvariable=self.subject, font=("montserrat", 14))
        self.entry_subject.pack(pady=5, ipadx=10, ipady=5, fill=X, padx=50)

        btn_submit = Button(frame, text="Start Attendance", font=("montserrat", 14, "bold"), bg="green", fg="white", command=self.get_subject)
        btn_submit.pack(pady=10)

    def sanitize_subject(self, subject_name):
        return re.sub(r'[^a-zA-Z0-9_]', '_', subject_name)

    def get_subject(self):
        subject_name = self.sanitize_subject(self.subject.get().strip())
        if not subject_name:
            messagebox.showerror("Error", "Please enter a valid subject name.")
            return
        self.subject.set(subject_name)
        self.create_table()
        self.face_recog()

    def create_table(self):
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

        my_cursor.execute(f"SHOW COLUMNS FROM `{subject_name}` LIKE '{today_date}'")
        if not my_cursor.fetchone():
            my_cursor.execute(f"ALTER TABLE `{subject_name}` ADD COLUMN `{today_date}` ENUM('Present', 'Absent') DEFAULT 'Absent'")
        
        conn.commit()
        conn.close()

    def mark_attendance(self, student_id, roll, name, dep):
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
        conn.close()

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            
            conn = mysql.connector.connect(user="root", password="praful", host="localhost", database="face_recognizer", port=3305)
            my_cursor = conn.cursor()
            
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                my_cursor.execute("SELECT student_id, name, roll, dep FROM student WHERE student_id = %s", (id,))
                result = my_cursor.fetchone()

                if result:
                    student_id, name, roll, dep = result
                else:
                    student_id, name, roll, dep = "Unknown", "Unknown", "Unknown", "Unknown"

                if confidence > 77:
                    cv2.putText(img, f"ID: {student_id}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll: {roll}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name: {name}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department: {dep}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(student_id, roll, name, dep)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
            
            conn.close()

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap = cv2.VideoCapture(0)
        if not video_cap.isOpened():
            messagebox.showerror("Error", "Camera not detected. Please check your webcam.")
            return
        
        while True:
            ret, img = video_cap.read()
            draw_boundary(img, faceCascade, 1.1, 10, clf)
            cv2.imshow("Face Recognition", img)
            if cv2.waitKey(1) == 13:
                break
        
        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognition(root)
    root.mainloop()
