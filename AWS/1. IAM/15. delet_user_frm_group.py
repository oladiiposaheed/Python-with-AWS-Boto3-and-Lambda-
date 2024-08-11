import boto3

def delete_user_group(username, groupName):
    iam = boto3.resource('iam')
    #group = iam.Group(groupName)
    #response = group.remove_user(UserName=username)
    #response = group.remove_user_from_group(UserName=username)
    response = iam.remove_user_from_group(
    GroupName=username,
    UserName=groupName,
)

    print(response)
delete_user_group(username='rdsUser', groupName='RDSAdmin')