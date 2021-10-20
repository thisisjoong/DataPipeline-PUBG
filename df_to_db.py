from match_dataframe import *

from sqlalchemy import create_engine
import pymysql
import sys
import json
import os
import base64
import requests
import pandas as pd


# host = 'mydbinstance.cbpwyt3fnvr3.us-east-2.rds.amazonaws.com'
# username = 'hyunjoong'
# password = 'guswnd12!!'
# database = 'mydbinstance'
# port = '3306'

# def connect_RDS(host,port,username,password,database):
#     try:
#         conn = pymysql.connect(host, user=username, passwd=password, db=database,port=port, use_unicode=True, charset='utf-8')
#         cursor = conn.cursor()

#     except:
#         logging.error("RDS에 연결되지 않았습니다.")
#         sys.exit(1)

#     return conn,cursor



db_connection = create_engine('mysql+pymysql://hyunjoong:'+'guswnd12!!'+'@mydbinstance.cbpwyt3fnvr3.us-east-2.rds.amazonaws.com:3306/mydbinstance?charset=utf8', encoding='utf-8')
conn = db_connection.connect()

stats_df.to_sql(name='match1', con=db_connection, if_exists='append', index=False)
stats_2_df.to_sql(name='match2', con=db_connection, if_exists='append', index=False)
stats_3_df.to_sql(name='match3', con=db_connection, if_exists='append', index=False)
stats_4_df.to_sql(name='match4', con=db_connection, if_exists='append', index=False)
stats_5_df.to_sql(name='match5', con=db_connection, if_exists='append', index=False)
stats_6_df.to_sql(name='match6', con=db_connection, if_exists='append', index=False)
stats_7_df.to_sql(name='match7', con=db_connection, if_exists='append', index=False)
stats_8_df.to_sql(name='match8', con=db_connection, if_exists='append', index=False)
stats_9_df.to_sql(name='match9', con=db_connection, if_exists='append', index=False)
stats_10_df.to_sql(name='match10', con=db_connection, if_exists='append', index=False)

all_match_info_df.to_sql(name='match_info', con=db_connection, if_exists='append', index=False)

conn.close()