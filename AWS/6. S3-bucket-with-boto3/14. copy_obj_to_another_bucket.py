import boto3

s3_resource = boto3.resource('s3')

copy_source = {
    'Bucket': 'boketdjango',
    'Key': 'AWS/S3-bucket-with-boto3/user.txt'
}

s3_resource.meta.client.copy(copy_source, 'boto-3-bucket', 'copied.pdf')