from flask import Blueprint
from flask_restful import Api

from stegano.api.resources import (
    UserResource,
    UsersResource
)


blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint)


api.add_resource(UserResource, '/users/<uid>')
api.add_resource(UsersResource, '/users')
