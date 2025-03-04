from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
from time import strftime
from datetime import datetime
import numpy as np



class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Title label
        title_lbl = Label(self.root, text="Face Recognition System", 
                          font=("montserrat", 30, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=50)

        # Main Frame
        main_frame = Frame(self.root, bd=2, bg="lightyellow", relief=RIDGE)
        main_frame.place(x=10, y=70, width=1480, height=670)

        # LabelFrame for Attendance Section
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, 
                                text="To mark attendance, click the button ...", 
                                font=("montserrat", 12, "bold"))
        Left_frame.place(x=10, y=300, width=730, height=100)

        # Face Recognition Button (with hover effect)
        def on_enter(e):
            b1_1.config(bg="deepskyblue")

        def on_leave(e):
            b1_1.config(bg="lightskyblue")

        b1_1 = Button(
            Left_frame, text="Face Recognition", cursor="hand2",
            font=("montserrat", 18, "bold"), bg="lightskyblue", fg="black",
            command=self.face_recog
        )
        b1_1.place(x=10, y=40, width=207, height=40)

        # Adding hover effect
        b1_1.bind("<Enter>", on_enter)
        b1_1.bind("<Leave>", on_leave)

        # 🎨 Bubble Design on Right Side
        bubble_canvas = Canvas(main_frame, bg="lightyellow", bd=0, highlightthickness=0)
        bubble_canvas.place(x=1050, y=50, width=400, height=600)

        # List of bubble positions & sizes
        bubbles = [
            (50, 50, 120, 120),
            (200, 80, 270, 150),
            (100, 200, 180, 280),
            (220, 300, 290, 370),
            (80, 400, 150, 470),
            (250, 450, 320, 520),
            (150, 100, 230, 180),
            (300, 250, 370, 320),
            (180, 380, 250, 450),
            (50, 500, 120, 570)
        ]

        # Dictionary to track original sizes
        self.bubble_ids = {}

        # Function to enlarge bubble on hover
        def on_bubble_enter(event, bubble_id, original_coords):
            x1, y1, x2, y2 = original_coords
            bubble_canvas.coords(bubble_id, x1 - 5, y1 - 5, x2 + 5, y2 + 5)  # Expand

        # Function to reset bubble size
        def on_bubble_leave(event, bubble_id, original_coords):
            bubble_canvas.coords(bubble_id, *original_coords)  # Reset to original size

        # Draw Bubbles with Interactivity
        for coords in bubbles:
            bubble_id = bubble_canvas.create_oval(*coords, outline="black", width=2)
            self.bubble_ids[bubble_id] = coords  # Store original coords

            # Bind hover effects
            bubble_canvas.tag_bind(
                bubble_id, "<Enter>", 
                lambda event, id=bubble_id, c=coords: on_bubble_enter(event, id, c)
            )
            bubble_canvas.tag_bind(
                bubble_id, "<Leave>", 
                lambda event, id=bubble_id, c=coords: on_bubble_leave(event, id, c)
            )



    #==========addtendence=============
    def mark_attendence(self,i,r,n,d):
        #def mark_attendance(self,i,r,n,d):
        with open("praful.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]

            for line in myDataList:
                entry=line.split((","))  # praful,2,IT
                name_list.append(entry[0])

            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list) and (i!="Unknown") and (r!="Unknown") and (n!="Unknown") and (d!="Unknown")):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")

                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i}, {r}, {n}, {d}, {dtString}, {d1}, Present")




    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []
            conn = mysql.connector.connect(user="root", password="praful", host="localhost",
                                           database="face_recognizer", port=3305)
            my_cursor = conn.cursor()

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                # Fetch student details
                my_cursor.execute("SELECT name FROM student WHERE student_id = %s", (id,))
                n = my_cursor.fetchone()
                n = "+".join(n) if n else "Unknown"

                my_cursor.execute("SELECT roll FROM student WHERE student_id = %s", (id,))
                r = my_cursor.fetchone()
                r = "+".join(r) if r else "Unknown"

                my_cursor.execute("SELECT dep FROM student WHERE student_id = %s", (id,))
                d = my_cursor.fetchone()
                d = "+".join(d) if d else "Unknown"

                my_cursor.execute("SELECT student_id FROM student WHERE student_id = %s", (id,))
                i = my_cursor.fetchone()
                i = str(i[0]) if i else "Unknown"

                if confidence > 77:
                    cv2.putText(img, f"ID: {i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                    self.mark_attendence(i,r,n,d)

                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            draw_boundary(img, faceCascade, 1.1, 10, clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(1)
        if not video_cap.isOpened():
            messagebox.showerror("Error", "Camera not detected. Please check your webcam.")
            return

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
