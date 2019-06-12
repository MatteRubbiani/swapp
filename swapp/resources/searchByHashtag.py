from flask_restful import Resource, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.users import UserModel
from models.objects import ObjectModel
from models.hashtagObjects import HashtagObjects
from models.allHashtags import AllHashtags
from models.hashtagsPairs import HashtagsPairs

class SearchByHashtag(Resource):

    @jwt_required
    def get(self):
        hashtag_name = request.args.get('hashtag')
        max_distance = request.args.get('distance')
        hashtag = allHashtags.find_by_name(hashtag_name)
        if hashtag is None:
            return []
        all = HashtagObjects.find_objects_by_hashtag_id(hashtag.id)
        total = []
        #metti in ordine di posizione prima di iterare
        for a in all:
            l = ObjectModel.find_by_id(a)
            total.append({'name': l.name,
               'description': l.description,
               'posizione': 'Modena',
               'value': l.object_value})
        possible_matches = HashtagsPairs.find_matching_hashtags(hashtag.id)
        possible_other_objects=[]
        for i in possible_matches:
            objs=HashtagObjects.find_objects_by_hashtag_id(hashtag.id)
            for j in objs:
                if j in possible_other_objects:
                    break
                hashtags=HashtagObjects.find_by_object_id(j)
                if hashtag.id in hashtags:
                    break
                object_points=0
                for k in hashtags:
                    hashtag_points=HashtagsPairs.find_pair(k, hashtag_id).count
                    object_points=object_points+hashtag_points
                object_with_points= ObjectWithPoints(k, object_points)
                possible_other_objects.append(object_with_points)
        d=sorted(possible_other_objects, key=lambda x: x.points, reverse=True)
        return total+d




        return total
class ObjectWithPoints():
    object_id=0
    points=0
    def __init__ (self, a, b):
        self.object_id=a
        self.points=b
