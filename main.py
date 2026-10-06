from fastapi import FastAPI
from routes.student_routes import router as student_router

app = FastAPI(
    title="University Student CRUD API",
    description="FastAPI CRUD application using local in-memory storage.",
    version="1.0.0"
)

app.include_router(student_router)

@app.get("/")
def root():
    return {"message": "University Student CRUD API is running"}
