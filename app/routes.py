from flask import Blueprint, request, jsonify
from .models import db, User

bp = Blueprint('routes', __name__)

@bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'], password_hash=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

# Define other endpoints here
