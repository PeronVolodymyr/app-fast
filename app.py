from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

import uvicorn

app = FastAPI()


class Students(BaseModel):
    id: int
    name: str
    chair: str
    group: int


class CreateStudent(BaseModel):
    name: str
    chair: str
    group: int


class EditStudent(BaseModel):
    name: str
    chair: str
    group: int


students = [
    {
        'id': 1,
        'name': 'Volodymyr Peron',
        'chair': 'IFTKN',
        'group': 443
    },
    {
        'id': 2,
        'name': 'Ivan Ivanov',
        'chair': 'Computer Science',
        'group': 223
    }
]

my_students: List[Students] = students

@app.get("/students", response_model=List[Students])
def read_word():
    return my_students


@app.get("/student/{student_id}", response_model=Students)
def save_student(student_id: int):
    student = list(filter(lambda t: t['id'] == student_id, my_students))
    return student[0]


@app.post("/create/student", response_model=Students, status_code=201)
def create_word(w: CreateStudent):
    student = {
        'id': 44,
        'name': w.name,
        'chair': w.chair,
        'group': w.group
    }
    students.append(student)
    return student


@app.put("/students/{student_id}", response_model=Students)
def edit_students(student_id, w: EditStudent):
    new_student = {
        'id': student_id,
        'name': w.name,
        'chair': w.chair,
        'group': w.group
    }
    return new_student


@app.delete("/students/{student_id}", response_model=List[Students], status_code=201)
def delete_students(student_id: int):
    student = list(filter(lambda t: t['id'] != student_id, my_students))
    return student
