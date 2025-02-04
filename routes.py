
from flask import Blueprint, request, jsonify
from database import db
from models import User

app_routes = Blueprint('app_routes', __name__)


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
def add_user():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    name = data.get('name')

    if not name:
        return jsonify({'error': 'Name and email are required.'}), 400
    
    try:
        new_user = User(name=name)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User added successfully', 'id': new_user.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'User added successfully', 'id': new_user.id}), 201

@app_routes.route('/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        users_list = [{'id': u.id, 'name': u.name} for u in users]
        return jsonify(users_list)
    except Exception as e:
        error_str = str(e)
        print(f'Unicodedecodeerror: {error_str}')
    
        pos = e.start
        problematic_str = str(users).encode('utf-8', errors='replace').decode('utf-8')
        print(f'Полный текст: {problematic_str}')
        print(f'Проблемный символ: {problematic_str[pos-5:pos+5]}')

        return jsonify({"error": "Unicode decoding error", "details": error_str}), 500