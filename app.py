import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from datetime import timedelta
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager

from resources.register import Register
from resources.login import Login
from resources.refreshToken import RefreshToken
from resources.getDetails import GetAllDetails, GetMailUsername
from resources.createObject import CreateObject
from resources.userOwnedObjects import UserOwnedObjectsList, UserOwnedObject
from resources.modifyUser import ModifyUser
from resources.addHashtag import AddHashtag


app= Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]=os.environ.get("DATABASE_URL","sqlite:///data.db")
app.config["SQLALCHEMY_TRAK_MODIFICATIONS"]=False
app.config["PROPAGATE_EXCEPTIONS"]=True
app.secret_key="Matteo"
api=Api(app)


jwt = JWTManager (app)


#app.config['JWT_AUTH_USERNAME_KEY'] = 'mail'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(hours=5)

app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(weeks=100)
"""
@app.before_first_request
def create_table():
    db.create_all()
"""




api.add_resource(Register, "/register")
api.add_resource(Login, "/login")
api.add_resource(RefreshToken, "/refresh_token")

api.add_resource(ModifyUser, "/user/modify")

api.add_resource(GetAllDetails, "/user/details/all")
api.add_resource(GetMailUsername, "/user/details/mail_username")

api.add_resource(CreateObject, "/object/create")
api.add_resource(AddHashtag, "/object/hashtag/add")


api.add_resource(UserOwnedObjectsList, "/objects/owner/list")
api.add_resource(UserOwnedObject, "/object/owner")


if __name__=="__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
