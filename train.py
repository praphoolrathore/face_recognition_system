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

        # **Check if folder exists**
        if not os.path.exists(data_dir):
            messagebox.showerror("Error", "Data folder not found!")
            self.progress_window.destroy()
            self.root.destroy()
            return
        
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith(('.jpg', '.png', '.jpeg'))]

        if len(path) == 0:
            messagebox.showerror("Error", "No images found in the data folder!")
            self.progress_window.destroy()
            self.root.destroy()
            return

        faces = []
        ids = []

        for image in path:
            try:
                img = Image.open(image).convert('L')  # Convert to grayscale
                imageNp = np.array(img, 'uint8')

                # **Extract ID safely**
                filename = os.path.basename(image)
                id_parts = filename.split('.')
                if len(id_parts) < 2 or not id_parts[1].isdigit():
                    print(f"Skipping invalid file: {filename}")
                    continue

                id = int(id_parts[1])

                faces.append(imageNp)
                ids.append(id)
            except Exception as e:
                print(f"Error processing image {image}: {e}")

        if len(faces) < 2:
            messagebox.showerror("Error", "Not enough training data. Add more face images!")
            self.progress_window.destroy()
            self.root.destroy()
            return

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
