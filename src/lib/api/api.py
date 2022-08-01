import time
from flask import Flask, jsonify, redirect, request, url_for
import requests
from flask_restful import Resource, reqparse, Api
from flask import Flask

app = Flask(__name__)
api = Api(app)

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

group_info_args = reqparse.RequestParser()

group_info_args.add_argument("UserName",type=str,help = "first") 
group_info_args.add_argument("Password",type=str,help = "last") 
group_info_args.add_argument("uEmail",type=str,help = "email")  

User = {}
#Handles User Creation
class UserCreate(Resource):
    

    def get(self):
        args = group_info_args.parse_args()
        return User

    def post(self):
        args = group_info_args.parse_args()
        User['UserName'] = args['UserName']
        User['Password'] = args['Password']
        User['uEmail'] = args['uEmail']

        return args

api.add_resource(UserCreate,'/createUser')


if __name__ == '__main__':
    app.run(debug=True)