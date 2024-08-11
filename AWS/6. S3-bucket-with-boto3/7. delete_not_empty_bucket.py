import boto3

BUCKET_NAME = 'userboket'

s3_resource = boto3.resource('s3')

s3_bucket = s3_resource.Bucket(BUCKET_NAME)

def clean_up():

    #delete the object
    for s3_object in s3_bucket.objects.all():
        s3_bucket.delete()

#delete bucket versioning
for s3_object_version in s3_bucket.object_versions.all():
    s3_object_version.delete()
print('S3 bucket cleaned')

clean_up()
s3_bucket.delete()
print('The bucket has been deleted')