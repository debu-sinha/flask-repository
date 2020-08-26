import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token
from models.user import UserModel

class User_Register(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, help='username cannot be empty!')
        parser.add_argument('password', type=str, required=True, help='password cannot be empty!')
        args = parser.parse_args()

        #prevent duplicate username entry
        if not UserModel.find_by_username(args.get('username')):
            UserModel.create(args.get('username'), args.get('password'))
            return {"message" : "User created successfully."}, 201
        return {"message" : "Username already exists ."}, 400  


class User_Login(Resource):
    
    def post(self):
        from security import authenticate
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, help='Username cannot be empty!')
        parser.add_argument('password', type=str, required=True, help='Password cannot be empty!')
        args = parser.parse_args()

        user = authenticate(username=args.get('username'), password=args.get('password'))
        if user:
            token = create_access_token(identity=args.get('username'), fresh=True)
            return {'access_token': token}, 200
        return {'message': 'Cannot validate Username or Password!'}, 400    






