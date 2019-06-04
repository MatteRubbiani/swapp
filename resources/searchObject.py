from flask_restful import Resource, request
from flask_jwt_extended import jwt_required, get_jwt_identity
import difflib


from models.users import UserModel
from models.objects import ObjectModel
from models.hashtagObjects import HashtagObjects
from models.allHashtags import AllHashtags
from models.hashtagsPairs import HashtagsPairs


class ObjectWithSim():
    object=None
    simily=0

    def __init__(hashtag_name, object):
        self.object_id=object
        seq = difflib.SequenceMatcher(None,object.name, hashtag_name)
        d = seq.ratio()*100
        self.simily=d


class SearchByHashtag(Resource):

    @jwt_required
    def get(self):
        hashtag_name=request.args.get('hashtag')
        max_distance=request.args.get('distance')

        hashtag=AllHashtags.find_by_name(hashtag_name)
        if hashtag is None:
            return []
        all=HashtagObjects.find_objects_by_hashtag_id(hashtag.id)
        #for i in all:
            #calcola la distanza e valuta se rispetta il parametro
            #metti prima i liberi poi calcola preiodo entro il quale dovrebbe essere libero
        total=[]
        for a in all:
            l=ObjectModel.find_by_id(a)
            #trova in che posizione e'
            total.append({
                "name":l.name,
                "description":l.description,
                "posizione":"Modena",
                "value":l.object_value

            })
        return total


class SearchByName(Resource):

    @jwt_required
    def get(self):
        hashtag_name=request.args.get('name')
        max_distance=request.args.get('distance')
        all=ObjectModel.find_all()
        b=[]
        for a in all:
            b.append(ObjectWithSim(hashtag_name, a))
        b.sort(key=lambda x: x.simily, reverse=True)
        final=[]
        for l in b:
            final.append({
                "name":l.object.name,
                "description":l.object.description,
                "posizione":"Modena",
                "value":l.object.object_value

            })
