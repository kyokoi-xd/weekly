from flask import Flask
from flask_migrate import Migrate
from config import Config
from database import db
from models import User
from routes import app_routes


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(app_routes)

@app.route('/')
def index():
    return "<p>Hello, World!<p>"

if __name__ =='__main__':
    app.run(debug=True)