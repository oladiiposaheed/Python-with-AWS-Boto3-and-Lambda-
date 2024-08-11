import mysql.connector as mc

try:
    mydb = mc.connect(
        host = 'rdsuser.chmm28ags7tu.us-east-1.rds.amazonaws.com',
        user = 'admin',
        password = 'password',
        database = 'rdsdb'
    )
    print('Connection Created')
except mc.Error as e:
    print('There is no connection for {}'.format(e))