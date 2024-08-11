import boto3
import json

def create_policy():
    # Initialize Boto3 IAM client
    iam = boto3.client('iam')  

    #create administrator policy
    user_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "*",
            "Resource": "*"
        }
    ]
    }
    # Create custom IAM policy
    policies = ['completeAccess', 'pyFullAccess-1', 'pyFullAccess-2', 'pyFullAccess-3']
    for policy_name in policies:
        response = iam.create_policy(
        #PolicyName = 'pyFullAccess',
        PolicyName = policy_name,
        PolicyDocument = json.dumps(user_policy)
    )
    print(response)
    #print('*'*100)

    # Extract the ARN of the created policy
    #policy_arn = response['Policy']['Arn']

    # Print the ARN of the created policy
    #print("Custom IAM policy created successfully with ARN:", policy_arn)



create_policy()



