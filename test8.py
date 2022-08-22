# Sql queries on dress_details & dress_sales data
import mysql.connector as connector
import logging as lg

connection = connector.connect(host='localhost', user='root', passwd='1234')
cursor = connection.cursor()

lg.basicConfig(filename='log1.log', level=lg.INFO, format='%(asctime)s %(name)s %(levelname)s %(message)s\n')

# Query 1
# try:
#     cursor.execute(
#         'select dresses.dress_details.price, dresses.dress_details.rating, dresses.dress_details.recommendation from dresses.dress_details left join dresses.dress_sales on dresses.dress_details.dress_id = dresses.dress_sales.dress_id')
#     lg.info(msg='Query executed successfully')
#     print(cursor.fetchall())
#
# except Exception as e:
#     lg.error(e)

# Query 2
# try:
#     cursor.execute('select dress_id, count(distinct dress_id) from dresses.dress_details group by style')
#     # cursor.execute('select style, count(distinct dress_id) from dresses.dress_details group by style')
#     lg.info(msg='Query executed successfully')
#     print(cursor.fetchall())
#
# except Exception as e:
#     lg.error(e)

# Query 3
# try:
#     cursor.execute('select dress_id, style, price, rating from dresses.dress_details where recommendation = 0')
#     lg.info(msg='Query executed successfully')
#     print(cursor.fetchall())
#
# except Exception as e:
#     lg.error(e)

# Query 4
s = """select dress_id, COALESCE(29A, 0) + COALESCE(31A, 0) + COALESCE(02S, 0) + COALESCE(04S, 0) + COALESCE(06S, 0)
+ COALESCE(08S, 0) + COALESCE(10S, 0) + COALESCE(12S, 0) + COALESCE(14S, 0) + COALESCE(16S, 0) + COALESCE(18S, 
0)  + COALESCE(20S, 0) + COALESCE(22S, 0) + COALESCE(24S, 0) + COALESCE(26S, 0) + COALESCE(28S, 0) + COALESCE(30S, 
0) + COALESCE(02O, 0) + COALESCE(04O, 0) + COALESCE(06O, 0) + COALESCE(08O, 0) + COALESCE(10O, 0) + COALESCE(12O, 0) as 
'Total_sales 'from dresses.dress_sales;"""
# s = """insert into dresses.dress_sales(Total_Sales)
# select COALESCE(29A, 0) + COALESCE(31A, 0) + COALESCE(02S, 0) + COALESCE(04S, 0) + COALESCE(06S, 0)
# + COALESCE(08S, 0) + COALESCE(10S, 0) + COALESCE(12S, 0) + COALESCE(14S, 0) + COALESCE(16S, 0) + COALESCE(18S,
# 0)  + COALESCE(20S, 0) + COALESCE(22S, 0) + COALESCE(24S, 0) + COALESCE(26S, 0) + COALESCE(28S, 0) + COALESCE(30S,
# 0) + COALESCE(02O, 0) + COALESCE(04O, 0) + COALESCE(06O, 0) + COALESCE(08O, 0) + COALESCE(10O, 0) + COALESCE(12O, 0) as
# 'Total_sales 'from dresses.dress_sales;"""

try:
    cursor.execute(s)
    lg.info(msg='Query executed successfully')
    #print(cursor.fetchall())
except Exception as e:
    lg.error(e)

# Query 5
l = []
w = cursor.fetchall()
# print(w)
w.sort(key=lambda i:i[1], reverse=True)
print(w)