from db import db
import time

class UserModel(db.Model):
    __tablename__="users"

    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(80))
    mail=db.Column(db.String(80))
    telephone_number=db.Column(db.String(20))
    password=db.Column(db.String(140))
    creation_date=db.Column(db.String(30))
    password_change_date=db.Column(db.Integer)
    confirmed=db.Column(db.Boolean)
    profile_foto=db.Column(db.String(30))
    country_id=db.Column(db.Integer)
    language_id=db.Column(db.Integer)
    feedback_rating=db.Column(db.Integer)
    address=db.Column(db.String(30))
    city=db.Column(db.String(30))
    zip_code=db.Column(db.String(30))
    privacy_setting=db.Column(db.Boolean)
    status=db.Column(db.Integer)
    credit_remaining=db.Column(db.Integer)
    currency_id=db.Column(db.Integer)

    def __init__(self, mail, phone_number, username, password):
        self.mail=mail
        self.username=username
        self.phone_number=phone_number
        self.password=password
        self.confirmed=False
        self.password_change_date=time.time()
        self.creation_date=self.password_change_date

    @classmethod
    def find_by_id(cls, id):
        return UserModel.query.filter_by(id=id).first()

    @classmethod
    def find_by_mail(cls, mail):
        return UserModel.query.filter_by(mail=mail).first()

    def has_completed_account(self):
        if self.telephone_number and self.country_id and self.address and self.city: #and self.zip_code:
            return True
        return False

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
