from db import db

class HashtagsPairs(db.Model):
    __tablename__="hastags_pairs"

    id = db.Column(db.Integer, primary_key=True)
    hashtag_id_1=db.Column(db.Integer)#the one with smallest id
    hashtag_id_2 = db.Column(db.Integer)
    count = db.Column(db.Integer)

    def __init__(self, hashtag_id_1, hashtag_id_2):
        self.hashtag_id_1 = hashtag_id_1
        self.hashtag_id_2=hashtag_id_2
        self.count=1


    @classmethod
    def find_by_id(cls, id):
        return HashtagsPairs.query.filter_by(id=id).first()

    @classmethod
    def find_pair(cls, hashtag_id_1, hashtag_id_2):
        return HashtagsPairs.query.filter_by(hashtag_id_1=hashtag_id_1,hashtag_id_2=hashtag_id_2 ).first()
    @classmethod
    def add_or_create_pair(cls, hashtag_id_1, hashtag_id_2):
        pair=HashtagsPairs.query.filter_by(hashtag_id_1=hashtag_id_1).filter_by(hashtag_id_2=hashtag_id_2).first()
        if pair:
            pair.count=pair.count+1
        else:
            pair=HashtagsPairs(hashtag_id_1, hashtag_id_2)
        pair.save_to_db()

    @classmethod
    def find_by_name(cls, name):
        return HashtagsPairs.query.filter_by(name=name).first()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
