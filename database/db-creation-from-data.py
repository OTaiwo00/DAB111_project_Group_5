import pathlib
import sqlite3
import pandas as pd

path = pathlib.Path().cwd() # get the current working directory

def create_db_table(db_name, filename, table_name):
    file_path = path / filename # create a path to the data file
    db_path = path / 'website' / db_name #path to the database file to create

    con = sqlite3.connect(db_path) # Create a connection to the database. This will create the database if not already exist.
    cursor = con.cursor() # create a cursor to the current row

    breast_cancer = pd.read_csv(file_path) # read in the data 
    # insert the data into the specified table table_name
    breast_cancer.to_sql(table_name,con,index=False, if_exists='replace')
    # execute sql statement to check if data is loaded into the table
    recordset = cursor.execute(f"SELECT * FROM {table_name} LIMIT 30").fetchall()
    # commit the changes to the database
    con.commit()
    # close the connection
    con.close()
    #print the recordset
    print(recordset)


if __name__=="__main__":
    db_name = "breastcancer.db"
    table_name = "breast_cancer"
    filename = "database/breast-cancer.csv"
    create_db_table(db_name, filename, table_name)
