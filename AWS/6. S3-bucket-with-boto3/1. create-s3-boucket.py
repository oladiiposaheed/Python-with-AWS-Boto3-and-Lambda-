import boto3

#Create resource
bucket = boto3.resource('s3')
response = bucket.create_bucket(
    Bucket = 'boto-3-bucket',
    ACL = 'private',

    # CreateBucketConfiguration= {
    #     'LocationConstraint': 'us-east-1'
    # }
)
print(response)