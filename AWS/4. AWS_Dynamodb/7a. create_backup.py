import boto3

db = boto3.client('dynamodb')

response = db.create_backup(
    #TableName= 'article',
    #BackupName= 'article_backup'
    TableName= 'employee',
    BackupName= 'employee_backup'
)
print(response)