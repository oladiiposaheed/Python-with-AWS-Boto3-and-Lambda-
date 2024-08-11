import boto3

s3 = boto3.resource('s3')

object_summary = s3.ObjectSummary('boketdjango','AWS/S3-bucket-with-boto3/user.txt')
print(object_summary)
print(object_summary.bucket_name)
print(object_summary.key)