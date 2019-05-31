from flask_restful import Resource, request
import time
from models.users import UserModel
from models.objects import ObjectModel
from flask_jwt_extended import jwt_required, get_jwt_identity

class UserOwnedObjectsList(Resource):
    @jwt_required
    def get(self):
        current_user=get_jwt_identity()
        user=UserModel.find_by_id(current_user)
        if user:
            a=ObjectModel.find_by_user_id(user.id)
            objects=[]
            for i in a:
                #ricorda di mettere anche i tag
                objects.append({"name":i.name,
                                "description":i.description,
                                "value":i.object_value,
                                "id":i.id
                                })
            return objects, 200
        return "user does not exist", 401


class UserOwnedObject (Resource):
    @jwt_required
    def get(self):
        name=request.args.get('object_name')
        id=request.args.get('object_id')
        current_user=get_jwt_identity()
        user=UserModel.find_by_id(current_user)
        if user:

                return "non hai accesso a questo elemento", 407
            if i:
                i=ObjectModel.find_by_id(id)
                if i.owner_id != user.id:
                object={"name":i.name,
                        "description":i.description,
                        "value":i.object_value,
                        "currency":"TODO",
                        "must_be_returned":i.must_be_returned,
                        "must_be_returned_date":i.must_be_returned_date,
                        "shipping_possible":i.shipping_possible,
                        "is_away":i.is_away,
                        "keeper":"TODO",
                        "id":i.id
                        }
                return object, 200
            return "object does not exist", 402
        return "user does not exist", 401
