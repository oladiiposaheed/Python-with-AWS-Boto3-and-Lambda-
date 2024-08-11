import boto3

rds_client = boto3.client('rds')

response = rds_client.describe_db_instances(
    DBInstanceIdentifier = 'rdsUser',   
)
print(response)