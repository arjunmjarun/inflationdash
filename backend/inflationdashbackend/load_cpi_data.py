import os
import sys
import uuid
import pandas as pd
import sqlite3 as sql

## Data Ingest
files = [x for x in os.listdir('data') if not x.startswith('.')]

## Data sets:
## CPIAUCSL = US inflation, all items
## CUSR0000SETA02 = US inflation, used cars and trucks
## CUUR0000SETA01 = US inflation, new cars
## CPIUFDSL = US inflation, food
## CUUR0000SEHA = US inflation, rent
## CPIENGSL = US inflation, energy
## CUSR0000SETB01 = US inflation, gasoline
## CUSR0000SEHG = US inflation, water trash & sewer collection
## CUUR0000SAS4 = US inflation, transportation services

file_description_map = {
    'CPIAUCSL.csv' : 'US Inflation, All Items',
    'CUSR0000SETA02.csv': 'US Inflation, Used Cars & Trucks',
    'CUUR0000SETA01.csv': 'US Inflation, New Cars',
    'CPIUFDSL.csv': 'US Inflation, Food',
    'CUUR0000SEHA.csv': 'US Inflation, Rent',
    'CPIENGSL.csv': 'US Inflation, Energy',
    'CUSR0000SETB01.csv': 'US Inflation, Gasoline',
    'CUSR0000SEHG.csv': 'US Inflation, Water Trash & Sewer Collection',
    'CUUR0000SAS4.csv': 'US Inflation, Transportation Services'
}

def clean_data(df, filename, description_map):
    '''
    Given a CPI DF add the following cols:
        - cpi_year
        - cpi_month
        - cpi_year_month
        - cpi_description

    Args:
        - df: The dataframe being cleaned
        - filename: The name of the source CSV for the given DF
        - description_map: The dictionary that maps a given file to a file description 
    '''
    df = df.loc[df[filename[:-4]] != '.'].reset_index(drop=True)
    print(df.head())

    uuids = [str(uuid.uuid4()) for x in range(len(df))]
    df['monthly_cpi_id'] = uuids
    df['cpi_year'] = pd.to_datetime(df['DATE']).dt.year
    df['cpi_year'] = df['cpi_year'].astype(int)
    df['cpi_month'] = pd.to_datetime(df['DATE']).dt.month
    df['cpi_month'] = df['cpi_month'].astype(int)
    df['cpi_year_month'] = df['cpi_year'].astype(str) + '-' + df['cpi_month'].astype(str)
    df['cpi_internal_code'] = filename[:-4]
    df['cpi_description'] = description_map.get(filename)
    df['DATE'] = pd.to_datetime(df['DATE']).dt.strftime('%Y-%m-%d')
    df.rename(columns = {
        'DATE': 'cpi_date',
        filename[:-4]: 'cpi'
    }, inplace=True)
    df['cpi'] = df['cpi'].astype(float).astype(int)
    return df

def load_data(df, conn, table_name):
    '''
    Load a specific dataframe to a specific table

    Args:
         - df: The dataframe being loaded
         - conn: A SQLite connection object
         - table_name: The specific table the dataframe is being loaded to
    '''
    df.to_sql(table_name, conn, if_exists='replace', index=False)

conn = sql.connect('db.sqlite3')

for file in files:
    print(f'Loading file {file}...')
    df = pd.read_csv(f'data/{file}')
    clean_df = clean_data(df, filename=file, description_map=file_description_map)
    load_data(df=clean_df, conn=conn, table_name='inflation_monthlycpi')
    print(f'Finished loading file {file}...')