from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import mysql.connector
import pandas as pd
import os
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.styles import Alignment
from PIL import Image, ImageTk  # ✅ Import for background image

class AttendanceExport:
    def __init__(self, root):
        self.root = root
        self.root.title("Attendance Export System")
        self.root.state('zoomed')
        self.root.configure(bg='#f0f0f0')

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
        frame.place(relx=0.3, rely=0.3, relwidth=0.4, relheight=0.4)

        # Title Label
        title = Label(frame, text="Attendance Export System", font=("Montserrat", 20, "bold"), bg="#ffffff", fg="black")
        title.pack(pady=10)

        # Subject Selection
        Label(frame, text="Enter Subject Name:", font=("Montserrat", 14, "bold"), bg="#ffffff").pack(pady=5)
        self.subject_var = StringVar()
        Entry(frame, textvariable=self.subject_var, font=("Montserrat", 14)).pack(ipady=5, fill=X, padx=50)

        # Date Range Inputs with Date Picker
        Label(frame, text="Select Date Range:", font=("Montserrat", 14, "bold"), bg="#ffffff").pack(pady=5)

        self.from_date = DateEntry(frame, font=("Montserrat", 14), date_pattern='yyyy-MM-dd')
        self.from_date.pack(ipady=5, fill=X, padx=50)

        self.to_date = DateEntry(frame, font=("Montserrat", 14), date_pattern='yyyy-MM-dd')
        self.to_date.pack(ipady=5, fill=X, padx=50)

        # ✅ Styled Export Button
        self.export_btn = Button(frame, text="Export Attendance", font=("Montserrat", 14, "bold"), bg="#4CAF50", fg="white", command=self.export_attendance)
        self.export_btn.pack(pady=15)
        self.export_btn.bind("<Enter>", self.on_hover)
        self.export_btn.bind("<Leave>", self.on_leave)

    def on_hover(self, event):
        event.widget.config(bg="#45a049")

    def on_leave(self, event):
        event.widget.config(bg="#4CAF50")

    def export_attendance(self):
        subject = self.subject_var.get().strip()
        from_date = self.from_date.get_date().strftime('%Y-%m-%d')
        to_date = self.to_date.get_date().strftime('%Y-%m-%d')

        if not subject:
            messagebox.showerror("Error", "Subject Name is required!")
            return

        try:
            conn = mysql.connector.connect(user="root", password="praful", host="localhost", database="face_recognizer", port=3305)
            cursor = conn.cursor()

            # Check if subject table exists
            cursor.execute("SHOW TABLES LIKE %s", (subject,))
            if not cursor.fetchone():
                messagebox.showerror("Error", f"Subject '{subject}' does not exist in the database!")
                return

            # Fetch available date columns
            cursor.execute(f"SHOW COLUMNS FROM `{subject}`")
            table_columns = [col[0] for col in cursor.fetchall()]

            # Generate required date range
            date_columns = pd.date_range(from_date, to_date).strftime('%Y-%m-%d').tolist()
            existing_columns = [f"`{date}`" for date in date_columns if date in table_columns]

            if not existing_columns:
                messagebox.showinfo("Info", "No valid attendance records found for the selected dates.")
                return

            # Fetch attendance data
            query = f"SELECT student_id, name, roll, dep, {', '.join(existing_columns)} FROM `{subject}`"
            cursor.execute(query)
            data = cursor.fetchall()

            if not data:
                messagebox.showinfo("Info", "No attendance records found!")
                return

            # Convert to DataFrame
            columns = ['Student ID', 'Name', 'Roll', 'Department'] + [col.strip('`') for col in existing_columns]
            df = pd.DataFrame(data, columns=columns)

            # Calculate total present days
            df['Total Present'] = df.iloc[:, 4:].apply(lambda row: row.tolist().count('Present'), axis=1)

            # Ensure 'attendance' folder exists
            save_folder = "attendance"
            if not os.path.exists(save_folder):
                os.makedirs(save_folder)

            # Construct filename and save path
            filename = f"{subject}_{from_date}_to_{to_date}.xlsx"
            save_path = os.path.join(save_folder, filename)

            # Save as Excel with formatted columns
            wb = Workbook()
            ws = wb.active
            ws.title = subject

            for r in dataframe_to_rows(df, index=False, header=True):
                ws.append(r)

            # Adjust column width based on content length
            for col in ws.columns:
                max_length = 0
                col_letter = col[0].column_letter  # Get column letter
                for cell in col:
                    try:
                        if cell.value:
                            max_length = max(max_length, len(str(cell.value)))
                    except:
                        pass
                ws.column_dimensions[col_letter].width = max_length + 2

            # Center align headers
            for cell in ws[1]:
                cell.alignment = Alignment(horizontal="center", vertical="center")

            wb.save(save_path)

            # Open file automatically
            os.startfile(save_path)

            messagebox.showinfo("Success", f"Attendance exported successfully and saved in '{save_folder}' folder as {filename}")

        except Exception as e:
            messagebox.showerror("Error", f"Database Error: {str(e)}")
        finally:
            conn.close()

if __name__ == "__main__":
    root = Tk()
    app = AttendanceExport(root)
    root.mainloop()
