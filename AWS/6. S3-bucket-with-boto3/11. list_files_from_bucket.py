import boto3

BUCKET_NAME = 'boketdjango'

s3_resource = boto3.resource('s3')

s3_bucket = s3_resource.Bucket(BUCKET_NAME)
print('List bucket files or Objects')

for obj in s3_bucket.objects.all():
    print(obj.key)