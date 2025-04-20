# seed_movies.py

import os
from models.managers import SQLAlchemyDataManager
from models.handlers import JsonFileHandlerModel
from config import config

def safe_join_list(value):
    return ", ".join(value) if isinstance(value, list) else value or ""

def seed_movies_json_to_db():
    """Seed the database with movies from JSON file."""
    # Ensure the data directory exists
    data_dir = os.path.join(os.getcwd(), config.DATA_DIRECTORY)
    os.makedirs(data_dir, exist_ok=True)
    
    manager = SQLAlchemyDataManager()        
    file_path = os.path.join(data_dir, config.DATA_FILE)
    file_handler = JsonFileHandlerModel(file_path)
    movie_data = file_handler.read_data()

    for imdb_id, movie in movie_data.items():
        try:
            if str(movie.get("rating")).lower() == "n/a":
                movie["rating"] = 0.0

            # Skip if movie already exists
            if manager.movie_exists(imdb_id):
                print(f"⚠️ Skipped (already exists): {movie.get('title')}")
                continue

            movie_record = {
                "imdb_id": imdb_id,
                "title": movie.get("title", "Unknown"),
                "rating": float(movie.get("rating", 0)),
                "year": int(movie.get("year", 0)),
                "poster": movie.get("poster", ""),
                "country": safe_join_list(movie.get("country")),
                "director": movie.get("director", "Unknown"),
                "actors": safe_join_list(movie.get("actors")),
                "writer": safe_join_list(movie.get("writer")),
                "genre": safe_join_list(movie.get("genre")),
                "plot": movie.get("plot", ""),
                "language": movie.get("language", ""),
                "awards": safe_join_list(movie.get("awards")),
                "notes": movie.get("notes", "")
            }

            manager.add_movie(**movie_record)
            print(f"✅ Inserted: {movie['title']}")

        except Exception as e:
            print(f"❌ Failed to insert {movie.get('title')} - {e}")

