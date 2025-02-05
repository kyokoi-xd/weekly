from flask import Blueprint, request, jsonify
from database import db
from models import User

app_routes = Blueprint('app_routes', __name__)

@app_routes.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    name = data.get('name')

    if not name:
        return jsonify({'error': 'Name are required.'}), 400
    
    try:
        new_user = User(name=name)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User added successfully', 'id': new_user.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'User not added successfully', 'id': new_user.id}), 201

@app_routes.route('/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        users_list = [{'id': u.id, 'name': u.name} for u in users]
        return jsonify(users_list)
    except Exception as e:
        error_str = str(e)
        return jsonify({"error": "Unicode decoding error", "details": error_str}), 500
    

@app_routes.route('/users/<int:id>', methods=['GET'])
def get_user_by_id(id):
    user_by_filter = User.query.filter_by(id=id).first()
    if user_by_filter:
        return jsonify(vars(user_by_filter))
    return jsonify({"error": "User not found"}), 404

@app_routes.route('/users/<int:id>', methods=['PUT'])
def update_user_by_id(id):
    data = request.get_json()
    new_name = data.get('name')
    try:
        update_user = User.query.filter_by(id=id).first()
        update_user.name = new_name
        db.session.commit()
        return jsonify({'message': 'User update successfully', 'id': update_user.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'User not update successfully', 'id': update_user.id}), 201
    
@app_routes.route('/users/<id>', methods=['DELETE'])
def delete_user_by_id(id):
    try:
        delete_user = User.query.get(id)
        if delete_user:
            db.session.delete(delete_user)
            db.session.commit()
            return jsonify({'message': 'User deleted successfully', 'id': delete_user.id}), 201
        return jsonify({"error": "User not found"}), 404
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'User deleted unsuccessfuly', 'id': delete_user.id}), 201