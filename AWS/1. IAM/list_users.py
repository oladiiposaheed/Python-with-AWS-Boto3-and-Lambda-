import boto3

def lst_users():
    iam = boto3.client('iam')
    paginator = iam.get_paginator('list_users')
    for response in paginator.paginate():
        for user in response['Users']:
            username = user['UserName']
            Arn = user['Arn']
            # = user['Created']
            print('UserName: {}\nArn: {}'.format(username, Arn))
            print('*'*50)

lst_users()