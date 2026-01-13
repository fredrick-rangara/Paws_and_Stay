from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from models import db  # Importing the db from your models.py

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_DATA'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize plugins
db.init_app(app)
migrate = Migrate(app, db)
CORS(app)

@app.route('/')
def index():
    return {"message": "Paws & Stay API is running!"}

@app.route('/stay_sessions', methods=['POST'])
def create_stay_session():
    data = request.get_json()

    

if __name__ == '__main__':
    app.run(port=5555, debug=True)