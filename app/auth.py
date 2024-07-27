from flask import Blueprint, request, jsonify
import jwt
import datetime

bp = Blueprint('auth', __name__)

SECRET_KEY = 'your_secret_key'

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    # Validate user credentials and generate JWT token
    token = jwt.encode({
        'user_id': 1,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }, SECRET_KEY)
    return jsonify({'token': token})

# Define other authentication endpoints here
