from tkinter import *
from tkinter import messagebox
import os
import cv2
import numpy as np
from PIL import Image
import threading
import time

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

        # Start training in a separate thread
        self.root.after(100, self.start_training)

    def start_training(self):
        threading.Thread(target=self.train_classifier, daemon=True).start()

    def train_classifier(self):
        data_dir = "data"
        if not os.path.exists(data_dir):
            messagebox.showerror("Error", "Data folder not found!")
            self.progress_window.destroy()
            self.root.destroy()
            return

        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            try:
                img = Image.open(image).convert('L')  # Convert to grayscale
                imageNp = np.array(img, 'uint8')
                id = int(os.path.splitext(os.path.basename(image))[0].split('.')[1])
                
                faces.append(imageNp)
                ids.append(id)
            except (IndexError, ValueError):
                print(f"Skipping invalid file: {image}")
                continue

        if len(faces) == 0 or len(ids) == 0:
            messagebox.showerror("Error", "No valid training data found!")
            self.progress_window.destroy()
            self.root.destroy()
            return

        ids = np.array(ids)

        # Train classifier
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)

        filename = f"classifier_{int(time.time())}.xml"
        clf.write(filename)

        # Destroy progress window after completion
        self.progress_window.destroy()

        # Show completion message
        messagebox.showinfo("Result", f"Training completed! Model saved as {filename}")

        # Close the root application
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
