from flask_restful import Resource
from models.usuario import UserModel


class User(Resource):

    def get(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            return user.json()
        return {'message': 'User not found.'}, 404     # Not found

    def delete(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            try:
                user.delete_user()
            except:
                return {'message': 'An internal error ocurred trying\
                    to delete user.'}, 500  # Internal Server Error
            return {'message': 'User deleted.'}
        return {'message': 'User not found.'}, 404  # Not found
