from collections import OrderedDict

from Model.Constant import *
from flask import jsonify,request,json
from datetime import datetime
from Model.Function import *
from Model.Constant import *

def saveAdminUser(id,name,mobile,email):
    try:
        creation_timestamp= str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        password = get_pass()
        cursor = connection.cursor()
        message = cursor.callproc('saveAdminUser',(id,creation_timestamp,1,name,mobile,email,password,pymssql.output(str)))
        # message = cursor.fetchall()
        connection.commit()
        # print(message[[len(message)-1]])
        # print(message)
        return (message[-1])
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500 


def getAdminUserList(flag,deleted,status,id,created_by_id):
    try:
        cursor = connection.cursor()
        cursor.callproc('getAdmin',(flag,deleted,status,id,created_by_id))
        # connection.commit()
        data = cursor.fetchall()
        data = [OrderedDict(zip([column[0] for column in cursor.description], row)) for row in data]
        return jsonify(data)
    
    except Exception as e:
        return jsonify({'error':str(e)}),500
