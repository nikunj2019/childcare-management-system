import boto3
import os

S3_BUCKET = os.getenv("AWS_S3_BUCKET")
s3_client = boto3.client("s3")

def upload_to_s3(file_name, file_data):
    """ Upload file to AWS S3 """
    try:
        s3_client.put_object(Bucket=S3_BUCKET, Key=file_name, Body=file_data)
        return f"https://{S3_BUCKET}.s3.amazonaws.com/{file_name}"
    except Exception as e:
        print(f"Error uploading to S3: {str(e)}")
        return None