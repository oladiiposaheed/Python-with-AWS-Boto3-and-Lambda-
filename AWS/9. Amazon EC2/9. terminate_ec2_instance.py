import boto3

def terminate_instance(instance_id):

    ec2_client = boto3.client('ec2')
    response = ec2_client.terminate_instances(InstanceIds= [instance_id])
    print(response)

#terminate_instance('i-073d740251e5b8969')
terminate_instance('i-00e02142b8c3a6d52')
