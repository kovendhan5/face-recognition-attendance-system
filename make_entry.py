import face_recognition
import numpy as np
import pandas as pd

students_csv_path = './database/students.csv'

def make_student_entry_to_database(image_path: str, student_id: int, university: str, first_name: str, middle_name: str, last_name: str, semester: int, course: str) -> None:
    '''
    Gets information of student and:
        -> Adds entry to students.csv
        -> Adds face encoding to database/face_encodings directory
    '''
    students_df = pd.read_csv(students_csv_path)
    students_df.loc[len(students_df)] = [student_id, university, first_name, middle_name, last_name, semester, course]
    students_df.to_csv(students_csv_path, index=False)

    image = face_recognition.load_image_file(image_path)
    encoding = face_recognition.face_encodings(image, model = 'large')[0]
    np.save(f'./database/face_encodings/{student_id}-{university}', encoding)

make_student_entry_to_database(
    image_path = './pp.jpg',
    student_id = 23140750, 
    university = 'BCU', 
    first_name = 'Sudeep', 
    middle_name = '', 
    last_name = 'Fullel', 
    semester = 3, 
    course = 'Bsc (Hons) Computer and Data Science'
)