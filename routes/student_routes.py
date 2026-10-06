from fastapi import APIRouter, Response, status
from models.student_model import Student, StudentCreate
from controllers.student_controller import (
    create_student,
    get_all_students,
    get_student_by_id,
    update_student,
    delete_student,
)

router = APIRouter(prefix="/students", tags=["Students"])


@router.post("", response_model=Student, status_code=status.HTTP_201_CREATED)
def create_student_api(student: StudentCreate):
    return create_student(student)


@router.get("", response_model=list[Student], status_code=status.HTTP_200_OK)
def get_all_students_api():
    return get_all_students()


@router.get("/{student_id}", response_model=Student, status_code=status.HTTP_200_OK)
def get_student_api(student_id: int):
    return get_student_by_id(student_id)


@router.put("/{student_id}", response_model=Student, status_code=status.HTTP_200_OK)
def update_student_api(student_id: int, student: StudentCreate):
    return update_student(student_id, student)


@router.delete("/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student_api(student_id: int):
    delete_student(student_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
