from db import db
import time

class ObjectModel(db.Model):
    __tablename__="objects_requests"

    id = db.Column(db.Integer, primary_key=True)
    object_id=db.Column(db.String(50))
    from_user_id = db.Column(db.String(500))
    to_user_id= db.Column(db.Integer)
    request_type_id=db.Column(db.Integer) #
    currency_id=db.Column(db.Integer)
    must_be_returned =db.Column(db.Boolean)
    must_be_returned_date =db.Column(db.Integer)
    shipping_possible=db.Column(db.Boolean)
    is_away=db.Column(db.Boolean)
    is_borrowable=db.Column(db.Boolean)
    is_requested=db.Column(db.Boolean)

    def __init__(self, name, description, owner_id, object_value, currency_id, must_be_returned, must_be_returned_date, shipping_possible, is_borrowable):
        self.name = name
        self.description= description
        self.owner_id=owner_id
        self.object_value=object_value
        self.currency_id=currency_id
        self.must_be_returned=bool(must_be_returned)
        self.must_be_returned_date=must_be_returned_date
        self.shipping_possible=bool(shipping_possible)
        self.is_away=False
        self.is_borrowable=bool(is_borrowable)
        self.is_requested=False
