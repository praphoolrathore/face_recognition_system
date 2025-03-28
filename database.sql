-- Create the database
CREATE DATABASE IF NOT EXISTS face_recognizer;
USE face_recognizer;

-- Create the student table
CREATE TABLE IF NOT EXISTS student (
    Dep VARCHAR(45),
    course VARCHAR(45),
    Year VARCHAR(45),
    Semester VARCHAR(45),
    Student_id VARCHAR(45) NOT NULL PRIMARY KEY,
    Name VARCHAR(45),
    Division VARCHAR(45),
    Roll VARCHAR(45),
    Gender VARCHAR(45),
    Dob VARCHAR(45),
    Email VARCHAR(45),
    Phone VARCHAR(45),
    Address VARCHAR(45),
    Teacher VARCHAR(45),
    PhotoSample VARCHAR(45)
);

-- Sample data insertion (optional)
INSERT INTO student (Dep, course, Year, Semester, Student_id, Name, Division, Roll, Gender, Dob, Email, Phone, Address, Teacher, PhotoSample) 
VALUES 
('CSE', 'B.Tech', '3rd', '6th', 'S101', 'John Doe', 'A', '23', 'Male', '2002-05-14', 'johndoe@email.com', '9876543210', '123 Street, City', 'Prof. Smith', 'john_photo.jpg'),
('ECE', 'B.Tech', '2nd', '4th', 'S102', 'Jane Doe', 'B', '45', 'Female', '2003-08-21', 'janedoe@email.com', '8765432109', '456 Avenue, City', 'Prof. Johnson', 'jane_photo.jpg');
