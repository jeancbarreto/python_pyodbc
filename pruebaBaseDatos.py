import pyodbc 
import pandas as pd
import csv

def main():
    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-LQFETQU\SQLEXPRESS;'
                      'Database=prueba;'
                      'Trusted_Connection=yes;')
    #cursor = conn.cursor()
    #ufData = cursor.execute('SELECT PersonID FROM dbo.Table_prueba Where PersonID = 2')
    array = pd.read_sql_query('SELECT PersonID,LastName,FirstName,Address,City FROM dbo.Table_prueba', conn)
    print(array)
    #print(ufData[0])

    # cursor.close()
    conn.close() 

if __name__ == "__main__":
   main()