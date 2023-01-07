import pandas as pd
pd.set_option('display.max_columns', None)
import sqlite3 as sql

conn = sql.connect('db.sqlite3')
crsr = conn.cursor()
query = '''SELECT DISTINCT
                cpi_2021,
                cpi_2022,
                cpi_2022.cpi_month_2022,
                (cpi_2022 - cpi_2021) / cast(cpi_2022 AS REAL) AS inflation_percentage
           FROM (
            SELECT
                cpi as cpi_2021,
                cpi_month as cpi_month_2021
            FROM inflation_monthlycpi
            WHERE cpi_internal_code = "CUUR0000SEHA"
            AND   cpi_year IN ("2021")
           ) AS cpi_2021
           JOIN
           (
            SELECT
                cpi as cpi_2022,
                cpi_month as cpi_month_2022
            FROM inflation_monthlycpi
            WHERE cpi_internal_code = "CUUR0000SEHA"
            AND   cpi_year IN ("2022")
           ) AS cpi_2022 ON cpi_2021.cpi_month_2021 = cpi_2022.cpi_month_2022
        '''
crsr.execute(query)
results = crsr.fetchall()
df = pd.DataFrame(results)
df.columns = [description[0] for description in crsr.description]
print(df)