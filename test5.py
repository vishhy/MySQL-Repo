# Sql Task: Bulk Upload
import mysql.connector as connector
from sqlalchemy import create_engine
import pandas as pd

connection = connector.connect(host='localhost', user='root', passwd='1234', port=3306)
cursor = connection.cursor()

# cursor.execute('create database dresses')
# cursor.execute('create table dresses.dress_details '
#                '(dress_id int,'
#                'style varchar(30),'
#                'price varchar(30),'
#                'rating decimal,'
#                'size varchar(30),'
#                'season varchar(30),'
#                'neckline varchar(30),'
#                'sleevelength varchar(30),'
#                'waistline varchar(30),'
#                'material varchar(30),'
#                'fabrictype varchar(30),'
#                'decoration varchar(30),'
#                'patterntype varchar(30),'
#                'recommendation int)')

cursor.execute('create table dresses.dress_sales'
               '(dress_id int,'
               '29A int,'
               '31A int,'
               '02S int,'
               '04S int,'
               '06S int,'
               '08S int,'
               '10S int,'
               '12S int,'
               '14S int,'
               '16S int,'
               '18S int,'
               '20S int,'
               '22S int,'
               '24S int,'
               '26S int,'
               '28S int,'
               '30S int,'
               '02O int,'
               '04O int,'
               '06O int,'
               '08O int,'
               '10O int,'
               '12O int)')

# cursor.execute('describe dresses.dress_details')
engine = create_engine('mysql+mysqlconnector://' + 'root' + ':' + '1234' + '@' + 'localhost' ':' + '3306', echo=False)
# print(cursor.fetchall())

# df1 = pd.read_excel("F:\\FSDS\\Pandas Class Notes\\data fsds\\Attribute DataSet.xlsx")
df2 = pd.read_excel("F:\\FSDS\\Pandas Class Notes\\data fsds\\Dress Sales.xlsx", sheet_name='Sheet3')
#print(df1.head(3))

#df1.to_sql(name='dress_details', schema='dresses', con=engine, if_exists='append', index=False)
df2.to_sql(name='dress_sales', schema='dresses', con=engine, if_exists='append', index=False)