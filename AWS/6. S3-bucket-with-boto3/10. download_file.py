import boto3

BUCKET_NAME = 'boketdjango'

s3_resource = boto3.resource('s3')
s3_object = s3_resource.Object(BUCKET_NAME, 'AWS/S3-bucket-with-boto3/file.pdf')
s3_object.download_file('text.pdf')
print('File has been downloaded')