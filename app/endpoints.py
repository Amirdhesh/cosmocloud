from fastapi import APIRouter, HTTPException
from schema import Student, UpdateStudent
from crud import crud

routes = APIRouter()


@routes.post("/students", status_code=201)
def create_student(student_detail: Student):
    return crud.create(student_detail)


@routes.get("/students")
def list_students(country: str, age: int):
    return crud.list(country, age)


@routes.get("/students/{id}")
def fetch_student(id: int):
    student = crud.fetch(id)
    if student:
        return student
    else:
        raise HTTPException(status_code=404, detail="Student not found")


@routes.patch("/students/{id}", status_code=204)
def update_student(id: str, updates: UpdateStudent):
    return crud.update(id, updates)


@routes.delete("/students/{id}", status_code=200)
def delete_student(id: str):
    return crud.delete(id)
