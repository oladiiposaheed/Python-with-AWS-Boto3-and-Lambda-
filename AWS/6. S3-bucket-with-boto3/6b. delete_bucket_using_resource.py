import boto3

#userboket
resource = boto3.resource('s3')
bucket_name = 'userboket'
s3_bucket = resource.Bucket(bucket_name)

s3_bucket.delete()
print('This {} has been deleted.'.format(s3_bucket))