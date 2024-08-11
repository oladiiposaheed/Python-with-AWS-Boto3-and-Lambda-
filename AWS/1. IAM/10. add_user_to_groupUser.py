import boto3

def add_user(username, group_name):
    iam = boto3.client('iam')

    response = iam.add_user_to_group(
        UserName= username,
        GroupName = group_name
    )
    print(response)

#add_user(username='rdsUser', group_name='RDSAdmin')
add_user(username='s3User', group_name='S3Admins')
add_user(username='django_user', group_name='Ictdept')
add_user(username='my_user', group_name='Ictdept')