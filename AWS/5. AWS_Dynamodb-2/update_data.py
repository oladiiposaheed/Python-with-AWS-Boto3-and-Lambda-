import boto3
from pprint import pprint
from decimal import Decimal

def update_movie(title, year, rating, plot, dynamodb=None):
    if not dynamodb:
        #Create dynamodb from resource
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('movies')

    response = table.update_item(
        Key={
            'year': year,
            'title': title
        },

        UpdateExpression='set info.rating=:r, info.plot=:p',
        ExpressionAttributeValues = {
            ':r': Decimal(rating),
            ':p': plot,
        },
        ReturnValues = 'UPDATED_NEW'
    )
    return response

if __name__=='__main__':
    update_response = update_movie(
        'World War Z', 2013, 8.5, 'This is the latest version of the movie'
    )
    pprint(update_response)
