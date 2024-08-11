import boto3

client = boto3.client('s3')
response = client.delete_objects(
    Bucket = 'boketdjango',
    Delete = {
        'Objects': [
            {
              'Key':'AWS/S3-bucket-with-boto3/files.txt'   
            },

            {
              'Key':'AWS/S3-bucket-with-boto3/user.txt'   
            }
        ]
    }
)

print(response)