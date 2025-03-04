import cv2
import mysql.connector
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="Face Recognition", font=("montserrat", 30, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open("C:/Users/ASUS/OneDrive/Desktop/face_recognition system/college_images/third_image.jpeg").resize((650, 700), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=700)

        img_bottom = Image.open("C:/Users/ASUS/OneDrive/Desktop/face_recognition system/college_images/third_image.jpeg").resize((950, 700), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650, y=55, width=950, height=700)

        b1_1 = Button(f_lbl, text="Face Recognition", cursor="hand2", font=("montserrat", 18, "bold"),
                      bg="lightskyblue", fg="black", command=self.face_recog)
        b1_1.place(x=365, y=620, width=207, height=40)

    def mark_attendance(self, i, r, n, d):
        with open("attendance.csv", "a", newline="\n") as f:
            now = datetime.now()
            f.write(f"{i}, {r}, {n}, {d}, {now.strftime('%H:%M:%S')}, {now.strftime('%d/%m/%Y')}, Present\n")

    def draw_boundary(self, img, classifier, scaleFactor, minNeighbors, clf):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray, scaleFactor, minNeighbors)

        conn = mysql.connector.connect(user="root", password="praful", host="localhost",
                                       database="face_recognizer", port=3305)
        my_cursor = conn.cursor()

        for (x, y, w, h) in features:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            id, predict = clf.predict(gray[y:y + h, x:x + w])
            confidence = int((100 * (1 - predict / 300)))

            my_cursor.execute("SELECT student_id, roll, name, dep FROM student WHERE student_id = %s", (id,))
            student_data = my_cursor.fetchone()
            if student_data:
                i, r, n, d = student_data
                self.mark_attendance(i, r, n, d)

        conn.close()
        return img

    def face_recog(self):
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)
        if not video_cap.isOpened():
            messagebox.showerror("Error", "Camera not detected. Please check your webcam.")
            return

        while True:
            ret, img = video_cap.read()
            img = self.draw_boundary(img, faceCascade, 1.1, 10, clf)
            cv2.imshow("Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
