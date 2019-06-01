from flask_restful import Resource, request
import time
from models.users import UserModel
from models.objects import ObjectModel
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.hashtagObjects import HashtagObjects
from models.allHashtags import AllHashtags


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
        object_id=request.args.get('object_id')
        current_user=get_jwt_identity()
        user=UserModel.find_by_id(current_user)
        if user:
            i=ObjectModel.find_by_id(object_id)
            if i:
                if i.owner_id != user.id:
                    return "non hai accesso a questo elemento", 407
                hashtot=[]
                hashtags=HashtagObjects.find_by_object_id(object_id)
                for i in hashtags:
                    k=AllHashtags.find_by_id(i)
                    hashtot.append("hashtag_id"=i.id,
                                   "hashtag_name"=i.name,
                                   "total_times_used"=i.total_times_used)
                object={"name":i.name,
                        "description":i.description,
                        "value":i.object_value,
                        "currency":"TODO",
                        "must_be_returned":i.must_be_returned,
                        "must_be_returned_date":i.must_be_returned_date,
                        "shipping_possible":i.shipping_possible,
                        "is_away":i.is_away,
                        "keeper":"TODO",
                        "id":i.id,
                        "hashtags":hashtot
                        }
                return object, 200
            return "object does not exist", 402
        return "user does not exist", 401
