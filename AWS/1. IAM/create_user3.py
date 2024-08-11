import boto3

def create_user(username):
    iam = boto3.client('iam')  #Create IAM client
    response = iam.create_user(UserName=username)
    print(response)

create_user('user_20')