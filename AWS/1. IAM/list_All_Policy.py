import boto3
def listPolicy():
    iam = boto3.client('iam')

    paginator = iam.get_paginator('list_policies')
    #for response in paginator.paginate(Scope= 'Local'):
    for response in paginator.paginate(Scope= 'AWS'):
        for policy in response['Policies']:
            policy_name = policy['PolicyName']
            arn = policy['Arn']
            print('Policy Name: {}\nArn: {}'.format(policy_name, arn))
            print('')

listPolicy()