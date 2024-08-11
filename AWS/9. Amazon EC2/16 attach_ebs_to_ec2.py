import boto3

ec2_resource = boto3.resource('ec2')
volume = ec2_resource.Volume('vol-01719e322957b17e1')
print('Volume {} status -> {}'.format(volume.id, volume.state))

volume.attach_to_instance(
    Device = '/dev/sdh',
    InstanceId = 'i-0681590c6251d7560'
)
print('Volume {} Status -> {}'.format(volume.id, volume.state))