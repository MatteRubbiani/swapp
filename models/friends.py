from db import db


class FriendModel(db.Model):
    __tablename__="amici"

    id = db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer)
    orario_id=db.Column(db.Integer)
    data=db.Column(db.String(30))





    def __init__(self, id, user_id, orario_id, data):
        self.id=id
        self.user_id=user_id
        self.orario_id=orario_id
        self.data=data

    @classmethod
    def find_by_user_id(cls, user_id):
        return FriendModel.query.filter_by(user_id=user_id).first()

    @classmethod
    def find_by_orario_id(cls, user_id, orario_id):
        return FriendModel.query.filter_by(user_id=user_id, orario_id=orario_id).first()




    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


def delete_slots_by_user_id(user_id):
    slots=FriendModel.query.filter_by(user_id=user_id)
    for i in slots:
        i.delete_from_db()
