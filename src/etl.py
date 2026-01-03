from datetime import datetime
from extract import extract
from transform import transform
from load import load_to_csv, load_to_db
import pandas as pd
import sqlite3
import os

URL = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'

os.makedirs('logs', exist_ok=True)
os.makedirs('data/processed', exist_ok=True)

output_csv_path = 'data/processed/Largest_banks_data.csv'
csv_path = 'data/raw/exchange_rate.csv'
db_name = 'Banks.db'
table_name = 'Largest_banks'
log_file ='logs/code_log.txt'

# Function to log the progress of the code.
def log_progress(message):
    time_format = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(time_format)
    with open(log_file, 'a') as logfile:
        logfile.write(timestamp + ',' + message + '\n')

# function to run queries on the database table.
def run_query(query_statement, sql_connection):
    query_output = pd.read_sql(query_statement, sql_connection)
    print('query_statement: ', query_statement)
    print('query_output: \n', query_output)

if __name__ == '__main__':
    # Log the initialization of the ETL process 
    log_progress('ETL Initiated')

    # Extraction phase
    log_progress('Extraction Phase Initiated')
    extraction = extract(URL)
    log_progress('Extraction Phase Ended')

    # Transform phase 
    log_progress('Transformation Phase Initiated')
    transformation = transform(extraction, csv_path)
    log_progress('Transformation Phase Ended')

    # loading Phase
    # CSV load
    log_progress('CSV Loading Phase Initiated')
    load_to_csv(transformation, output_csv_path)
    log_progress('CSV Loading Phase Ended')

    # DB Load
    log_progress('DB Loading Phase Initiated')
    conn = sqlite3.connect(db_name)
    load_to_db(transformation, table_name, conn)
    log_progress('DB Loading Phase Ended')

    # Log the completion of the ETL process 
    log_progress("ETL Ended") 

    #run_query in terminal
    query1 = f'SELECT * FROM {table_name}'
    query2 = f'SELECT AVG(MC_GBP_Billion) FROM {table_name}'
    query3 = f'SELECT Name from {table_name} LIMIT 5'
    run_query(query1, conn)
    run_query(query2, conn)
    run_query(query3, conn)

    conn.close()