import mysql.connector as mc

try:
    mydb = mc.connect(
        host = 'rdsuser.chmm28ags7tu.us-east-1.rds.amazonaws.com',
        user = 'admin',
        password = 'password',
        database = 'rdsUser'
    )

    mycursor = mydb.cursor()
    mycursor.execute('SHOW TABLES')

    for table in mycursor:
        print(table)
    
except mc.Error as e:
    print('No table present in the {}'.format(e))