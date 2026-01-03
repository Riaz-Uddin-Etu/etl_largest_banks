# function to load the transformed data frame to an output CSV file.
def load_to_csv(df, output_path):
    df.to_csv(output_path)

# function to load the transformed data frame to an SQL database server as a table.
def load_to_db(df, table, sql_connection):
    df.to_sql(table, sql_connection, if_exists='replace', index=False)




