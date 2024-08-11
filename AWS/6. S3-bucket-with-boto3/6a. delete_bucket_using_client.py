import boto3

client = boto3.client('s3')
bucket_name = 'docexamplebucket50'
client.delete_bucket(Bucket= bucket_name)
print('S3 Bucket has been deleted')