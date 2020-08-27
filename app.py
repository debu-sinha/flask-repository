from flask import Flask
from flask_restful import  Api
from flask_jwt_extended import JWTManager

from resource.user import User_Register, User_Login
from resource.item import Item, Items
from resource.store import Store, StoreList

from createtable import reset_database


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
api = Api(app)


app.config['JWT_SECRET_KEY'] = '<testkey>' 
jwt = JWTManager(app)

api.add_resource(Item,'/item/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(User_Register, '/register')
api.add_resource(User_Login, '/login')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    #reset_database()
    app.run(port = 5000, debug = True)
    