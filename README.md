# 🎭 Face Recognition-Based Student Attendance System

## 📌 Overview
The **Face Recognition-Based Student Attendance System** is an AI-powered solution that automates attendance tracking using **OpenCV**, **Deep Learning**, and **MySQL**. It efficiently recognizes students' faces, marks attendance in real-time, and stores data securely in a database.

## ✨ Features
✅ **Real-Time Face Recognition** – Detects and recognizes students' faces using OpenCV.  
✅ **Automated Attendance Marking** – Updates attendance records in the database instantly.  
✅ **User-Friendly Interface** – Interactive **Tkinter**-based GUI for easy navigation.  
✅ **Attendance Export** – Generate attendance reports in **Excel (.xlsx)** format.  
✅ **Date-wise Filtering** – Filter attendance records based on custom date ranges.  
✅ **Secure Database** – Stores student details and attendance data in **MySQL**.  

---

## 🚀 Tech Stack
| **Technology** | **Purpose** |
|---------------|------------|
| **Python** | Main programming language |
| **OpenCV** | Face detection and recognition |
| **Deep Learning** | Improving face recognition accuracy |
| **Tkinter** | GUI development |
| **MySQL** | Database management |
| **Pandas** | Data handling & processing |
| **OpenPyXL** | Excel file management |

---

## 📂 Folder Structure
```
📁 Face_Recognition_Attendance_System
├── 📂 college_images         # Images used in the project
├── 📂 attendance             # Folder where attendance records are saved
├── 📂 data                   # Grayscale images for training
├── 📄 main.py                # Main application file
├── 📄 train.py               # Training module
├── 📄 face_recognition.py    # Face recognition logic
├── 📄 student.py             # Student management module
├── 📄 developer.py           # Developer info section
├── 📄 help.py                # Help section
├── 📄 login_signup.py        # Authentication module
├── 📄 README.md              # Project documentation

```


---

## 🛠️ Setup & Installation

### ✅ Prerequisites
Before setting up the project, make sure you have:
- **Python (≥3.8)**
- **MySQL Server**
- **pip (Python package manager)**

### 🔽 Step 1: Clone the Repository
```sh
git clone https://github.com/praphoolrathore/face_recognition_system.git
cd face_recognition_system
```
### 📦 Step 2: Install Dependencies
```sh
pip install -r requirements.txt
```

### 🛢️ Step 3: Set Up MySQL Database
Open MySQL Workbench or the command line.

Create a new database:
```sql
CREATE DATABASE face_recognizer;
```
Import the provided SQL file:
```sh
mysql -u root -p face_recognizer < database.sql
```

### ▶️ Step 4: Run the Application
```sh
python main.py
```


### 🎥 Project Demonstration

 Video Demonstration
[![Watch the Demo](https://img.youtube.com/vi/rTaP-dTynvI/maxresdefault.jpg)](https://youtu.be/rTaP-dTynvI)



### 🔮 Future Enhancements

🚀 Deep Learning Model Integration – Enhance accuracy with CNN models.
☁️ Cloud-Based Storage – Store attendance data securely on cloud platforms.
📱 Mobile App Support – Enable attendance marking via mobile devices.
📈 Real-Time Analytics – Provide insights and trends on student attendance.

### 🤝 Contribution

Contributions are welcome! To contribute:

Fork the repository.
Create a feature branch (git checkout -b feature-branch).
Commit your changes (git commit -m "Add new feature").
Push to the branch (git push origin feature-branch).
Open a Pull Request.


### 📧 Contact & Support

For any queries, reach out to:
👤 Praphool Rathore
📩 Email: praphoolrathore2003@gmail.com
🔗 LinkedIn: [Connect with me](www.linkedin.com/in/praphool-rathore-b67ba82a8)
🌍 GitHub: [Project Repository](https://github.com/praphoolrathore/face_recognition_system)



