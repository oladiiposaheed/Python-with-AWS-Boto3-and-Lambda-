import boto3
from pprint import pprint
from botocore.exceptions import ClientError

def delete_movie(title, year, dynamodb=None):
    if not dynamodb:
        #Create dynamodb from resource
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('movies')

    try:
        response = table.update_item(
        Key={
            'year': year,
            'title': title
        },
        )
    except ClientError as e:
        print(e.response['Error']['Message'])

    else:
        return response
    
if __name__=='__main__':
    delete_response = delete_movie("Now You See Me", 2013)
    if delete_movie:
        pprint(delete_response)
