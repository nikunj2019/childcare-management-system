from fastapi import FastAPI
from routes import enrollments, upload, predictions

app = FastAPI(title="Childcare Management API")

# Register Routes
app.include_router(enrollments.router, prefix="/enrollments")
app.include_router(upload.router, prefix="/upload")
app.include_router(predictions.router, prefix="/predict")

@app.get("/")
def root():
    return {"message": "Childcare Management API is running!"}

# Run: uvicorn main:app --reload