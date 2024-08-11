import boto3
def stop_instance(instance_id):
    ec2_client = boto3.client('ec2')
    response = ec2_client.stop_instances(InstanceIds = [instance_id])

    print(response)

#stop_instance('i-00e02142b8c3a6d52')
stop_instance('i-073d740251e5b8969')