from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from models.item import ItemModel

class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help='srice cannot be empty!')
    parser.add_argument('store_id', type=int, required=True, help='store_id cannot be empty!')

    def get(self, name):
        try:
            item = ItemModel.find_item_by_name(name)
            if item:
                return item.json(), 200
            return {'message': 'item not found!'}, 400
        except Exception as e:
            return {'message': 'Internal server error occured {}'.format(e)}, 500    
  

    @jwt_required
    def post(self, name):

        item = ItemModel.find_item_by_name(name)
        if item:
            return {'message': 'an item with name {} already exist!'.format(item.name)}, 400
        args = Item.parser.parse_args()
        item = ItemModel(name, args.get('price'), args.get('store_id'))
        try:
            item.upsert()
            return item.json(), 201
        except Exception as e:
            return {'message': 'Internal server error occured {}'.format(e)}, 500      

    @jwt_required
    def delete(self, name):
        try:
            item = ItemModel.find_item_by_name(name)
            if item:
                item.delete()
                return {'message': 'item deleted'}, 200
            else:
                 return {'message': 'no item with name {} found'.format(name)}, 400   
        except Exception as e:
            return {'message': 'Internal server error occured {}'.format(e)}, 500   
        
   
    @jwt_required
    def put(self, name):
        
        args = Item.parser.parse_args()
        item = ItemModel(name, args.get('price'), args.get('store_id'))
        try:
            item.upsert()
            return item.json(), 201
        except Exception as e:
            print(e)
            return {'message': 'Internal server error occured {}'.format(e)}, 500      


class Items(Resource):

    def get(self):
        try:
            items = [item.json() for item in ItemModel.get_all_items()]
            return {'items': items}, 201
        except Exception as e:
            return {'message': 'Internal server error occured {}'.format(e)}, 500      
