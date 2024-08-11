import boto3

def create_movie_table(dynamodb= None):

    #Create dynamodb if there is no dynamodb
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    #Create table
    table = dynamodb.create_table(
        TableName= 'movies',
        KeySchema= [
            {
                'AttributeName': 'year',
                'KeyType': 'HASH'
            },

            {
                'AttributeName': 'title',
                'KeyType': 'RANGE'
            }
        ],

        AttributeDefinitions = [
            {
                'AttributeName': 'year',
                'AttributeType': 'N'
            },

            {
                'AttributeName': 'title',
                'AttributeType': 'S'
            }
        ],

        ProvisionedThroughput = {
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10,
        }

    )
    return table

if __name__=='__main__':
    movie_table = create_movie_table()
    print('Table status: {}'.format(movie_table.table_status))