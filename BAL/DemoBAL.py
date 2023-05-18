from flask_restful import Resource, reqparse
from flask import jsonify,request,json
from Model.Constant import *
from Model.Bean import *

# from Model.Database import connection

def getAdmin():
    try:
        cursor = connection.cursor()
        cursor.execute('getDemo')
        data = cursor.fetchall()
        data = [dict(zip([column[0] for column in cursor.description], row)) for row in data]
        # connection.close()
        return jsonify(data)
    except Exception as e:
            return jsonify({'error': str(e)}), 500 

# SP connection
# def saveAdmin(id,name):
#     try:
#         cursor = connection.cursor()
#         # message = cursor.var(pyodbc.SQL_CHAR, 1000)
#         # output_param = cursor.var(pyodbc.SQL_CHAR, 10)
#         cursor.execute("{CALL spDemo(?,?,?)}" ,(id,name,None))
#         # message = output_param.getvalue()
#         message = cursor.fetchval()
#         connection.commit()

#         # message = cursor.fetchone()[0]
#         return jsonify(message)
#     except Exception as e:
#             return jsonify({'error': str(e)}), 500 
    
def saveAdmin(id,name):
    try:
        cursor = connection.cursor()
        message = cursor.callproc('spDemo',(id,name,pymssql.output(str)))
        # message = cursor.fetchall()
        connection.commit()
        # print(json.dumps(message[-1]))
        return json.dumps(message[-1])
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500 