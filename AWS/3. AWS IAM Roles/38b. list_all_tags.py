import boto3

iam_client = boto3.client('iam')

response = iam_client.list_users()
#print(response)
for user in response['Users']:
    #print('Username: {}'.format(user))
    user_name = user['UserName']
    user_id = user['UserId']
    tags = iam_client.list_user_tags(UserName= user_name)['Tags']
    #print(user_name, '', user_id)
    print('User: {} Tags: {}'.format(user, tags))
