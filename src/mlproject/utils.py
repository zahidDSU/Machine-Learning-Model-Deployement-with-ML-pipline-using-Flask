import sys
import os
from src.mlproject.exception import CustomException
import numpy as np
import pandas as pd
import logging
import pymysql
import pickle


host = 'localhost'
user = 'root'
password = 'Password@#123'
db = 'mydb'

def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        mydb = pymysql.connect(
            host = host,
            user = user,
            password = password,
            db = db
        )
        logging.info("Connection Established",mydb)
        df = pd.read_sql_query('Select * from sales',mydb)
        print(df.head())
        
        return df
    except Exception as ex:
        raise CustomException(ex, sys)
print("File Executed")