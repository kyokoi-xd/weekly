from flask import Flask
<<<<<<< HEAD
=======
from flask_migrate import Migrate
>>>>>>> 0cd55705017f3957d85537e17e07e3d3a0c9f602
from config import Config
from database import db
from models import User
from routes import app_routes


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
<<<<<<< HEAD
=======
migrate = Migrate(app, db)
>>>>>>> 0cd55705017f3957d85537e17e07e3d3a0c9f602

app.register_blueprint(app_routes)

@app.route('/')
def index():
    return "<p>Hello, World!<p>"

if __name__ =='__main__':
    app.run(debug=True)