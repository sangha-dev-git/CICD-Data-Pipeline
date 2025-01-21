import boto3
import os

def deploy_to_s3(bucket_name, file_path, s3_key):
    s3 = boto3.client('s3')
    s3.upload_file(file_path, bucket_name, s3_key)
    print(f"Deployed {file_path} to s3://{bucket_name}/{s3_key}")

if __name__ == "__main__":
    bucket_name = os.getenv("S3_BUCKET_NAME")
    file_path = "artifact.zip"  # Example artifact
    s3_key = "deployments/artifact.zip"
    
    deploy_to_s3(bucket_name, file_path, s3_key)
