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
    def find_matching_hashtags(cls, hashtag_id):
        a1=HashtagsPairs.query.filter_by(hashtag_id_1=hashtag_id)
        a2=HashtagsPairs.query.filter_by(hashtag_id_2=hashtag_id)
        o=[]
        for i in a1:
            o.append(i)
        for j in a2:
            o.append(j)
        o1=sorted(o, key=lambda x: x.count, reverse=True)
        o2=[]
        for k in o1:
            if k.hashtag_id_1==int(hashtag_id):
                h_id=k.hashtag_id_2
            else:
                h_id=k.hashtag_id_1
            o2.append(int(h_id))
        return o2

    @classmethod
    def find_pair(cls, hashtag_id_1, hashtag_id_2):
        if int(hashtag_id_1)>hashtag_id_2:
            a=hashtag_id_2
            b=hashtag_id_1
        else:
            a=hashtag_id_1
            b=hashtag_id_2
        a=HashtagsPairs.query.filter_by(hashtag_id_1=a,hashtag_id_2=b ).first()
        return a


    @classmethod
    def add_or_create_pair(cls, hashtag_id_1, hashtag_id_2):
        if int(hashtag_id_1)>hashtag_id_2:
            a=hashtag_id_2
            b=hashtag_id_1
        else:
            a=hashtag_id_1
            b=hashtag_id_2

        pair=HashtagsPairs.query.filter_by(hashtag_id_1=a, hashtag_id_2=b).first()
        if pair:
            pair.count=pair.count+1
        else:
            pair=HashtagsPairs(a, b)
        pair.save_to_db()

    @classmethod
    def get_all(cls):
        b=HashtagsPairs.query.filter_by()
        a=[]
        for i in b:
            a.append(i)
        return a

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
