import boto3
from boto3.dynamodb.conditions import Key

def query_movies(year, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('movies')
    response = table.query(
        KeyConditionExpression=Key('year').eq(year)
    )
    return response['Items']

if __name__ == '__main__':
    query_year = 2010
    print('Movie from {}'.format(query_year))

    movies = query_movies(query_year)
    for movie in movies:
        print(movie['year'], ':', movie['title'])