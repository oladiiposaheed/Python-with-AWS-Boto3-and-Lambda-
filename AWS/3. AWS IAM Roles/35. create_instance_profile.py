import boto3

iam = boto3.client('iam')

instance_profile_name = 'myEC2Profile'
iam.create_instance_profile(
    InstanceProfileName = instance_profile_name
)
print('Instance Profile Created: {}'.format(instance_profile_name))