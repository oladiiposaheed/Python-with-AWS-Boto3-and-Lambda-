import boto3

ec2_client = boto3.client('ec2')
ec2_resource = boto3.resource('ec2')
volume = ec2_resource.Volume('vol-01719e322957b17e1')

volume.detach_from_instance(
    Device = '/dev/sdh',
    InstanceId = 'i-0681590c6251d7560'
)
waiter = ec2_client.get_waiter('volume_available')
waiter.wait(
    VolumeIds = [
        volume.id
    ]
)
print('Volume {} Status -> {}'.format(volume.id, volume.state))