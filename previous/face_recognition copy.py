from tkinter import *
from tkinter import messagebox
import mysql.connector
import cv2
import dlib
import numpy as np

# Database Connection
conn = mysql.connector.connect(user="root", password="praful", host="localhost", database="face_recognizer", port=3305)
cursor = conn.cursor()

# Load Dlib’s models
detector = dlib.get_frontal_face_detector()
shape_predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
face_rec_model = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")

def extract_face_embedding(image):
    """Extracts 128D face embedding from a frame"""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    if len(faces) == 0:
        return None

    for face in faces:
        shape = shape_predictor(gray, face)
        face_descriptor = face_rec_model.compute_face_descriptor(image, shape)
        return np.array(face_descriptor)

def cosine_similarity(vec1, vec2):
    """Computes cosine similarity between two face embeddings"""
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def recognize_face(frame):
    """Compares detected face with database and returns the closest match"""
    face_embedding = extract_face_embedding(frame)
    if face_embedding is None:
        return None, None, None

    # Fetch all stored embeddings from the database
    cursor.execute("SELECT student_id, embedding FROM student_embeddings")
    records = cursor.fetchall()

    best_match_id = None
    best_match_score = -1  # Higher is better

    for student_id, embedding_str in records:
        stored_embedding = np.array([float(x) for x in embedding_str.split(",")])
        similarity = cosine_similarity(face_embedding, stored_embedding)

        if similarity > best_match_score:  # Update best match
            best_match_score = similarity
            best_match_id = student_id

    # Confidence threshold
    if best_match_score > 0.4:
        cursor.execute("SELECT student_id, name, roll, dep FROM student WHERE student_id = %s", (best_match_id,))
        result = cursor.fetchone()
        return result if result else (None, None, None)
    else:
        return None, None, None

def start_face_recognition():
    """Runs face recognition in real-time"""
    video_cap = cv2.VideoCapture(1)
    if not video_cap.isOpened():
        messagebox.showerror("Error", "Camera not detected.")
        return

    while True:
        ret, frame = video_cap.read()
        student_id, name, roll = recognize_face(frame)

        if student_id:
            cv2.putText(frame, f"ID: {student_id}, Name: {name}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else:
            cv2.putText(frame, "Unknown", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow("Face Recognition", frame)
        if cv2.waitKey(1) == 13:  # Press 'Enter' to exit
            break

    video_cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    start_face_recognition()
