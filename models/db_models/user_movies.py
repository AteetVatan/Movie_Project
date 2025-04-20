"""Database model for managing user-movie relationships."""
from singletons import get_db
db = get_db()

class UserMovies(db.Model):
    """Represents a relationship between a user and a movie."""
    __tablename__ = 'user_movies'
    # They will make a composite key
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), primary_key=True)

    def __repr__(self):
        return f"<UserMovie {self.user_id} {self.movie_id}>"
