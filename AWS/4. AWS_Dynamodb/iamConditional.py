import datetime
import boto3
import json

#Create IAM Client
iam = boto3.client('iam')

#Get the current date in ISO 8601 format without the time
current_date = datetime.utcnow().strftime('%Y-%m-%d')

#Define the start and end times for the access window in ISO 8601 format
start_time = '{}T01:00:00Z'.format(current_date)
end_time = '{}T03:00:00Z'.format(current_date)

policy_document = {
    "Version": ""
}