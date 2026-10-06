# University Student CRUD API

This project implements the Assignment 1 FastAPI Student CRUD application.

## Requirements

- FastAPI
- Uvicorn
- Pydantic validation
- Local in-memory storage
- No database

## Project Structure

```text
student-crud/
├── main.py
├── models/
│   ├── __init__.py
│   └── student_model.py
├── routes/
│   ├── __init__.py
│   └── student_routes.py
├── controllers/
│   ├── __init__.py
│   └── student_controller.py
├── requirements.txt
└── README.md
```

## Installation

Open PowerShell in this folder:

```powershell
python -m pip install -r requirements.txt
```

## Run

```powershell
uvicorn main:app --reload
```

Open:

http://127.0.0.1:8000/docs

## Five Required APIs

1. POST `/students` - Create Student - 201
2. GET `/students` - Read All Students - 200
3. GET `/students/{id}` - Read Student by ID - 200
4. PUT `/students/{id}` - Update Student - 200
5. DELETE `/students/{id}` - Delete Student - 204

## Sample Students

Create at least five students using Swagger. Example:

```json
{
  "name": "Rahul Patel",
  "email": "rahul@example.com",
  "course": "B.Tech Computer Engineering",
  "semester": 5
}
```

Other suggested records:

```json
{
  "name": "Diya Rana",
  "email": "diya@example.com",
  "course": "B.Sc Information Technology",
  "semester": 6
}
```

```json
{
  "name": "Aarav Shah",
  "email": "aarav@example.com",
  "course": "B.Tech Information Technology",
  "semester": 4
}
```

```json
{
  "name": "Neha Patel",
  "email": "neha@example.com",
  "course": "BCA",
  "semester": 3
}
```

```json
{
  "name": "Karan Mehta",
  "email": "karan@example.com",
  "course": "MCA",
  "semester": 2
}
```

## Required Testing

Test these cases in `/docs`:

- Valid create -> 201
- Invalid data -> 422
- Get all -> 200
- Existing ID -> 200
- Non-existing ID -> 404
- Update existing -> 200
- Update non-existing -> 404
- Delete existing -> 204
- Delete non-existing -> 404
- Retrieve deleted student -> 404

## Important

Data is stored only in Python memory. Restarting the application clears the student records.

## API Endpoints

- POST /students - Create student
- GET /students - Get all students
- GET /students/{id} - Get student by ID
- PUT /students/{id} - Update student
- DELETE /students/{id} - Delete student
