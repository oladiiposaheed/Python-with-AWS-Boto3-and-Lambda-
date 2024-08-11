import boto3

##Create Access Key for the User
'''
def create_access_key(username):
    iam = boto3.client('iam')
    response = iam.create_access_key(
        UserName = username
    )
    print(response)

create_access_key(username='django_user')
create_access_key(username='django_users')
'''

def update_access():
    iam = boto3.client('iam')
    iam.update_access_key(
        AccessKeyId= 'AKIAVRUVPS3YJYS2VOXL',
        Status = 'Inactive',
        UserName = 'django_user'
    )
update_access()