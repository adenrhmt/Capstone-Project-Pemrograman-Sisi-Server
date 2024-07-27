from flask import Blueprint, request, jsonify
from .models import db, User, Product, Order, OrderItem

bp = Blueprint('routes', __name__)

@bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'])
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@bp.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    new_product = Product(name=data['name'], price=data['price'], stock=data['stock'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product created successfully'}), 201

@bp.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    new_order = Order(user_id=data['user_id'], total_price=data['total_price'])
    db.session.add(new_order)
    db.session.commit()
    return jsonify({'message': 'Order created successfully'}), 201

@bp.route('/order_items', methods=['POST'])
def create_order_item():
    data = request.get_json()
    new_order_item = OrderItem(order_id=data['order_id'], product_id=data['product_id'], quantity=data['quantity'], price=data['price'])
    db.session.add(new_order_item)
    db.session.commit()
    return jsonify({'message': 'Order Item created successfully'}), 201

# Define other endpoints here
