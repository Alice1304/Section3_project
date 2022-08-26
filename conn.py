import data #import from data.py 
import sqlite3

conn = sqlite3.connect('cancer.db')
data.df.to_sql('cancer', conn)






