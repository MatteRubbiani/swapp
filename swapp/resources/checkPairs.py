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
            b.append(i.__dict__)
        return b
