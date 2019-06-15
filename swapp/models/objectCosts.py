from db import db
import time

class ObjectCostsModel(db.Model):
    __tablename__="object_costs"

    id = db.Column(db.Integer, primary_key=True)
    object_id = db.Column(db.Integer)
    rental_period_id = db.Column(db.Integer)
    rental_cost = db.Column(db.Integer)
    rental_currency_id= db.Column(db.Integer)

    def __init__(self, object_id, rental_period_id, rental_cost, rental_currency_id):
        self.object_id=object_id
        self.rental_period_id=rental_period_id
        self.rental_cost=rental_cost
        self.rental_currency_id=rental_currency_id


    @classmethod
    def find_by_id(cls, id):
        return ObjectCostsModel.query.filter_by(id=id).first()

    @classmethod
    def find_by_object_id(cls, object_id):
        return ObjectCostsModel.query.filter_by(object_id=object_id).first()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
