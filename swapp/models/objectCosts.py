from db import db
import time

class ObjectCostsModel(db.Model):
    __tablename__="object_costs"

    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50))
    object_id = db.Column(db.Integer)
    rental_period_id = db.Column(db.Integer)
    rental_cost = db.Column(db.Integer)
    rental_currency_id= db.Column(db.Integer)
    notes=db.Column(db.String(200))

    def __init__(self, description, owner_id, object_value, currency_id, must_be_returned, must_be_returned_date, shipping_possible):
        self.name = name
        self.object_id=object_id
        self.rental_period_id=rental_period_id
        self.rental_cost=rental_cost
        self.rental_currency_id=rental_currency_id
        self.notes=notes


    @classmethod
    def find_by_id(cls, id):
        return ObjectCostsModel.query.filter_by(id=id).first()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
