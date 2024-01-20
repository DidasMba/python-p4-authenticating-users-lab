from flask import session, request
from flask_restful import Resource

from models import User  # Assuming you have a User model

class LoginResource(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')

        # Retrieve the user by username
        user = User.query.filter_by(username=username).first()

        if user:
            # Set the session's user_id value to the user's id
            session['user_id'] = user.id
            return user.serialize(), 200
        else:
            return {'error': 'Invalid username'}, 401
        
class LogoutResource(Resource):
    def delete(self):
        # Remove the user_id value from the session
        session.pop('user_id', None)
        return {}, 204

class CheckSessionResource(Resource):
    def get(self):
        # Retrieve the user_id value from the session
        user_id = session.get('user_id')

        if user_id:
            # If the session has a user_id, return the user as JSON
            user = User.query.get(user_id)
            return user.serialize(), 200
        else:
            # If the session does not have a user_id, return Unauthorized
            return {}, 401
