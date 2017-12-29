import pandas as pd
from sqlalchemy import create_engine
import sqlite3
import os

connex = sqlite3.connect("all_your_base.db")  # Opens file if exists, else creates file
cur = connex.cursor()  # This object lets us actually send messages to our DB and receive results

file = r'all_data.csv'

# print pd.read_csv(file, nrows=5, sep='\t', encoding='utf-16')
statinfo = os.stat(file)
chunksize = statinfo.st_size

for chunk in pd.read_csv(file, chunksize=chunksize, iterator=True, sep='\t', encoding='utf-16'):
    chunk.to_sql(name="data", con=connex, if_exists="append", index=False)  #"name" is name of table 
    print(chunk.iloc[0, 1])
