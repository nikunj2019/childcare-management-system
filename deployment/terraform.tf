provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "childcare_data" {
  bucket = "childcare-data-bucket"
}

resource "aws_lambda_function" "backend" {
  function_name = "childcare-api"
  role          = aws_iam_role.lambda_role.arn
  runtime       = "python3.9"
  handler       = "main.handler"
  filename      = "backend/function.zip"
}

resource "aws_rds_instance" "database" {
  engine         = "postgres"
  instance_class = "db.t3.micro"
  allocated_storage = 20
  username       = "admin"
  password       = "password"
}