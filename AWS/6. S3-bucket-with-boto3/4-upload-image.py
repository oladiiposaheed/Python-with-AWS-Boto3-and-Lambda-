import boto3

client = boto3.client('s3')

with open('AWS/S3-bucket-with-boto3/img5.png', 'rb') as f:
    data = f.read()

response = client.put_object(
    ACL = 'private',
    Bucket = 'bucket-boto3',
    Body = data,
    Key= 'img5.png'
)  
print(response)