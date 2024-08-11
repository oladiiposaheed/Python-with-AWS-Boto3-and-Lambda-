import boto3

db = boto3.client('dynamodb')

response = db.delete_backup(
    BackupArn= 'arn:aws:dynamodb:us-east-1:381491844848:table/employee/backup/01721841807874-9bfa20f2'
)

print(response)