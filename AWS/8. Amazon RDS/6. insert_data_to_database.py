import mysql.connector as mc

try:
    mydb = mc.connect(
        host = 'rdsuser.chmm28ags7tu.us-east-1.rds.amazonaws.com',
        user = 'admin',
        password = 'password',
        database = 'rdsUser'
    )

    mycursor = mydb.cursor()

    nums = int(input('How many data do you want to enter?: '))
    for num in range(nums + 1):
        firstName = input('Please enter your first name: ')
        lastName = input('Please enter your last name: ')

        query = 'INSERT INTO Person (firstName, lastName) VALUES (%s, %s)'
        value = (firstName, lastName)

        mycursor.execute(query, value)

    mydb.commit()
    print('Data Inserted')

except mc.Error as e:
    print('{} Fail to add data'.format(e))