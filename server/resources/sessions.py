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

