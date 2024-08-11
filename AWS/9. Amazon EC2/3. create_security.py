import boto3

ec2_client = boto3.client('ec2')

response = ec2_client.create_security_group(
    Description = 'This is description of the security group',
    GroupName = 'security-group',
    VpcId = 'vpc-0952251249a6e8a18'
)

print(response)