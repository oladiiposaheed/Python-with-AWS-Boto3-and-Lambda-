import mysql.connector as mc

try:
    dbname = input('Please Enter The Database Name: ')
    tablename = input('Please Enter The Table Name: ')
    mydb = mc.connect(
    host = 'rdsuser.chmm28ags7tu.us-east-1.rds.amazonaws.com',
    user = 'admin',
    password = 'password',
    database = dbname
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM {}".format(tablename))

    results = mycursor.fetchall()

    for data in results:
        print(data)

except mc.Error as e:
    print("{} database has no data".format(e))
