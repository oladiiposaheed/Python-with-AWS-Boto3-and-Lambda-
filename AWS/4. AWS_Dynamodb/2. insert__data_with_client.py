import boto3

db = boto3.client('dynamodb')

response = db.put_item(
    TableName = 'employee',
    Item = {
        'emp_id': {
            'S': '4'
        },

        'fname': {
            'S': 'Kazeem'
        },
        'lname': {
            'S': 'Mahmud'
        },
        'age': {
            'N': '67'
        },
        'email': {
            'S': 'mah@hotmail.com'
        },
        'salary': {
            'N': '43000'
        },
        
        'gender': {
            'S': 'M'
        },
    }
)