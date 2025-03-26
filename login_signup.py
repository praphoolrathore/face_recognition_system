from tkinter import *
from tkinter import messagebox
import mysql.connector
import bcrypt
import os
import re

class LoginSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition - Login & Signup")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f0f0")

        self.username_var = StringVar()
        self.email_var = StringVar()
        self.password_var = StringVar()

        self.create_login_ui()

    def is_valid_email(self, email):
        return re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email)

    def is_valid_password(self, password):
        return len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isalpha() for char in password)

    def create_login_ui(self):
        """Create Login UI"""
        self.clear_frame()
        frame = Frame(self.root, bg="#1a1a1a", bd=3, relief=RIDGE)
        frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=350, height=350)

        Label(frame, text="Login", font=("Orbitron", 18, "bold"), bg="#1a1a1a", fg="#00ffcc").pack(pady=20)

        Label(frame, text="Username:", bg="#1a1a1a", fg="#00ffcc", font=("Orbitron", 12)).pack()
        Entry(frame, textvariable=self.username_var, font=("Orbitron", 12), bd=2, bg="#262626", fg="#00ffcc", insertbackground="#00ffcc").pack(pady=5, ipadx=10)

        Label(frame, text="Password:", bg="#1a1a1a", fg="#00ffcc", font=("Orbitron", 12)).pack()
        Entry(frame, textvariable=self.password_var, font=("Orbitron", 12), bd=2, bg="#262626", fg="#00ffcc", show="*", insertbackground="#00ffcc").pack(pady=5, ipadx=10)

        Button(frame, text="Login", font=("Orbitron", 12, "bold"), bg="#00ffcc", fg="#1a1a1a", command=self.login_user).pack(pady=10)
        Button(frame, text="Create Account", font=("Orbitron", 10), fg="#00ffcc", bg="#1a1a1a", command=self.create_signup_ui).pack()
    
    def create_signup_ui(self):
        """Create Signup UI"""
        self.clear_frame()
        frame = Frame(self.root, bg="#1a1a1a", bd=3, relief=RIDGE)
        frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=350, height=420)

        Label(frame, text="Sign Up", font=("Orbitron", 18, "bold"), bg="#1a1a1a", fg="#00ffcc").pack(pady=20)

        Label(frame, text="Username:", bg="#1a1a1a", fg="#00ffcc", font=("Orbitron", 12)).pack()
        Entry(frame, textvariable=self.username_var, font=("Orbitron", 12), bd=2, bg="#262626", fg="#00ffcc", insertbackground="#00ffcc").pack(pady=5, ipadx=10)

        Label(frame, text="Email:", bg="#1a1a1a", fg="#00ffcc", font=("Orbitron", 12)).pack()
        Entry(frame, textvariable=self.email_var, font=("Orbitron", 12), bd=2, bg="#262626", fg="#00ffcc", insertbackground="#00ffcc").pack(pady=5, ipadx=10)

        Label(frame, text="Password:", bg="#1a1a1a", fg="#00ffcc", font=("Orbitron", 12)).pack()
        Entry(frame, textvariable=self.password_var, font=("Orbitron", 12), bd=2, bg="#262626", fg="#00ffcc", show="*", insertbackground="#00ffcc").pack(pady=5, ipadx=10)

        Button(frame, text="Register", font=("Orbitron", 12, "bold"), bg="#00ffcc", fg="#1a1a1a", command=self.register_user).pack(pady=10)
        Button(frame, text="Back to Login", font=("Orbitron", 10), fg="#00ffcc", bg="#1a1a1a", command=self.create_login_ui).pack()

    def register_user(self):
        """Register New User"""
        username = self.username_var.get().strip()
        email = self.email_var.get().strip()
        password = self.password_var.get().strip()

        if not username or not email or not password:
            messagebox.showerror("Error", "All fields are required!")
            return
        
        if not self.is_valid_email(email):
            messagebox.showerror("Error", "Invalid email format!")
            return

        if not self.is_valid_password(password):
            messagebox.showerror("Error", "Password must be at least 8 characters long and contain both letters and numbers!")
            return

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        try:
            conn = mysql.connector.connect(user="root", password="praful", host="localhost", database="face_recognizer", port=3305)
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
            if cursor.fetchone():
                messagebox.showerror("Error", "Username already exists! Choose another.")
                return

            cursor.execute("INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)", 
                           (username, email, hashed_password.decode('utf-8')))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Account created successfully!")
            self.create_login_ui()

        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error: {str(e)}")

    def login_user(self):
        """Authenticate User"""
        username = self.username_var.get()
        password = self.password_var.get()

        if not username or not password:
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            conn = mysql.connector.connect(user="root", password="praful", host="localhost", database="face_recognizer", port=3305)
            cursor = conn.cursor()
            cursor.execute("SELECT password_hash FROM users WHERE username=%s", (username,))
            result = cursor.fetchone()
            conn.close()

            if result and bcrypt.checkpw(password.encode('utf-8'), result[0].encode('utf-8')):
                messagebox.showinfo("Success", "Login Successful!")
                self.root.destroy()
                os.system("python main.py")  # ✅ Open Main Face Recognition App
            else:
                messagebox.showerror("Error", "Invalid Username or Password!")

        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error: {str(e)}")


    def clear_frame(self):
        """Clear Frame for Switching UI"""
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = Tk()
    app = LoginSystem(root)
    root.mainloop()
