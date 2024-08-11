import mysql.connector as mc

try:
    mydb = mc.connect(
        host = 'rdsuser.chmm28ags7tu.us-east-1.rds.amazonaws.com',
        username = 'admin',
        password = 'password',
    )

    dbname = input('Please Enter you database name: ')
    cursor = mydb.cursor()
    cursor.execute('CREATE DATABASE {}'.format(dbname))
    print('Database Created')

except mc.Error as e:
    print('{} Failed to create database'.format(e))