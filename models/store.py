from db import db

class StoreModel(db.Model):

    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy = 'dynamic')

    def __init__(self, name):
        self.name = name

    @classmethod
    def find_store_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
    
    @classmethod
    def get_all_stores(cls):
        return cls.query.all()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def add(self):
        store = StoreModel.find_store_by_name(self.name)
        if not store:  
            db.session.add(self)    
            db.session.commit()  

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}     
        