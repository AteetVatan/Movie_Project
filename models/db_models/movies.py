"""Database model for managing movie data and relationships with users."""
from singletons import get_db
db = get_db()

class Movies(db.Model):
    """Represents a movie in the system with its associated users."""
    __tablename__ = 'movies'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # internal DB ID
    imdb_id = db.Column(db.String(20), unique=True, nullable=False, index=True)  # imdb source ID
    title = db.Column(db.String(200), nullable=False)
    director = db.Column(db.String(200), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    poster = db.Column(db.String(500), nullable=True)
    country = db.Column(db.String(200), nullable=True)
    actors = db.Column(db.Text, nullable=True)  # stored as comma-separated string
    writer = db.Column(db.Text, nullable=True)  # stored as comma-separated string
    genre = db.Column(db.Text, nullable=True)  # stored as comma-separated string
    plot = db.Column(db.Text, nullable=True)
    language = db.Column(db.String(100), nullable=True)
    awards = db.Column(db.Text, nullable=True)
    notes = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<Movie {self.name} ({self.year})>"
