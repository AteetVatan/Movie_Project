"""Database model for managing user data and relationships with movies."""
from singletons import DbInstance

DB = DbInstance.get_db()


class Users(DB.Model):
    """Represents a user in the system with their associated movies."""
    __tablename__ = 'users'
    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    name = DB.Column(DB.String(100), nullable=False)

    # Many-to-many relationship with movies
    movies = DB.relationship(
        'Movies',
        secondary='user_movies',  # Use table name instead of model class
        backref='users',
        lazy='dynamic'
    )

    def __repr__(self):
        return f"<User {self.name}>"
