from flask_restful import fields,reqparse
# class loginModel():
#     logindict={'username':fields.String(None),'password':fields.String(None)}
#     username= str(None)
#     password =str(None)

# class AdminUser():
#     save = {'id':fields.Integer(None),'name':fields.String(None)}
#     id= str(None)
#     name = str(None)

class Admin:
    def __init__(self):
        self._id = None
        self._created_by_id = None
        self._name = None
        self._mobile = None
        self._email = None
        self._deleted = None
        self._deleted_by_id=None
        self._status = None

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        if isinstance(value, int) or  value is "":
            self._id = value
        else:
            raise ValueError("Id must be an integer")
    
    @property
    def created_by_id(self):
        return self._created_by_id
        
    @created_by_id.setter
    def created_by_id(self, value):
        if isinstance(value, int) or value is "":
            self._created_by_id = value
        else:
            raise ValueError("created_by_id must be integer")
        
    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            raise ValueError("Name must be string")

    @property
    def mobile(self):
        return self._mobile
    
    @mobile.setter
    def mobile(self, value):
        if isinstance(value, str):
            self._mobile = value
        else:
            raise ValueError("Add mobile number properly")

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if isinstance(value, str):
            self._email = value
        else:
            raise ValueError("Email must be string")
        
    @property
    def deleted(self):
        return self._deleted

    @deleted.setter
    def deleted(self, value):
        if isinstance(value, bool) or value is None:
            self._deleted = value
        else:
            raise ValueError("Invalid value assigned to 'deleted' property. Expected bool or None.")
        
    
    @property
    def deleted_by_id(self):
        return self._deleted_by_id

    @deleted_by_id.setter
    def deleted_by_id(self, value):
        if isinstance(value, int):
            self._deleted_by_id= value
        else:
            raise ValueError("Deleted_by_id must be integer")
    
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if isinstance(value, bool) or value is None:
            self._status = value
        else:
            raise ValueError("Invalid value assigned to 'deleted' property. Expected bool or None.")

