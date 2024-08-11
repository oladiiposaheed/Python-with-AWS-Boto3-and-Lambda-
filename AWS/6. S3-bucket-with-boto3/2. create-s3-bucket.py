import boto3

#Create resource
bucket = boto3.resource('s3')
response = bucket.create_bucket(
    Bucket = 'boto-3-bucket-1',
    ACL = 'public-read-write',
)
print(response)