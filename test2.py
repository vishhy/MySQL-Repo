import mysql.connector as connector

connection = connector.connect(host='localhost', user='root', passwd='1234')
cursor = connection.cursor()

# cursor.execute("insert into vishwas.student_details values(101, 'vishwas', 'XII', 500, 30)")
# connection.commit()
cursor.execute("select * from vishwas.student_details")
print(cursor.fetchall())