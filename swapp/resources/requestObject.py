from flask_restful import Resource, request
from flask_jwt_extended import jwt_required, get_jwt_identity



from models.users import UserModel
from models.objects import ObjectModel
from models.hashtagObjects import HashtagObjects
from models.allHashtags import AllHashtags
from models.hashtagsPairs import HashtagsPairs
from models.objectRequests import ObjectRequests
from models.objectCosts import ObjectCosts



class RequestObject(Resource):

    @jwt_required
    def post(self):
        number_of_times = request.args.get('number_of_times')
        object_id = int(request.args.get('object_id'))
        user=UserModel.find_by_id(l.owner_id)
        if user:
            object=ObjectModel.find_by_id(object_id)
            if object is None:
                return "object does not exist", 403
            if object.is_requested:
                return "object is already requested, you shouldn't be here", 406
            if not object.is_borrowable:
                return "object isn't borrowable, you shouldn't be here", 406
            object_cost=ObjectCosts.find_by_object_id(object_id)
            if object_cost is None:
                return "l'oggetto non ha costi e' un casino non dovresti essere qui", 406

            requestModel=ObjectRequests(object_id, user.id, object.keeper_id, object_cost.id, int(number_of_times))
            requestModel.save_to_db()
            object.is_requested=True
            object.save_to_db()
            return "object requested successfully", 200
        return "user does not exist", 409


    @jwt_required
    def delete(self):
        object_id = int(request.args.get('object_id'))
        user=UserModel.find_by_id(l.owner_id)
        if user:
            object=ObjectModel.find_by_id(object_id)
            if object is None:
                return "object does not exist", 403

            requestModel=ObjectRequests.find_by_object_id(object_id)
            if requestModel and requestModel.from_user_id==user.id:
                requestModel.was_deleted==True
                requestModel.save_to_db()
                object.is_requested=False
                object.save_to_db()
            return "object un-requested successfully", 200
            
        return "user does not exist", 409
