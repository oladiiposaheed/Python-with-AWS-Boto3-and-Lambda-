import boto3

ec2_client = boto3.client('ec2')

volume_id = 'vol-01719e322957b17e1'

response = ec2_client.modify_volume(
    VolumeId = volume_id,
    Size = 7
)
print(response)