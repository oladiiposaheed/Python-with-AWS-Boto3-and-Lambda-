import mysql.connector as mc

try:
    mydb = mc.connect(
        host = 'rdsuser.chmm28ags7tu.us-east-1.rds.amazonaws.com',
        user = 'admin',
        password = 'password',
        database = 'rdsUser'
    )
    mycursor = mydb.cursor()
    query = "UPDATE Person SET firstname= 'updated' WHERE id = '1'"
    mycursor.execute(query)
    mydb.commit()
    print(mycursor.rowcount, 'recorded updated')
except mc.Error as e:
    print('{} can not update data'.format(e))