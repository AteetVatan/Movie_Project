"""Database model for managing user data and relationships with movies."""
from singletons import get_db
from .user_movies import UserMovies
db = get_db()

class Users(db.Model):
    """Represents a user in the system with their associated movies."""
    __tablename__= 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)

    # Many-to-many relationship with movies
    movies = db.relationship(
        'Movies',
        secondary='user_movies',  # Use table name instead of model class
        backref='users',
        lazy='dynamic'
    )

    def __repr__(self):
        return f"<User {self.name}>"