import pyodbc
from Model.Constant import *
from flask import Flask,jsonify

app = Flask(__name__)

# @app.route('/get',methods =['GET'])
# def getCursor():
#         connection=None
#         data=None
#         try:
#             connection = pypyodbc.connect(DatabaseConstant.DatabaseConnectionString)
#             cursor = connection.cursor()
#             cursor.execute('select * from admin_user')
#             data=cursor.fetchall()            
#             connection.close()
#         except Exception as e:
#             return e
#         finally:
#             if(connection!=None):
#                 if(connection.connect==1):
#                     connection.close()

#         return jsonify(data)

@app.route('/get',methods =['GET'])
def getCursor():
        connection=None
        data=None
        try:
            connection = pyodbc.connect(DatabaseConnectionString)
            cursor = connection.cursor()
            cursor.execute('select * from admin_users')
            data=cursor.fetchall()   
            data = [dict(zip([column[0] for column in cursor.description], row)) for row in data]

            connection.close()
            return jsonify(data)
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        

if __name__ == '__main__':
    app.run(debug=True)