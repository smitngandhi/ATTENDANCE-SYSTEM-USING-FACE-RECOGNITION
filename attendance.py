import cv2
import face_recognition
import numpy as np
import csv
from datetime import datetime

video_capture = cv2.VideoCapture(0)

known_face_encodings = []
known_face_names = []

# Load known face images and encodings
image_paths = [
    'C:/Users/Smit/Desktop/5th sem/AI/Face_recognition/Test_Photos/Diya.jpg',
    'C:/Users/Smit/Desktop/5th sem/AI/Face_recognition/Test_Photos/Manan.jpg',
    'C:/Users/Smit/Desktop/5th sem/AI/Face_recognition/Test_Photos/Prachi.jpg',
    'C:/Users/Smit/Desktop/5th sem/AI/Face_recognition/Test_Photos/Smit.jpg',
    'C:/Users/Smit/Desktop/5th sem/AI/Face_recognition/Test_Photos/Nikhil.jpg',
    'C:/Users/Smit/Desktop/5th sem/AI/Face_recognition/Test_Photos/Rachana.jpg', 
    'C:/Users/Smit/Desktop/5th sem/AI/Face_recognition/Test_Photos/Tisha.jpg'
    'C:/Users/Smit/Desktop/5th sem/AI/Face_recognition/Test_Photos/Archana.jpg'
    'C:/Users/Smit/Desktop/5th sem/AI/Face_recognition/Test_Photos/Ronak.jpg'
    'C:/Users/Smit/Desktop/5th sem/AI/Face_recognition/Test_Photos/Ashutosh.jpg'
    'C:/Users/Smit/Desktop/5th sem/AI/Face_recognition/Test_Photos/Harsh.jpg'
    'C:/Users/Smit/Desktop/5th sem/AI/Face_recognition/Test_Photos/Jalay.jpg'
    'C:/Users/Smit/Desktop/5th sem/AI/Face_recognition/Test_Photos/Karma.jpg'
    'C:/Users/Smit/Desktop/5th sem/AI/Face_recognition/Test_Photos/Kaushal.jpg'
    'C:/Users/Smit/Desktop/5th sem/AI/Face_recognition/Test_Photos/Kshitij.jpg'
    'C:/Users/Smit/Desktop/5th sem/AI/Face_recognition/Test_Photos/Meet.jpg'
    # Add paths for other known faces here
]

for image_path in image_paths:
    image = face_recognition.load_image_file(image_path)
    face_encoding = face_recognition.face_encodings(image)[0]  # Assuming only one face per image
    known_face_encodings.append(face_encoding)

    # Extract name from filename (assuming format like "Name.jpg")
    name = image_path.split('/')[-1].split('.')[0]
    known_face_names.append(name)

students = known_face_names.copy()

face_locations = []
face_encodings = []
face_names = []
s = True  # Flag to control face detection frequency

now = datetime.now()
current_date = now.strftime('%Y-%m-%d')

attendance_file = open(current_date + '.csv', 'w+', newline='')
writer = csv.writer(attendance_file)

while True:
    ret, video_frame = video_capture.read()
    # Resize for better performance (adjust fx and fy as needed)
    # small_frame = cv2.resize(video_frame, (0, 0))
    # rgb_small_frame = small_frame[:, :, ::-1]  # Convert BGR to RGB

    if s:  # Detect faces only occasionally for efficiency
        face_locations = face_recognition.face_locations(video_frame)
        face_encodings = face_recognition.face_encodings(video_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = ""
            face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distance)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

            if name in known_face_names:
                if name in students:
                    students.remove(name)
                    current_time = now.strftime('%H-%M-%S')
                    writer.writerow([name, current_time])
    #import dataset from cv2 to detect face muscles
    col = cv2.cvtColor(video_frame,cv2.COLOR_BGR2GRAY)
    
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Draw a rectangle around the face
        cv2.rectangle(video_frame, (left, top), (right, bottom), (0, 255, 0), 2)  # Blue rectangle, thickness 2

        # Add a label with the name below the face
        cv2.putText(video_frame, name, (left + 3, bottom - 6), cv2.FONT_HERSHEY_TRIPLEX, 1, (255,255,255), 2)  #convert to black and white
    cv2.imshow("AttendanceSystem",video_frame)
    if cv2.waitKey(10) == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()
attendance_file.close()
