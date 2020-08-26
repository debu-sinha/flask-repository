from flask_restful import Resource
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from models.store import StoreModel

class Store(Resource):

    def get(self, name):
        try:
            store = StoreModel.find_store_by_name(name)
            if store:
                return store.json(), 200
            return {'message': 'Store not found!'}, 400
        except Exception as e:
            return {'message': 'Internal server error occured {}'.format(e)}, 500    
  

    @jwt_required
    def post(self, name):
        store = StoreModel.find_store_by_name(name)
        if store:
            return {'message': 'a store with name {} already exist!'.format(name)}, 400
        try:
            store = StoreModel(name)
            store.add() 
            return store.json(), 201
        except Exception as e:
            return {'message': 'Internal server error occured {}'.format(e)}, 500      

    @jwt_required
    def delete(self, name):
        try:
            store = StoreModel.find_store_by_name(name)
            if store:
                store.delete()
                return {'message': 'Store deleted'}, 200
            else:
                 return {'message': 'no store with name {} found'.format(name)}, 400   
        except Exception as e:
            return {'message': 'Internal server error occured {}'.format(e)}, 500   



class StoreList(Resource):

    def get(self):
        try:
            stores = [store.json() for store in StoreModel.get_all_stores()]
            return {'stores': stores}, 201
        except Exception as e:
            return {'message': 'Internal server error occured {}'.format(e)}, 500      
