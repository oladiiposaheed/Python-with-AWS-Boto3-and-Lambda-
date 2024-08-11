import boto3

db = boto3.resource('dynamodb')
table = db.Table('employee')

with table.batch_writer() as batch:
    batch.put_item(
        Item = {
        'emp_id': '4',
        'fname': 'Maria',
        'lname': 'Nushi',
        'salary': 35000,
        'gender': 'F',
        'email': 'maria@gmail.com.com',
        'age': 29,
        }
    )

    batch.put_item(
        Item = {
        'emp_id': '5',
        'fname': 'Jose',
        'lname': 'Muhammad',
        'salary': 85000,
        'gender': 'M',
        'email': 'josm@gmail.com.com',
        'age': 51,
        }
    )

    batch.put_item(
        Item = {
        'emp_id': '6',
        'fname': 'Wei',
        'lname': 'Yan',
        'salary': 70000,
        'gender': 'F',
        'email': 'maria@gmail.com.com',
        'age': 39,
        }
    )

    batch.put_item(
        Item = {
        'emp_id': '7',
        'fname': 'Ali',
        'lname': 'John',
        'salary': 62000,
        'gender': 'M',
        'email': 'ali@yahoo.com.com',
        'age': 55,
        }
    )

    batch.put_item(
        Item = {
        'emp_id': '11',
        'fname': 'Anna',
        'lname': 'Juan',
        'salary': 41000,
        'gender': 'F',
        'email': 'anna@gmail.com.com',
        'age': 27,
        }
    )

    batch.put_item(
        Item = {
        'emp_id': '8',
        'fname': 'Daniel',
        'lname': 'Robert',
        'salary': 66000,
        'gender': 'M',
        'email': 'darob@gmail.com.com',
        'age': 30,
        }
    )

    batch.put_item(
        Item = {
        'emp_id': '9',
        'fname': 'Maryam',
        'lname': 'Varlos',
        'salary': 57000,
        'gender': 'F',
        'email': 'mar@gmail.com.com',
        'age': 26,
        }
    )

    batch.put_item(
        Item = {
        'emp_id': '10',
        'fname': 'Abdul',
        'lname': 'Abubakar',
        'salary': 9000,
        'gender': 'M',
        'email': 'abdul@gmail.com.com',
        'age': 34,
        }
    )