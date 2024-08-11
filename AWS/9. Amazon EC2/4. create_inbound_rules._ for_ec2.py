import boto3

ec2_client = boto3.client('ec2')

response = ec2_client.authorize_security_group_ingress(
    GroupId = 'sg-0e80fb7efe82a3f0a',
    IpPermissions = [
        {
            'IpProtocol': 'tcp',
            'FromPort': 80,
            'ToPort': 80,
            'IpRanges': [{'CidrIp': '0.0.0.0/0', 'Description': 'My description'}] 
        },

        {
            'IpProtocol': 'tcp',
            'FromPort': 45,
            'ToPort': 45,
            'IpRanges': [{'CidrIp': '0.0.0.0/0', 'Description': 'My description'}] 
        },
    ]
)
print(response)