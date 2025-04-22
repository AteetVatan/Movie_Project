"""Database model for managing user-movie relationships."""
from singletons import DbInstance

DB = DbInstance.get_db()


class UserMovies(DB.Model):
    """Represents a relationship between a user and a movie."""
    __tablename__ = 'user_movies'
    # They will make a composite key
    user_id = DB.Column(DB.Integer, DB.ForeignKey('users.id'), primary_key=True)
    movie_id = DB.Column(DB.Integer, DB.ForeignKey('movies.id'), primary_key=True)

    def __repr__(self):
        return f"<UserMovie {self.user_id} {self.movie_id}>"
