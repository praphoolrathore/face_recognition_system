from tkinter import *
from tkinter import messagebox
import os
import cv2
import numpy as np
from PIL import Image

class Train:
    def __init__(self, root):
        self.root = root  
        self.root.withdraw()  # Hide main window immediately

        # Show a small progress window
        self.progress_window = Toplevel()
        self.progress_window.geometry("400x200+600+300")
        self.progress_window.title("Training Data")
        self.progress_window.config(bg="white")

        Label(self.progress_window, text="Training in Progress...", font=("montserrat", 15, "bold"), bg="white").pack(pady=30)
        self.progress_label = Label(self.progress_window, text="Processing...", font=("montserrat", 12), bg="white", fg="black")
        self.progress_label.pack()

        self.root.after(100, self.train_classifier)  # Start training after 100ms

    def train_classifier(self):
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')  # Convert to grayscale
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)

        ids = np.array(ids)

        # Train classifier
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")

        # Destroy progress window after completion
        self.progress_window.destroy()

        # Show completion message
        messagebox.showinfo("Result", "Training datasets completed!")

        # Close the root application
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
