from flask_restful import Resource, request
import time
from models.users import UserModel
from flask_jwt_extended import jwt_required, get_jwt_identity

class GetMailUsername(Resource):
    @jwt_required
    def get (self):
        current_user=get_jwt_identity()
        user=UserModel.find_by_id(current_user)
        if user:
            return {"mail":user.mail,
                    "username":user.username}
        return "user does not exist", 401

class GetAllDetails(Resource):
    @jwt_required
    def get (self):
        current_user=get_jwt_identity()
        user=UserModel.find_by_id(current_user)
        if user:
            return {"mail":user.mail,
                    "username":user.username,
                    "phone_number":user.telephone_number,
                    "address": user.address,
                    "country":user.country_id,
                    "city":user.city,
                    "country_id":user.country_id,
                    "language_id":user.language_id,
                    "zip_code":user.zip_code,
                    "privacy_setting": user.privacy_setting}
        return "user does not exist", 401
