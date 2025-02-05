<<<<<<< HEAD
=======

>>>>>>> 0cd55705017f3957d85537e17e07e3d3a0c9f602
from flask import Blueprint, request, jsonify
from database import db
from models import User

app_routes = Blueprint('app_routes', __name__)

<<<<<<< HEAD
@app_routes.route('/users', methods=['POST'])
=======

@app_routes.route('/test', methods=['POST'])
def test():
    if not request.data:
        return jsonify({"error": "No data received"}), 400

    try:
        data = request.get_json()
        if data is None:
            return jsonify({"error": "Invalid JSON format"}), 400
    except Exception as e:
        return jsonify({"error": f"JSON decoding error: {str(e)}"}), 400

    print("Received data:", data)
    return jsonify({"message": "OK"}), 200

@app_routes.route('/add_user', methods=['POST'])
>>>>>>> 0cd55705017f3957d85537e17e07e3d3a0c9f602
def add_user():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    name = data.get('name')

    if not name:
<<<<<<< HEAD
        return jsonify({'error': 'Name are required.'}), 400
=======
        return jsonify({'error': 'Name and email are required.'}), 400
>>>>>>> 0cd55705017f3957d85537e17e07e3d3a0c9f602
    
    try:
        new_user = User(name=name)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User added successfully', 'id': new_user.id}), 201
    except Exception as e:
        db.session.rollback()
<<<<<<< HEAD
        return jsonify({'message': 'User not added successfully', 'id': new_user.id}), 201
=======
        return jsonify({'message': 'User added successfully', 'id': new_user.id}), 201
>>>>>>> 0cd55705017f3957d85537e17e07e3d3a0c9f602

@app_routes.route('/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        users_list = [{'id': u.id, 'name': u.name} for u in users]
        return jsonify(users_list)
    except Exception as e:
        error_str = str(e)
<<<<<<< HEAD
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
=======
        print(f'Unicodedecodeerror: {error_str}')
    
        pos = e.start
        problematic_str = str(users).encode('utf-8', errors='replace').decode('utf-8')
        print(f'Полный текст: {problematic_str}')
        print(f'Проблемный символ: {problematic_str[pos-5:pos+5]}')

        return jsonify({"error": "Unicode decoding error", "details": error_str}), 500
>>>>>>> 0cd55705017f3957d85537e17e07e3d3a0c9f602
