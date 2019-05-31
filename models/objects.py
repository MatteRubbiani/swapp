from db import db
import time

class ObjectModel(db.Model):
    __tablename__="objects"

    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50))
    description = db.Column(db.String(500))
    owner_id= db.Column(db.Integer)
    object_value=db.Column(db.Integer)
    currency_id=db.Column(db.Integer)
    must_be_returned =db.Column(db.Boolean)
    must_be_returned_date =db.Column(db.Integer)
    shipping_possible=db.Column(db.Boolean)
    is_away=db.Column(db.Boolean)

    def __init__(self, name, description, owner_id, object_value, currency_id, must_be_returned, must_be_returned_date, shipping_possible):
        self.name = name
        self.description= description
        self.owner_id=owner_id
        self.object_value=object_value
        self.currency_id=currency_id
        self.must_be_returned=bool(must_be_returned)
        self.must_be_returned_date=must_be_returned_date
        self.shipping_possible=bool(shipping_possible)
        self.is_away=False


    @classmethod
    def find_by_id(cls, id):
        return ObjectModel.query.filter_by(id=id).first()

    @classmethod
    def find_by_name_and_user_id(cls, user_id, object_name):
        return ObjectModel.query.filter_by(owner_id=user_id, name=object_name).first()

    @classmethod
    def find_by_user_id(cls, user_id):
        array=[]
        a=ObjectModel.query.filter_by(owner_id=user_id)
        for i in a:
            array.append(i)
        return array


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
