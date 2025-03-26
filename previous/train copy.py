import os
import cv2
import dlib
import numpy as np
import mysql.connector
from imutils import paths

# Database Connection
conn = mysql.connector.connect(user="root", password="praful", host="localhost", database="face_recognizer", port=3305)
cursor = conn.cursor()

# Load Dlib’s face detector & ResNet face recognition model
detector = dlib.get_frontal_face_detector()
shape_predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
face_rec_model = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")

# Path to dataset folder
dataset_path = "dataset"

def extract_face_embeddings(image_path):
    """Extracts 128D face embeddings from an image"""
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    if len(faces) == 0:
        return None

    for face in faces:
        shape = shape_predictor(gray, face)
        face_descriptor = face_rec_model.compute_face_descriptor(image, shape)
        return np.array(face_descriptor)

def train_model():
    """Processes all images in the dataset and stores embeddings in the database"""
    image_paths = list(paths.list_images(dataset_path))
    
    for image_path in image_paths:
        student_id = os.path.basename(image_path).split(".")[0]  # Extract student ID from filename
        face_embedding = extract_face_embeddings(image_path)

        if face_embedding is not None:
            # Convert numpy array to string
            embedding_str = ",".join(str(x) for x in face_embedding)

            # Store in MySQL (update if already exists)
            cursor.execute("REPLACE INTO student_embeddings (student_id, embedding) VALUES (%s, %s)", (student_id, embedding_str))
            conn.commit()
            print(f"Stored embedding for {student_id}")
        else:
            print(f"Face not detected in {image_path}")

    print("Training completed!")

# Ensure database table exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS student_embeddings (
        student_id VARCHAR(50) PRIMARY KEY,
        embedding TEXT
    )
""")
conn.commit()

if __name__ == "__main__":
    train_model()
    conn.close()
