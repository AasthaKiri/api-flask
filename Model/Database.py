# # from flask import Flask
# # from flask_sqlalchemy import SQLAlchemy
# # from sqlalchemy.sql import text

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pymssql://sa:sasql@123@DESKTOP-A4FVATT\SQLEXPRESS/Local_Data'
# db = SQLAlchemy(app)

# # app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://<username>:<password>@<Host>:<Port>/LendApp'
# # conn_uri = "mssql+pymssql://<username>:<password>@<servername>/<dbname>"


# SQLALCHEMY_TRACK_MODIFICATIONS = False

import pypyodbc   
from Model.Constant import *
from flask import jsonify

class Database:

     @staticmethod #for inserting data
     def insertData(sql):
        connection=None
        try:
            connection = pypyodbc.connect(DatabaseConnectionString)
            cursor = connection.cursor()
            cursor.execute(sql)
            cursor.commit()
            connection.close()
        except BaseException as e:
            return e
        finally:
            if(connection!=None):
                if(connection.connect==1):
                    connection.close()
        return "200"

     @staticmethod #for getting data
     def getCursor(sql):
        connection=None
        data=None
        try:
            # connection = pyodbc.connect(DatabaseConnectionString)
            cursor = connection.cursor()
            cursor.execute(sql)
            data=cursor.fetchall()  
            data = [dict(zip([column[0] for column in cursor.description], row)) for row in data]
          
            connection.close()
            return '200'
        except Exception as e:
            return jsonify({'error': str(e)}), 500 


