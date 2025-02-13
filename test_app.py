import unittest
from jsonschema import validate
from app import app, db
from models import User

USERS_SCHEMA = {"type": "object",
                "properties": {
                    "id" : {"type": "number"},
                    "name" : {"type": "string"},
                    },
                'required': ['id', 'name']
                }

class APITest(unittest.TestCase):
    def setUp(self):
        self.app_context = app.app_context()
        self.app_context.push()
        self.client = app.test_client()
        self.client.testing = True
        db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.rollback()
        db.session.query(User).delete()
        db.session.commit()
        db.drop_all()
        self.app_context.pop()

    def test_get_users(self):
        user = User(id=1, name='Mary')
        db.session.add(user)
        db.session.commit()

        excepted_data = {'id': 1, 'name': 'Mary'}
        respone = self.client.get('/users')
        response_data = respone.get_json()

        self.assertEqual(200, respone.status_code)
        self.assertEqual(excepted_data, response_data[0])

        for user in response_data:
            validate(instance=user, schema=USERS_SCHEMA)

    def test_add_user(self):
        payload = {'id': 1, 'name': 'Mary'}
        response = self.client.post('/users', json=payload)

        self.assertEqual(201, response.status_code)
        self.assertIn('id', payload)
        self.assertIn('name', payload)

    def test_getUserById(self):
        user = User(id=1, name='Mary')
        db.session.add(user)
        db.session.commit()

        response = self.client.get(f'/users/{user.id}')
        response_data = response.get_json()

        self.assertEqual(200, response.status_code)

        validate(instance=response_data, schema=USERS_SCHEMA)

    def test_updateUserById(self):
        user = User(id=1, name='Mary')
        db.session.add(user)
        db.session.commit()

        payload = {'name': 'Test Name'}
        response = self.client.put(f'/users/{user.id}', json=payload)
        updated_user = db.session.get(User, user.id)


        self.assertEqual(200, response.status_code)

        self.assertEqual(updated_user.name, payload["name"])

    def test_deleteUserById(self):
        user = User(id=1, name='Mary')
        db.session.add(user)
        db.session.commit()

        response = self.client.delete(f'/users/{user.id}')

        self.assertEqual(201, response.status_code)

if __name__ == '__main__':
    unittest.main()