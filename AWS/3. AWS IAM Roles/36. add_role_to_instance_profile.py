import boto3

iam = boto3.client('iam')
role_name = 'myEC2Role'
instance_profile_name = 'myEC2Profile'

#Add role to the instance profile
iam.add_role_to_instance_profile(
    InstanceProfileName = instance_profile_name,
    RoleName = role_name
)
print('IAM Role: {} added to IAM Instance Profile: {}'.format(role_name, instance_profile_name))