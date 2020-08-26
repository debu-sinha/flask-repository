from db import db

class ItemModel(db.Model):

    __tablename__ = 'items'
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))
    price =  db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    @classmethod
    def find_item_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
    
    @classmethod
    def get_all_items(cls):
        return cls.query.all()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def upsert(self):
        item = ItemModel.find_item_by_name(self.name)
        if item:
            item.price = self.price
            db.session.add(item)
        else:    
            db.session.add(self)    
        db.session.commit()  

    def json(self):
        return {'name': self.name, 'price': self.price}     
        