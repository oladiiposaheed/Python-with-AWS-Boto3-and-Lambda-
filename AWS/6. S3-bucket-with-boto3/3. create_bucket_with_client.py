import boto3

client = boto3.client('s3')

response = client.create_bucket(
    Bucket = 'bucket-boto3',
    ACL = 'private',
)
print(response)