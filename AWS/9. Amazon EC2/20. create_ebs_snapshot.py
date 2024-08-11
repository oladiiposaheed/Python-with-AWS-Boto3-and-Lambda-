import boto3

ec2_resource = boto3.resource('ec2')

volume_id = 'vol-0d57be7c20c21d37a'

snapshot = ec2_resource.create_snapshot(
    VolumeId = volume_id,
    TagSpecifications = [
        {
            'ResourceType': 'snapshot',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'Python Snapshot'
                }
            ]
        }
    ]
)
print('Snapshot created')