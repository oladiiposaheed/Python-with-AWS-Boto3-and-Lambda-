import boto3

resource = boto3.resource('s3')

response = resource.buckets.all()
print('List All Buckets')

for bucket in response:
    print(bucket.name)