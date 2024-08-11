import boto3

#ec2_client = boto3.client('ec2')
ec2_client = boto3.resource('ec2')

new_volume = ec2_client.create_volume(
    AvailabilityZone = 'us-east-1d',
    Size = 5,
    VolumeType= 'gp2',
    TagSpecifications = [
        {
            'ResourceType': 'volume',
            'Tags':[
                {
                   'Key': 'Name',
                   #'Value': 'python and boto3' 
                   'Value': 'python and boto3 with resource'
                }
            ]
        }
    ]
)

#print('Created Volume ID: {}'.format(new_volume['VolumeId']))
print('Created Volume ID: {}'.format(new_volume.id))