import boto3

bucket = boto3.client('s3')

response = bucket.list_buckets()
print('List All Buckets')

for bucket in response['Buckets']:
    print(bucket)