# AWS Lambda–S3 File Ingestion Pipeline (Python + Boto3)
### 📌 Project Overview

This project demonstrates a serverless file ingestion pipeline built using AWS Lambda, Amazon S3, and Python (boto3).
The goal of the project is to securely and efficiently upload files from a local environment to an S3 bucket via an AWS Lambda function, rather than writing directly to S3.

This architecture is commonly used in data engineering pipelines to enforce validation, logging, transformation, and access control before data is persisted.

### 🏗️ Architecture
Local Python Script   ----> AWS Lambda Function ----->  Amazon S3 Bucket

### 🔧 Technologies Used

AWS S3 – Object storage for ingested files

AWS Lambda – Serverless compute for file ingestion

Python 3.x – Core programming language

boto3 – AWS SDK for Python

IAM Roles & Policies – Secure access control


