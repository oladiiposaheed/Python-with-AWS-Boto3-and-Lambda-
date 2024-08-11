import mysql.connector as mc
try:
    mydb = mc.connect(
        host = 'rdsuser.chmm28ags7tu.us-east-1.rds.amazonaws.com',
        user = 'admin',
        password = 'password',
        database = 'rdsUser'
    )

    mycursor = mydb.cursor()

    mycursor.execute('CREATE TABLE Person (id INT AUTO_INCREMENT PRIMARY KEY, \
                     lastName VARCHAR(255), \
                     firstName VARCHAR(255))')
    print('Table is created')
    
except mc.Error as e:
    print('{} table not created'.format(e))