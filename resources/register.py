from flask_restful import Resource, request
from itsdangerous import URLSafeTimedSerializer
import hashlib, uuid
import time
from db import db

from models.users import UserModel
from methods.sendMail import sendmail

class Register(Resource):
    def post(self):
        mail=request.args.get('mail')
        username=request.args.get('username')
        password=request.args.get('password')
        phone=request.args.get('phoneNumber')
        user=UserModel.find_by_mail(mail)
        if user:
            if user.confirmed==True:
                return "mail already taken", 413
            epsw=password.encode('utf-8')
            hashed_password = hashlib.sha512(epsw).hexdigest()
            user.username=username
            user.password=hashed_password
            user.phone_number=phone
            user.creation_date=time.time()
            user.password_change=time.time()
            user.save_to_db()
        else:
            now = time.time()
            epsw=password.encode('utf-8')
            hashed_password = hashlib.sha512(epsw).hexdigest()
            user=UserModel(mail, phone, username, hashed_password)
            user.save_to_db()


        return user.username
        sendmail(mail, username)

        return "user created, to be confirmed", 200
