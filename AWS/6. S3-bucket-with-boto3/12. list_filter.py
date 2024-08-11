import boto3

BUCKET_NAME = 'boketdjango'

s3_resource = boto3.resource('s3')

s3_bucket = s3_resource.Bucket(BUCKET_NAME)

print('List Filtered File')

for obj in s3_resource.objects.filter(Prefix='AWS/S3-bucket-with-boto3/user.txt'):
    print(obj.key)