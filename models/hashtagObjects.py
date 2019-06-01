from db import db

class HashtagObjects(db.Model):
    __tablename__="hastag_objects"

    id = db.Column(db.Integer, primary_key=True)
    hashtag_id=db.Column(db.Integer)#the one with smallest id
    object_id=db.Column(db.Integer)

    def __init__(self, hashtag_id_1, object_id):
        self.hashtag_id= hashtag_id_1
        self.object_id=object_id


    @classmethod
    def find_by_id(cls, id):
        return HashtagObjects.query.filter_by(id=id).first()

    @classmethod
    def find_by_object_id(cls, object_id):
        b=[]
        a= HashtagObjects.query.filter_by(object_id=object_id)
        for i in a:
            b.append(i.hashtag_id)
        return b





    @classmethod
    def find_by_name(cls, name):
        return HashtagObjects.query.filter_by(name=name).first()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
