import boto3

def attach_policy(policy_arn, username):
    iam = boto3.client('iam')

    response = iam.attach_user_policy(
        UserName = username,
        PolicyArn = policy_arn
    )
    print(response)

attach_policy('arn:aws:iam::381491844848:policy/pyFullAccess', 'django_user')