import boto3
from pprint import pprint

rds_client = boto3.client('rds')

response = rds_client.create_db_instance(
    DBName = 'rdsUser',
    DBInstanceIdentifier = 'rdsUser',
    AllocatedStorage = 20,
    DBInstanceClass = 'db.t3.micro',
    Engine = 'MySql',
    MasterUsername = 'admin',
    MasterUserPassword = 'password',
    Port = 3306,
    EngineVersion = '8.0.36',
    PubliclyAccessible = True,
    StorageType = 'gp2',
)
pprint(response)