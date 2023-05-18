from Model.Return import *
from Model.Bean import *
from flask import Blueprint, jsonify,request,json
from BAL.BALAdminUser import *

admin = Blueprint('api', __name__)

@admin.route('/saveAdminUser', methods=['POST'])
def save():
    try:
        save = Admin()
        save.id = request.json['id']
        save.name = request.json['name']
        save.mobile = request.json['mobile']
        save.email = request.json['email']

        if save.id is None or save.id == "":
            return jsonify({'error': 'Please enter your id'}), 400
        # return result

        if save.name is None or save.name == "":
            return jsonify({'error': 'Please enter your name'}), 400
        
        if save.mobile is None or save.mobile == "":
            return jsonify({'error': 'Please enter your mobile number'}), 400
        # return result

        if save.email is None or save.email == "":
            return jsonify({'error': 'Please enter your email'}), 400
        
        result = saveAdminUser(save.id, save.name,save.mobile,save.email)
        # return result
        if json.dumps(result) =='"TRUE"':
             return Return.returnResponse(200,'Data added sucessfully')
        else:
             return Return.returnResponse(201,result)
      
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@admin.route('/getAdminUsersList',methods = ['POST'])
def get():
    try:
        save = Admin()
        save.status = request.json['status']
        save.id= request.json['id']
        save.created_by_id = request.json['created_by_id']

        result = getAdminUserList('admin',0,save.status,save.id,save.created_by_id)
        return result
    
    except Exception as e:
        return jsonify({'error':str(e)}),500