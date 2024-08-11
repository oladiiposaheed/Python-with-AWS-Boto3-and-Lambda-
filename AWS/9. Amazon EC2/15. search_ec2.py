import boto3

#ec2_client = boto3.client('ec2')
ec2_resource = boto3.resource('ec2')

for volume in ec2_resource.volumes.filter(
    Filters = [
        {
            'Name':'tag:Name',
            'Values': [
                'python and boto3',
            ]
        }
    ]
):
    print('Volume {} ({} Gib) -> {}'.format(volume.id, volume.size, volume.state))