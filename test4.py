# Tryinng to perform Mysql that we did in workbench

import mysql.connector as connector

connection = connector.connect(host='localhost', user='root', passwd='1234')
cursor = connection.cursor()

# cursor.execute('select * from bank.bank_details')
# cursor.execute('select age,job from bank.bank_details where
# balance > 100 order by age desc')
cursor.execute("insert into bank.bank_details values(45, 'CEO', 'Married',"
               " 'Post Graduate', 'null', 5000, 'no', 'no', 'known', 29, 'March', 4455, 1, 30, 0, 'unknown', 'no')")
connection.commit()

cursor.execute("select * from bank.bank_details where education = 'Post Graduate'")
print(cursor.fetchall())