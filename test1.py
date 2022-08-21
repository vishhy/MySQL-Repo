# making a connection with sql by importing mysql package
# In SQL, Database: A Folder that contains many tables
# 1. Create Connection
# 2. Create Database
# 3. Define table structure: Defining Columns and their data types
# 4. Store data in Table


import mysql.connector as connector

# We've to connect pycharm to mysql

connection = connector.connect(host='localhost', user='root', passwd='1234')  # Creating Connection
# print(connection)
cursor = connection.cursor()  # Creating Cursor
# cursor.execute('create database vishwas')  # Database means folder means many tables can be stores in one database
# q1 = cursor.execute('create table vishwas.student_details(roll_no int(5),name varchar(30),class varchar(5), salary int(10),attendance int(3))')  # database_name.table_name

# cursor.execute('show databases')  # Executing Query through cursor
# print(cursor.fetchall())  # Executing Query through cursor

q2 = cursor.execute('select * from vishwas.student_details')
print(q2)