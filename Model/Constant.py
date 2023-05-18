import pymssql
# import pyodbc

# class DatabaseConstant:    
#     DatabaseName="Local_Data"
# DatabaseConnectionString='Driver={SQL Server};Server=DESKTOP-A4FVATT\\SQLEXPRESS;Database=local;Trusted_Connection=yes;'
# DatabaseConnectionString="Server= 'DESKTOP-A4FVATT\\SQLEXPRESS', user = 'sa' , password = 'sasql@123' , databse = 'local'"

try:
    # Create a connection object
    # connection = pyodbc.connect(DatabaseConnectionString)
    connection = pymssql.connect(server='DESKTOP-A4FVATT\SQLEXPRESS',user ='sa',password='sasql@123',database='local')

    # If the connection is successful, this line will be executed
    print('Connection established successfully')
except pymssql.Error as e:
    # If an exception is raised while connecting, this block will be executed
    print(f'Connection failed. Error message: {e}')