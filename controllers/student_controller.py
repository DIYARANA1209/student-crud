from fastapi import HTTPException
from models.student_model import Student, StudentCreate

# Local in-memory storage only. No database is used.
students: list[Student] = []
next_id = 1


def create_student(student_data: StudentCreate) -> Student:
    global next_id

    student = Student(
        id=next_id,
        name=student_data.name,
        email=student_data.email,
        course=student_data.course,
        semester=student_data.semester,
    )
    students.append(student)
    next_id += 1
    return student


def get_all_students() -> list[Student]:
    return students


def get_student_by_id(student_id: int) -> Student:
    for student in students:
        if student.id == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")


def update_student(student_id: int, student_data: StudentCreate) -> Student:
    for index, student in enumerate(students):
        if student.id == student_id:
            updated_student = Student(
                id=student_id,
                name=student_data.name,
                email=student_data.email,
                course=student_data.course,
                semester=student_data.semester,
            )
            students[index] = updated_student
            return updated_student

    raise HTTPException(status_code=404, detail="Student not found")


def delete_student(student_id: int) -> None:
    for index, student in enumerate(students):
        if student.id == student_id:
            students.pop(index)
            return

    raise HTTPException(status_code=404, detail="Student not found")
