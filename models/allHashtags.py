from db import db
import time

class AllHashtags(db.Model):
    __tablename__="all_hashtags"

    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50))
    total_times_used = db.Column(db.Integer)

    def __init__(self, name):
        self.name = name
        self.total_times_used=1


    @classmethod
    def find_by_id(cls, id):
        return AllHashtags.query.filter_by(id=id).first()


    @classmethod
    def find_by_name(cls, name):
        return AllHashtags.query.filter_by(name=name).first()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
