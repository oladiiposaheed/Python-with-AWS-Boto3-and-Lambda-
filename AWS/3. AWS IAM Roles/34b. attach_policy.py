import boto3

iam = boto3.client('iam')

role_name = "myEC2Role"

policy_name = 'myECPolicy'
iam.attach_role_policy(
    RoleName = role_name,
    PolicyArn = 'arn:aws:iam::381491844848:policy/myECPolicy'
)
print('Policy: {} attaced to IAM Role {}'.format(policy_name, role_name))