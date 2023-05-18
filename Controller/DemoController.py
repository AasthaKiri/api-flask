# from flask_restful import Resource, reqparse
# from flask_apispec.views import MethodResource
# from Model.ApiException import handleException
from Model.Return import *
from Model.Database import *
from Model.Bean import *
from flask import Blueprint, jsonify,request,json
from BAL.DemoBAL import *

api = Blueprint('api', __name__)

# @api.route('/getAdminUser')
# def getCursor():
#         connection=None
#         data=None
#         try:
#             connection = pyodbc.connect(DatabaseConnectionString)
#             cursor = connection.cursor()
#             cursor.execute('select * from admin_users')
#             data=cursor.fetchall()   
#             data = [dict(zip([column[0] for column in cursor.description], row)) for row in data]

#             connection.close()
#             return jsonify(data)
#         except Exception as e:
#             return jsonify({'error': str(e)}), 500 
        
# @api.route('/getCountry')
# def getCountry():
#         connection=None
#         data=None
#         try:
#             connection = pyodbc.connect(DatabaseConnectionString)
#             cursor = connection.cursor()
#             cursor.execute('select * from country')
#             data=cursor.fetchall()   
#             data = [dict(zip([column[0] for column in cursor.description], row)) for row in data]

#             connection.close()
#             return jsonify(data)
#         except Exception as e:
#             return jsonify({'error': str(e)}), 500 

@api.route('/getState')
def getState():
       query = 'select * from state'
       output = Database.getCursor(query)
# This will give error of 201 as the data we are getting is json format and not 200
       if(output!="200"):
                return Return.returnResponse("Some Internal Issue Occured while saving data ",201)
       return Return.returnResponse(output,200)
       
@api.route('/demo')
def getDemo():
      data = getAdmin()
      return data


# without validation
# @api.route('/saveDemo',methods=['POST'])
# def saveDemo():
#       id=request.json['id']
#       name = request.json['name']
#       data = saveAdmin(id,name)
#       return  data


# with validation
@api.route('/saveDemo', methods=['POST'])
def saveDemo():
    try:
        save = Admin()
        save.id = request.json['id']
        save.name = request.json['name']

        # id = request.json['id']
        # name = request.json['name']
        # Perform validation
        # if not isinstance(save.id, int):
        #     return jsonify({'error': 'ID must be an integer'}), 400

        # if not isinstance(save.name, str):
        #     return jsonify({'error': 'Name must be a string'}), 400
        if save.id is None or save.id == "":
            return jsonify({'error': 'Please enter your id'}), 400
        # return result

        if save.name is None or save.name == "":
            return jsonify({'error': 'Please enter your name'}), 400
        # return result
        
        result = saveAdmin(save.id, save.name)
        if result =='"True"':
             return Return.returnResponse(200,'Data added sucessfully')
        else:
             return Return.returnResponse(201,result)
       
      
    except Exception as e:
        return jsonify({'error': str(e)}), 500
        # print(e)
    
# @api.route('/saveDemo', methods=['POST'])
# def saveDemo():
#     # Get the JSON data from the request body
#     datajson = request.get_json()

#     # Extract the values of the "id" and "name" parameters from the JSON data
#     id = datajson['id']
#     name = datajson['name']
    
#     # Call the stored procedure in SQL Server using pyodbc
#     cursor = connection.cursor()
    
#     cursor.execute("{CALL spDemo(?,?)}" ,(id,name))
#     connection.commit()
#     # connection.close()

#     # data = cursor.fetchall()
#     # Return the output message from the stored procedure to the client as a JSON response
#     return jsonify('200')

