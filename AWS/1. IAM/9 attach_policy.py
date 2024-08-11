import boto3

def attach_policy(policy_arn, group_name):
    iam = boto3.client('iam')
    response = iam.attach_group_policy(
        GroupName = group_name,
        PolicyArn = policy_arn
    )
    print(response)

#attach_policy(policy_arn='arn:aws:iam::aws:policy/AmazonRDSFullAccess', group_name='RDSAdmin')
attach_policy(policy_arn='arn:aws:iam::aws:policy/AmazonS3FullAccess', group_name='S3Admins')

