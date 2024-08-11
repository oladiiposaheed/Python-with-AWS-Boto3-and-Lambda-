import boto3
from botocore.exceptions import ClientError

def check_encryption():
    s3_client = boto3.client('s3')

    try:
        response = s3_client.get_bucket_encryption(
            Bucket = 's3bucket-1000'
        )
        print(response)
    except ClientError as e:
        print('No encryption is available in this bucket')

check_encryption()