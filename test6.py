# Creating data frame of the uploaded data.

import mysql.connector as connector
import pandas as pd
import logging as lg

connection = connector.connect(host='localhost', user='root', passwd='1234')
cursor = connection.cursor()

lg.basicConfig(filename='log1.log', level=lg.INFO, format='%(asctime)s %(name)s %(levelname)s %(message)s\n')

try:
    df_dressdetails = pd.read_sql(sql='select * from dresses.dress_details', con=connection)
    lg.info(msg='Dataframe created successfully')
except Exception as e:
    lg.error(msg=e)

# print(df_dressdetails.head())

try:
    df_dresssales = pd.read_sql(sql='select * from dresses.dress_sales', con=connection)
    lg.info(msg='Dataframe created successfully')
except Exception as e:
    lg.error(msg=e)

try:
    dressdetails_json = df_dressdetails.to_json('F:\FSDS\Pandas Class Notes\data fsds\dressdetails.json', orient='records')
    lg.info(msg='JSON file created successfully')
except Exception as e:
    lg.error(msg=e)