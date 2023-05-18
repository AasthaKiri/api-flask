from flask import Flask, jsonify, request, make_response,jsonify, json
class Return:
    @staticmethod
    def returnResponse(code,object):
       
        response = jsonify(
                    {
                        "response_code":json.dumps(code),
                        "obj": json.loads(json.dumps(object))
                    }
                )
            
        response.headers["Content-Type"] = "application/json"
        
        return response