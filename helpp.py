from tkinter import *
from PIL import Image, ImageTk

class Help:
    def __init__(self, root):
        self.root = root

        # Get screen width and height dynamically
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        # Set window size dynamically
        self.root.geometry(f"{self.screen_width}x{self.screen_height}+-10+0")
        self.root.title("Face Recognition System")

        # **Dynamic Sizing Variables**
        self.title_height = int(self.screen_height * 0.07)  # 7% of screen height for title bar
        self.label_font_size = max(12, int(self.screen_width * 0.01))  # Adjust font size dynamically

        # **Title Bar**
        title_lbl = Label(self.root, text="Help Desk",
                          font=("Montserrat", int(self.screen_width * 0.018), "bold"),
                          bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=self.screen_width, height=self.title_height)

        # **Background Image (Scaled Dynamically)**
        img_top = Image.open("college_images/attendence_bg.jpg")
        img_top = img_top.resize((self.screen_width, self.screen_height - self.title_height), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        # **Display Background Image**
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=self.title_height, width=self.screen_width, height=self.screen_height - self.title_height)

        # **Email Labels (Positioned Dynamically)**
        email_start_y = int(self.screen_height * 0.30)  # Start position for emails (30% of screen height)
        email_spacing = int(self.screen_height * 0.07)  # 7% of screen height as spacing

        emails = [
            "Email: praphoolrathore2003@gmail.com",
            "Email: harshvardhans809@gmail.com",
            "Email: pranavmakwanaop@gmail.com"
        ]

        for i, email in enumerate(emails):
            Label(f_lbl, text=email,
                  font=("Montserrat", self.label_font_size, "bold"),
                  bg="white").place(x=int(self.screen_width * 0.35),
                                    y=email_start_y + i * email_spacing)

if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
