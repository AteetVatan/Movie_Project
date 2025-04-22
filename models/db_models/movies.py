"""Database model for managing movie data and relationships with users."""
from singletons import DbInstance

DB = DbInstance.get_db()


class Movies(DB.Model):
    """Represents a movie in the system with its associated users."""
    __tablename__ = 'movies'

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)  # internal DB ID
    imdb_id = DB.Column(DB.String(20), unique=True, nullable=False, index=True)  # imdb source ID
    title = DB.Column(DB.String(200), nullable=False)
    director = DB.Column(DB.String(200), nullable=False)
    year = DB.Column(DB.Integer, nullable=False)
    rating = DB.Column(DB.Float, nullable=False)
    poster = DB.Column(DB.String(500), nullable=True)
    country = DB.Column(DB.String(200), nullable=True)
    actors = DB.Column(DB.Text, nullable=True)  # stored as comma-separated string
    writer = DB.Column(DB.Text, nullable=True)  # stored as comma-separated string
    genre = DB.Column(DB.Text, nullable=True)  # stored as comma-separated string
    plot = DB.Column(DB.Text, nullable=True)
    language = DB.Column(DB.String(100), nullable=True)
    awards = DB.Column(DB.Text, nullable=True)
    notes = DB.Column(DB.Text, nullable=True)

    def __repr__(self):
        return f"<Movie {self.name} ({self.year})>"
