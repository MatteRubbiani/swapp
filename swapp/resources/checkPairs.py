from flask_restful import Resource, request
import time
from models.users import UserModel
from models.objects import ObjectModel
from models.hashtagObjects import HashtagObjects
from models.allHashtags import AllHashtags
from models.hashtagsPairs import HashtagsPairs
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.objectCosts import ObjectCostsModel

class CheckPairs(Resource):


    def get (self):
        a=HashtagsPairs.get_all()
        b=[]
        for i in a:
            hashtag1=AllHashtags.find_by_id(i.hashtag_id_1)
            hashtag2=AllHashtags.find_by_id(i.hashtag_id_2)
            b.append({
            "1":hashtag1.name,
            "2":hashtag2.name,
            "count":i.count
            })
        return b

    def post (self):
        id=request.args.get('id')
        return HashtagsPairs.find_matching_hashtags(id)
