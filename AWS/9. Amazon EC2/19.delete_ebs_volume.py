import boto3

ec2_resource = boto3.resource('ec2')
#volume = ec2_resource.Volume('vol-01719e322957b17e1')
volume = ec2_resource.Volume('vol-00ed214d8947a73eb')
#volume = ec2_resource.Volume('vol-0c8ee186d618a4a8c')

if volume.state == 'available':
    volume.delete()
    print('Volume Deleted')

else:
    print('Can not delete volume attached')
