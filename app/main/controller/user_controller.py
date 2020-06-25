from flask import request
from flask_restplus import Resource
from ..util.dto import UserDto

api = UserDto.api
_user = UserDto.user


@api.route('/')
class User(Resource):

    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        params = request.form

        return params
