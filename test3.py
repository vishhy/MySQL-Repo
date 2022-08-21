import mysql.connector as connector

connection = connector.connect(host='localhost', user='root', passwd='1234')
cursor = connection.cursor()

cursor.execute("select name, roll_no from vishwas.student_details")
# print(type(cursor.fetchall()))  # Gives a list: means an iterable
for i in cursor.fetchall():
    print(i)

# print(cursor.fetchone())