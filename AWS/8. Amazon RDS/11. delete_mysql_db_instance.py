import boto3

rds_client = boto3.client('rds')

response = rds_client.delete_db_instance(
    DBInstanceIdentifier = 'database-1',
    SkipFinalSnapshot = False,
    FinalDBSnapshotIdentifier = 'rdsuser-final-snapshot',
    DeleteAutomatedBackups= True
)

print(response)