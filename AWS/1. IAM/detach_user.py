import boto3

iam = boto3.client('iam')
response = iam.detach_user_policy(
    UserName = 'django_user',
    PolicyArn = 'arn:aws:iam::381491844848:policy/pyFullAccess'
)
print(response)