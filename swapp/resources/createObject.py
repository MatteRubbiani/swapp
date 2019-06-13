from flask_restful import Resource, request
import time
from models.users import UserModel
from models.objects import ObjectModel
from models.hashtagObjects import HashtagObjects
from models.allHashtags import AllHashtags
from models.hashtagsPairs import HashtagsPairs
from flask_jwt_extended import jwt_required, get_jwt_identity
class CreateObject(Resource):
    @jwt_required
    def post (self):
        name=request.args.get('name')
        description=request.args.get('description')
        object_value=request.args.get('object_value')
        must_be_returned=request.args.get('must_be_returned')
        must_be_returned_date=request.args.get('must_be_returned_date')
        shipping_possible=request.args.get('shipping_possible')
        is_borrowable=request.args.get('is_borrowable')
        hashtags=request.args.get('hashtags')

        current_user=get_jwt_identity()
        user=UserModel.find_by_id(current_user)
        if user:
            currency_id=1
            shipping_possible=True
            object=ObjectModel(name, description, user.id, object_value, None, must_be_returned, must_be_returned_date, shipping_possible, is_borrowable)
            object.save_to_db()
            hashtags_array= hashtags.split(",")
            for i in hashtags_array:
                return i
                add_hashtag(user, object.id, i)
            return object.id
            return "object created successfully", 200
        return "user does not exist", 401


    @jwt_required
    def put (self):
        id=request.args.get('object_id')
        name=request.args.get('name')
        description=request.args.get('description')
        object_value=request.args.get('object_value')
        must_be_returned=request.args.get('must_be_returned')
        must_be_returned_date=request.args.get('must_be_returned_date')
        shipping_possible=request.args.get('shipping_possible')
        is_borrowable=request.args.get('is_borrowable')

        current_user=get_jwt_identity()
        user=UserModel.find_by_id(current_user)
        if user:
            a=ObjectModel.find_by_id(int(id))
            if a is None:
                return "oggetto non esiste", 402
            if not (a.owner_id == user.id):
                return "non sei possessore di questo oggetto (in teoria non dovresti essere qui allora)", 406
            if a.is_away==True:
                return "you can't modify object while it's away", 403
            a.name=name
            a.description= description
            a.object_value=object_value
            a.must_be_returned=bool(must_be_returned)
            a.must_be_returned_date=must_be_returned_date
            a.shipping_possible=bool(shipping_possible)
            a.is_borrowable=bool(is_borrowable)
            a.save_to_db()

            return "ok", 200
        return "user does not exist", 401


def add_hashtag(user, id, hashtag_name):
    if user:
        object=ObjectModel.find_by_id(int(id))
        if object is None:
            return "oggetto non esiste", 402
        if not (object.owner_id == user.id):
            return "non sei possessore di questo oggetto (in teoria non dovresti essere qui allora)", 406
        if object.is_away==True:
            return "you can't modify object while it's away", 403
        hashtag=AllHashtags.find_by_name(hashtag_name)
        all_object_hashtags_id=HashtagObjects.find_by_object_id(object.id)#lo faccio prima cosi non mi da anche se stesso'

        if hashtag is None:
            hashtag=AllHashtags(hashtag_name)
        else:
            if hashtag.id in all_object_hashtags_id:
                return "hashtag gia' associato a questo ogetto", 408
            hashtag.total_times_used=hashtag.total_times_used+1
        hashtag.save_to_db()

        newPair=HashtagObjects(hashtag.id, object.id)
        newPair.save_to_db()
        for i in all_object_hashtags_id:
            if hashtag.id<i:
                a=hashtag.id
                b=i
            else:
                b=hashtag.id
                a=i
            HashtagsPairs.add_or_create_pair(a, b)
        return "hashtag added successfully", 200
