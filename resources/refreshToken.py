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


class RefreshToken(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user=get_jwt_identity()
        a=get_raw_jwt()
        user=UserModel.find_by_id(current_user)
        #return str(a["iat"])+" "+str(int(time.time()))
        #return str(user.password_change)+" "+str(a["iat"])
        if  a["iat"]>=user.password_change_date:
            expires = datetime.timedelta(days=365)
            new_token=create_access_token(identity=current_user, fresh=False)
            return {"access_token":new_token}
        return "password was changed"
