import pandas as pd
import sqlite3 as sql

conn = sql.connect('db.sqlite3')
crsr = conn.cursor()
query = 'SELECT * FROM inflation_monthlycpi LIMIT 10'
crsr.execute(query)
results = crsr.fetchall()
df = pd.DataFrame(results)
df.columns = [description[0] for description in crsr.description]
print(df)