"""SQLAlchemy implementation of the DataManagerInterface for movie management."""
from models.db_models import Users , Movies , UserMovies
from singletons import get_db
from .data_manager_interface import DataManagerInterface
from constants.data_constants import DataConstants
from models.utils.data_utils import DataUtils
from sqlalchemy import func
from constants import ConstantStrings as Cs
from constants.data_constants import DataConstants as Dc

class SQLAlchemyDataManager(DataManagerInterface):
    """Handles ORM-based logic for DB storage."""
    def __init__(self):
        self.db = get_db()

    # region READ
    def read_data(self):
        """Read all movies from the database and convert to JSON format."""
        try:
            data = self.__get_movies_as_json()
            return data
        except Exception as e:
            print(f"Error reading data: {e}")
            return []
        
        
    def get_all_movies(self, data):
        """Get all movies from the database."""
         # Transform movies dictionary into a list for template
        movies_list = []
        for movie_id, movie_data in data.items():
            movies_list.append({
                'id': movie_id,
                'title': movie_data.get(Dc.title(), Cs.NOT_AVAILABLE),
                'rating': movie_data.get(Dc.rating(), Cs.NOT_AVAILABLE),
                'year': movie_data.get(Dc.year(), Cs.NOT_AVAILABLE),
                'poster': movie_data.get(Dc.poster(), ''),
                'country': movie_data.get(Dc.country(), Cs.NOT_AVAILABLE),
                'director': movie_data.get(Dc.director(), Cs.NOT_AVAILABLE),
                'actors': movie_data.get(Dc.actors(), Cs.NOT_AVAILABLE),
                'genre': movie_data.get(Dc.genre(), Cs.NOT_AVAILABLE),
                'plot': movie_data.get(Dc.plot(), Cs.NOT_AVAILABLE)
            })
        return movies_list
        
   

    def get_all_users(self):
        """Get all users from the database."""
        return Users.query.all()

    def get_user_movies(self, user_id):
        """Get all movies associated with a specific user."""
        user = Users.query.get(user_id)
        if user:
            return user.movies.all()
        return []
    
    def add_user(self, user_data):
        """Add a new user to the database.
        
        Sample user_data:
        {            
            "name": "John Doe",
        }
        """
        #check if user already exists   
        user = Users.query.filter(func.lower(Users.name) == user_data["name"].lower()).first()
        if user:
            return False #user already exists        
        
        #add user to database
        user = Users(**user_data)
        self.db.session.add(user)
        self.db.session.commit()
        return user #user added successfully
    
    
    
    

    def movie_exists(self, imdb_id):
        """Check if a movie exists in the database by IMDB ID."""
        return Movies.query.filter_by(imdb_id=imdb_id).first() is not None
    # endregion

    # region CREATE
    def add_movie(self, data, id_column, **kwargs):
        """Add a new movie to both the data dictionary and database."""
        if id_column and id_column in kwargs:
            id_column_val = kwargs.get(id_column)
            del kwargs[id_column]
        else:
            id_column_val = str(len(data) + 1)

        data[id_column_val] = kwargs
        movie_data = self.__get_movie_object_from_json(id_column_val, kwargs)
        movie = Movies(**movie_data)
        self.db.session.add(movie)
        self.db.session.commit()
        return data
    # endregion

    # region UPDATE
    def update_movie(self, data, unique_key, **kwargs):
        """Update an existing movie in both the data dictionary and database."""
        item = {**kwargs}
        item_key = DataUtils.data_key_by_kv(data, unique_key, item[unique_key])
        for key, value in kwargs.items():
            data[item_key][key] = value        
    
        movie = Movies.query.filter(func.lower(Movies.title) == kwargs.get("title").lower()).first()       
        if not movie:
            return None
        for key, value in kwargs.items():
            if key == DataConstants.title():
                continue
            if hasattr(movie, key):
                setattr(movie, key, value)
        self.db.session.commit()
        return data

    def write_data(self, **kwargs):
        """Write movie data to the database."""
        try:
            self.__save_json_to_db(kwargs)
        except Exception as e:
            print(f"Error saving data: {e}")
            return []
    # endregion

    # region DELETE
    def delete_movie(self, data, key, value):
        """Delete a movie from both the data dictionary and database."""
        item_key = DataUtils.data_key_by_kv(data, key, value)
        del data[item_key]       
        
        movie = Movies.query.filter(func.lower(Movies.title) == value.lower()).first()
        if movie:
            self.db.session.delete(movie)
            self.db.session.commit()
        return data
    # endregion

    # region PRIVATE METHODS
    def __get_movies_as_json(self):
        """Convert all movies from the database to JSON format similar to data.json."""
        movies = Movies.query.all()
        result = {}
        
        for movie in movies:
            actors = [actor.strip() for actor in movie.actors.split(',')] if movie.actors else []
            writers = [writer.strip() for writer in movie.writer.split(',')] if movie.writer else []
            genres = [genre.strip() for genre in movie.genre.split(',')] if movie.genre else []
            countries = [country.strip() for country in movie.country.split(',')] if movie.country else []
            awards = [award.strip() for award in movie.awards.split(',')] if movie.awards else []
            
            result[movie.imdb_id] = {
                DataConstants.title(): movie.title.strip() if movie.title else "",
                DataConstants.rating(): movie.rating,
                DataConstants.year(): movie.year,
                DataConstants.director(): movie.director.strip() if movie.director else "",
                DataConstants.actors(): actors,
                DataConstants.writer(): writers,
                DataConstants.genre(): genres,
                DataConstants.plot(): movie.plot.strip() if movie.plot else "",
                DataConstants.language(): movie.language.strip() if movie.language else "",
                DataConstants.awards(): awards,
                DataConstants.poster(): movie.poster.strip() if movie.poster else "",
                DataConstants.country(): countries
            }
            
            if movie.notes:
                result[movie.imdb_id][DataConstants.notes()] = movie.notes.strip()
                
        return result

    def __save_json_to_db(self, json_data):
        """Save JSON data back to the database as Movie objects."""
        updated_movies = []
        
        for imdb_id, movie_data in json_data.items():            
            movie_data = self.__get_movie_object_from_json(imdb_id, movie_data)           
            
            existing_movie = Movies.query.filter_by(imdb_id=imdb_id).first()
            
            if existing_movie:
                for key, value in movie_data.items():
                    if hasattr(existing_movie, key):
                        setattr(existing_movie, key, value)
                updated_movies.append(existing_movie)
            else:
                new_movie = Movies(**movie_data)
                self.db.session.add(new_movie)
                updated_movies.append(new_movie)
        
        try:
            self.db.session.commit()
            return updated_movies
        except Exception as e:
            self.db.session.rollback()
            raise Exception(f"Error saving movies to database: {str(e)}")
    
    def __get_movie_object_from_json(self, imdb_id, movie_data):
        """Convert JSON data to a Movie object with proper formatting."""
        movie_data[DataConstants.actors()] = ','.join([actor.strip() for actor in movie_data.get(DataConstants.actors(), [])])
        movie_data[DataConstants.writer()] = ','.join([writer.strip() for writer in movie_data.get(DataConstants.writer(), [])])
        movie_data[DataConstants.genre()] = ','.join([genre.strip() for genre in movie_data.get(DataConstants.genre(), [])])
        movie_data[DataConstants.country()] = ','.join([country.strip() for country in movie_data.get(DataConstants.country(), [])])
        movie_data[DataConstants.awards()] = ','.join([award.strip() for award in movie_data.get(DataConstants.awards(), [])])
        
        for key in [DataConstants.title(), DataConstants.director(), DataConstants.plot(), 
                    DataConstants.language(), DataConstants.poster(), DataConstants.notes()]:
            if key in movie_data and isinstance(movie_data[key], str):
                movie_data[key] = movie_data[key].strip()
        
        movie_data['imdb_id'] = imdb_id.strip() if isinstance(imdb_id, str) else imdb_id
        return movie_data
    # endregion
