import boto3

from pprint import pprint

ec2_client = boto3.client('ec2')

resp = ec2_client.create_key_pair(
    KeyName = 'mykey',
    KeyType = 'rsa'
)
#pprint(resp['KeyMaterial'])

#Store the pem file
file = open('EC2-Window.pem', 'w')
file.write(resp['KeyMaterial'])
file.close()