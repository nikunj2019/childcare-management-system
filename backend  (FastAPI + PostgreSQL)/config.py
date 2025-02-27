import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
AWS_S3_BUCKET = os.getenv("AWS_S3_BUCKET")