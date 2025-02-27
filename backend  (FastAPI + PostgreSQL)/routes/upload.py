import boto3
import pandas as pd
from fastapi import APIRouter, UploadFile, File, HTTPException
from services.file_service import process_file

router = APIRouter()

S3_BUCKET = "childcare-data"
s3_client = boto3.client("s3")

@router.post("/")
async def upload_child_data(file: UploadFile = File(...)):
    try:
        s3_client.upload_fileobj(file.file, S3_BUCKET, file.filename)
        process_file(file.filename)
        return {"message": "File uploaded & processed successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))