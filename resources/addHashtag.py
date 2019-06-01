from flask_restful import Resource, request
import time
from flask_jwt_extended import jwt_required, get_jwt_identity


from models.users import UserModel
from models.objects import ObjectModel
from models.hashtagObjects import HashtagObjects
from models.allHashtags import AllHashtags
from models.hashtagsPairs import HashtagsPairs

class AddHashtag(Resource):

    @jwt_required
    def post(self):
        id=request.args.get('object_id')
        hashtag_name=request.args.get('hashtag')

        current_user=get_jwt_identity()
        user=UserModel.find_by_id(current_user)
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
                hashtagsPairs.add_or_create_pair(a, b)
            return "hashtag added successfully", 200
