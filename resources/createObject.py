from flask_restful import Resource, request
import time
from models.users import UserModel
from models.objects import ObjectModel
from flask_jwt_extended import jwt_required, get_jwt_identity

class CreateObject(Resource):
    @jwt_required
    def post (self):
        name=request.args.get('name')
        description=request.args.get('description')
        object_value=request.args.get('object_value')        must_be_returned=request.args.get('must_be_returned')
        must_be_returned_date=request.args.get('must_be_returned_date')
        shipping_possible=request.args.get('shipping_possible')
        current_user=get_jwt_identity()
        user=UserModel.find_by_id(current_user)
        if user:
            currency_id=1
            shipping_possible=True
            object=ObjectModel(name, description, user.id, object_value, None, must_be_returned, must_be_returned_date, shipping_possible)
            object.save_to_db()
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
            a.save_to_db()

            return "ok", 200
        return "user does not exist", 401
