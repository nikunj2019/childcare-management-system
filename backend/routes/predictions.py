from fastapi import APIRouter
from services.prediction_service import predict_availability

router = APIRouter()

@router.get("/")
async def get_predictions():
    return predict_availability()