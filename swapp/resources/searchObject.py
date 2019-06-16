from flask_restful import Resource, request
from flask_jwt_extended import jwt_required, get_jwt_identity
import difflib


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
        hashtag = AllHashtags.find_by_name(hashtag_name)
        total = []
        if hashtag_name == "":
            all=ObjectModel.find_all()
            for l in all:
                user=UserModel.find_by_id(l.owner_id)
                #devi trovare la posizione dell'oggetto... per il momento (16/06/19), non si possono ancora fare gli scambi quindi metto la posizione dell'utente

                total.append({'name': l.name,
                   'description': l.description,
                   'posizione': user.city,
                   'value': l.object_value,
                   "id":l.id})
            return total

        hashtag = AllHashtags.find_by_name(hashtag_name)
        if hashtag is None:
            return [{"name": "HASHTAG INESISTENTE",
            "description":"",
            "posizione":"mmm",
            "value":0
            }]

        all = HashtagObjects.find_objects_by_hashtag_id(hashtag.id)
        #metti in ordine di posizione prima di iterare
        for a in all:
            l = ObjectModel.find_by_id(a)
            user=UserModel.find_by_id(l.owner_id)
            #devi trovare la posizione dell'oggetto... per il momento (16/06/19), non si possono ancora fare gli scambi quindi metto la posizione dell'utente
            
            total.append({'name': l.name,
               'description': l.description,
               'posizione': user.city,
               'value': l.object_value,
               "id":l.id})
        possible_matches = HashtagsPairs.find_matching_hashtags(hashtag.id)
        possible_other_objects=[]
        for i in possible_matches:
            objs=HashtagObjects.find_objects_by_hashtag_id(i)
            for j in objs:
                hashtags=HashtagObjects.find_by_object_id(j)
                if hashtag.id in hashtags:
                    continue
                object_points=0
                for k in hashtags:
                    a=HashtagsPairs.find_pair(k, hashtag.id)
                    if a is None:
                        a=HashtagsPairs.find_pair(hashtag.id, k)
                    if a is None:
                        continue
                    object_points=object_points+a.count

                object_with_points= ObjectWithPoints(j, object_points)
                if object_with_points in possible_other_objects:
                    break
                possible_other_objects.append(object_with_points)

        d=sorted(possible_other_objects, key=lambda x: x.points, reverse=True)
        real_objects=[]
        for l in d:
            objl=ObjectModel.find_by_id(l.object_id)
            real_objects.append({'name': objl.name,
               'description': objl.description,
               'location': 'Modena',
               'value': objl.object_value})
        return total+real_objects


class SearchByName(Resource):

    @jwt_required
    def get(self):
        name=request.args.get('name')
        max_distance=request.args.get('distance')
        all=ObjectModel.find_all()
        b=[]
        for a in all:
            if a.name:
                seq = difflib.SequenceMatcher(None, a.name, name)
                d = seq.ratio()*100
                b.append({
                "object":a,
                "simily":d
                })
        c = sorted(b, key=lambda x: x["simily"], reverse=True)
        final=[]
        for l in c:
            object=l["object"]
            final.append({
                "name":object.name,
                "description":object.description,
                "location":"Modena",
                "value":object.object_value

            })
        return final


class ObjectWithSim():
    object=None
    simily=0

    def __init__(self, hashtag_name, object):
        self.object=object
        #metti tutto in minuscolo prima di confrontare che senno non funziona tanto bene
        seq = difflib.SequenceMatcher(None, object.name, hashtag_name)
        d = seq.ratio()*100
        self.simily=d


class ObjectWithPoints():
    object_id=0
    points=0
    def __init__ (self, a, b):
        self.object_id=a
        self.points=b
