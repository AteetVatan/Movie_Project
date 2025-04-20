import os
from flask import Flask
from models.db_models import db
from scripts.seed_movies import seed_movies_json_to_db

# Setup Flask app
app = Flask(__name__)
db_path = os.path.join(os.getcwd(), "data", "movie_project.db")
os.makedirs(os.path.dirname(db_path), exist_ok=True)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

def init_db():
    db.init_app(app)
    with app.app_context():
        db.create_all()
        print("Database tables created successfully")
        seed_movies_json_to_db(db)

if __name__ == "__main__":
    init_db()
