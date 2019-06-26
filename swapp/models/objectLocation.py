from db import db
import time

class ObjectLocation(db.Model):
    __tablename__="objects_location"
ID Long Integer 4
object_id Long Integer 4
user_id Short Text 255
received_date_time Date With Time 8
current_location Yes/No 1
location_country_id Short Text 255
location_city Short Text 255
location_address Short Text 255
local_pickup_possible Yes/No 1
available_from_date_time Date With Time 8
pickup_notes Long Text -

    id = db.Column(db.Integer, primary_key=True)
    object_id=db.Column(db.String(50))
    user_id = db.Column(db.String(500))
    received_date= db.Column(db.Integer)
    current_location=db.Column(db.Integer)
    longitude=db.Column(db.Integer)
    must_be_returned =db.Column(db.Boolean)
    must_be_returned_date =db.Column(db.Integer)
    shipping_possible=db.Column(db.Boolean)
    is_away=db.Column(db.Boolean)
    is_borrowable=db.Column(db.Boolean)
    is_requested=db.Column(db.Boolean)
    creation_date=db.Column(db.Integer)


    def __init__(self, name, description, owne
