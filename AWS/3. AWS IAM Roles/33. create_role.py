import boto3
import json

iam = boto3.client('iam')

role_name = 'myEC2Role'
trust_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "ec2.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}

iam.create_role(
    RoleName = role_name,
    AssumeRolePolicyDocument = json.dumps(trust_policy)
)
print('AIM Role: {} created'.format(role_name))
#print(role_name)

