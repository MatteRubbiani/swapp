from flask_restful import Resource, request
import hashlib, uuid
import datetime
from datetime import timedelta
import time
from flask_jwt_extended import (create_access_token,
                                create_refresh_token,
                                jwt_refresh_token_required,
                                get_jwt_identity,
                                get_raw_jwt)

from models.users import UserModel


class Login(Resource):
    def post(self):
        mail=request.args.get('mail')
        password=request.args.get('password')
        user=UserModel.find_by_mail(mail)
        epsw=password.encode('utf-8')
        if user and user.password==hashlib.sha512(epsw).hexdigest(): #and user.confirmed==True:
            expires = datetime.timedelta(days=365)
            access_token=create_access_token(identity=user.id, expires_delta=expires, fresh=True)
            refresh_token=create_refresh_token(user.id)
            return {"access_token":access_token,
                "refresh_token":refresh_token
                }, 200
        return {"message":"invalid cresdentials"}, 401
