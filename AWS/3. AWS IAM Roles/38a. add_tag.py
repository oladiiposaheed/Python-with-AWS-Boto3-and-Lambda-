import boto3

iam_client = boto3.client('iam')

user_name = 'ola'
tags = [{'Key': 'Department', 'Value': 'ICT'}, 
        {'Key': 'Project', 'Value': 'Onboarding'}]

iam_client.tag_user(UserName= user_name, Tags= tags)
print('Tag Added')