import boto3

# Detach Policy from User Group with Python
def detach_group(user_group, arn):
    iam = boto3.client('iam')

    response = iam.detach_group_policy(
        GroupName = user_group,
        PolicyArn = arn
    )
    print(response)

detach_group(user_group='RDSAdmin', arn='arn:aws:iam::aws:policy/AmazonRDSFullAccess')