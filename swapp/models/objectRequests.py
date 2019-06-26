from db import db
import time

class ObjectRequests(db.Model):
    __tablename__="objects_requests"

    id = db.Column(db.Integer, primary_key=True)
    object_id=db.Column(db.String(50))
    from_user_id = db.Column(db.String(500))
    to_user_id= db.Column(db.Integer)
    object_cost_id=db.Column(db.Integer) #fai riferimento alla tabella dei costi
    number_of_times=db.Column(db.Integer)
    request_date =db.Column(db.Integer)
    agreement_is_found=db.Column(db.Boolean)
    agreement_is_found_date=db.Column(db.Integer)
    is_satisfied=db.Column(db.Boolean)
    is_satisfied_date=db.Column(db.Integer)
    was_deleted=db.Column(db.Boolean)



    def __init__(self, object_id, from_user_id, to_user_id, object_cost_id, number_of_times):
        self.object_id = object_id
        self.from_user_id= from_user_id
        self.to_user_id=to_user_id
        self.object_cost_id=object_cost_id
        self.number_of_times=number_of_times
        self.request_date=time.time()
        self.agreement_is_found=False
        self.is_satisfied=False

    @classmethod
    def find_by_id(cls, id):
        return ObjectModel.query.filter_by(id=id).first()

    @classmethod
    def find_by_object_id(cls, user_id, object_name):
        return ObjectModel.query.filter_by(owner_id=user_id, name=object_name).first()

    @classmethod
    def from_user_id(cls, user_id):
        array=[]
        a=ObjectModel.query.filter_by(owner_id=user_id)
        for i in a:
            array.append(i)
        return array

    @classmethod
    def to_user_id(cls, user_id):
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
