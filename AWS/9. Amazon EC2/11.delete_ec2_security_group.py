import boto3

ec2_client = boto3.client('ec2')
response = ec2_client.delete_security_group(
    #GroupId = 'sg-0e80fb7efe82a3f0a'
    GroupId = 'sg-0e6c5b1bc00a081f7'
)
print(response)

