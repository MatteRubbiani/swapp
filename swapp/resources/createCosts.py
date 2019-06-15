from flask_restful import Resource, request
import time
from models.users import UserModel
from models.objects import ObjectModel
from models.hashtagObjects import HashtagObjects
from models.allHashtags import AllHashtags
from models.hashtagsPairs import HashtagsPairs
from models.objectCosts import ObjectCostsModel

from flask_jwt_extended import jwt_required, get_jwt_identity
class CreateCosts(Resource):

    @jwt_required
    def put (self):
        object_id=request.args.get('object_id')
        rental_period_id=request.args.get('rental_period_id')
        rental_cost=request.args.get('rental_cost')

        current_user=get_jwt_identity()
        user=UserModel.find_by_id(current_user)
        if user:
            p=ObjectCostsModel.find_by_object_id(object_id)
            if p is None:
                return "mmmmh", 409
            p.rental_period_id=rental_period_id
            p.rental_cost=rental_cost
            p.save_to_db()
            return "rental cost modified correctly"
        return "user does not exist", 401
