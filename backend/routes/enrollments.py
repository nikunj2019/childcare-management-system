from fastapi import APIRouter, HTTPException
from services.db_service import get_children, add_child

router = APIRouter()

@router.get("/")
async def list_enrollments():
    return get_children()

@router.post("/")
async def create_enrollment(child_data: dict):
    success = add_child(child_data)
    if not success:
        raise HTTPException(status_code=400, detail="Failed to add child")
    return {"message": "Child enrolled successfully!"}