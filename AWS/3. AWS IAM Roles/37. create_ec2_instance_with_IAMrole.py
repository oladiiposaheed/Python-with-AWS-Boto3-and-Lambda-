import boto3

ec2_client = boto3.client('ec2')

instance_profile_name = 'myEC2Profile'
response = ec2_client.run_instances(
    ImageId = 'ami-0427090fd1714168b',
    InstanceType = 't2.micro',
    MinCount = 1,
    MaxCount = 1,
    IamInstanceProfile = {
        "Name": instance_profile_name
    }
)
instance_id = response['Instances'][0]['InstanceId']
print('EX2 Instance with IAM Instance Proflie: {} launched'.format(instance_profile_name))