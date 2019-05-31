from flask_restful import Resource, request
import time
from models.users import UserModel
from flask_jwt_extended import jwt_required, get_jwt_identity

class ModifyUser(Resource):
    @jwt_required
    def post (self):
        username=request.args.get('username')
        telephone_number=request.args.get('telephone_number')
        profile_foto=request.args.get('profile_foto')
        country_id=request.args.get('country_id')
        language_id=request.args.get('language_id')
        address=request.args.get('address')
        city=request.args.get('city')
        zip_code=request.args.get('zip_code')
        privacy_setting=request.args.get('privacy_setting')
        currency_id=request.args.get('currency_id')

        current_user=get_jwt_identity()
        user=UserModel.find_by_id(current_user)

        if user:
            user.telephone_number=telephone_number
            user.username=username
            user.profile_foto=profile_foto
            user.country_id=country_id
            user.language_id=language_id
            user.address=address
            user.city=city
            user.zip_code=zip_code
            user.privacy_setting=bool(privacy_setting)
            user.currency_id=currency_id
            user.save_to_db()
            return "changes applied correctly"
        return "user does not exist", 401
