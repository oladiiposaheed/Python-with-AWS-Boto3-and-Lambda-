import boto3

db = boto3.resource('dynamodb')
table = db.Table('employee')
table.put_item(
    Item = {
        'emp_id': '3',
        'fname': 'Peter',
        'lname': 'Chucks',
        'salary': 50000,
        'gender': 'Male',
        'email': 'chucks@yahoo.com',
        'age': 42,
    }
)