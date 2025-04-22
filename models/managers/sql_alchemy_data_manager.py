"""SQLAlchemy implementation of the DataManagerInterface for movie management."""
from sqlalchemy import func
from singletons import DbInstance
from models.db_models import Users, Movies
from models.utils.data_utils import DataUtils
from constants import ConstantStrings as Cs, DataConstants as Dc
from .data_manager_interface import DataManagerInterface


class SQLAlchemyDataManager(DataManagerInterface):
    """Handles ORM-based logic for DB storage."""

    def __init__(self):
        self.db = DbInstance.get_db()

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
        # Transform movie dictionary into a list for template
        movies_list = []
        for movie_id, movie_data in data.items():
            movies_list.append({
                Dc.id(): movie_id,
                Dc.title(): movie_data.get(Dc.title(), Cs.NOT_AVAILABLE),
                Dc.rating(): movie_data.get(Dc.rating(), Cs.NOT_AVAILABLE),
                Dc.year(): movie_data.get(Dc.year(), Cs.NOT_AVAILABLE),
                Dc.poster(): movie_data.get(Dc.poster(), ''),
                Dc.country(): movie_data.get(Dc.country(), Cs.NOT_AVAILABLE),
                Dc.director(): movie_data.get(Dc.director(), Cs.NOT_AVAILABLE),
                Dc.actors(): movie_data.get(Dc.actors(), Cs.NOT_AVAILABLE),
                Dc.genre(): movie_data.get(Dc.genre(), Cs.NOT_AVAILABLE),
                Dc.plot(): movie_data.get(Dc.plot(), Cs.NOT_AVAILABLE)
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

    def get_user_by_id(self, user_id):
        """Get a user by their ID."""
        return Users.query.get(user_id)

    def add_user(self, name):
        """Add a new user to the database.
        
        Sample user_data:
        {            
            "name": "John Doe",
        }
        """
        # check if user already exists
        user = Users.query.filter(func.lower(Users.name) == name.lower()).first()
        if user:
            return False  # user already exists

        # add user to database
        user = Users(name=name)
        self.db.session.add(user)
        self.db.session.commit()
        return True  # user added successfully

    def add_movie_to_user(self, user_id, movie_id, movie_data):
        """Add a movie to a user's favorites."""
        user = Users.query.get(user_id)
        movie = Movies.query.filter_by(imdb_id=movie_id).first()

        # if the movie is not in the database, add it
        if not movie:
            movie_data_formatted = self.get_movie_object_from_json(movie_id, movie_data)
            movie_data_formatted.pop(Dc.id(), None)
            movie = Movies(**movie_data_formatted)
            self.db.session.add(movie)
            self.db.session.commit()

        if user and movie:
            # check if movie is already in user's favorites
            if movie in user.movies:
                return False  # movie already in user's favorites
            user.movies.append(movie)
            self.db.session.commit()
            return True  # movie added to user's favorites

        return False  # user or movie isn't found

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
        movie_data = self.get_movie_object_from_json(id_column_val, kwargs)
        movie = Movies(**movie_data)
        self.db.session.add(movie)
        self.db.session.commit()
        return data

    # endregion

    # region UPDATE
    def update_movie(self, data, unique_key, **kwargs):
        """Update an existing movie in both the data dictionary and database."""
        for key, value in kwargs.items():
            data[unique_key][key] = value

        movie = Movies.query.filter_by(imdb_id=unique_key).first()
        if not movie:
            return None
        for key, value in kwargs.items():
            if key == Dc.title():
                continue
            if hasattr(movie, key):
                setattr(movie, key, value)
        self.db.session.commit()
        return data

    def update_movie_bck(self, data, unique_key, **kwargs):
        """Update an existing movie in both the data dictionary and database."""
        item = {**kwargs}
        item_key = DataUtils.data_key_by_kv(data, unique_key, item[unique_key])
        for key, value in kwargs.items():
            data[item_key][key] = value

        movie = Movies.query.filter(func.lower(Movies.title) == kwargs.get("title").lower()).first()
        if not movie:
            return None
        for key, value in kwargs.items():
            if key == Dc.title():
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

    def remove_movie_from_user(self, user_id, movie_id):
        """Remove a movie from a user's favorites."""
        user = Users.query.get(user_id)
        movie = Movies.query.filter_by(imdb_id=movie_id).first()
        # remove the movie from the movie table
        if movie:
            self.db.session.delete(movie)
            self.db.session.commit()
        # remove the movie from the user's favorites
        if user:
            user.movies.remove(movie)
            self.db.session.commit()

    # endregion

    # region PRIVATE METHODS
    def __get_movies_as_json(self):
        """Convert all movies from the database to JSON format similar to data.json."""
        movies = Movies.query.all()
        result = {}

        for movie in movies:
            actors = [actor.strip()
                      for actor in movie.actors.split(',')] if movie.actors else []
            writers = [writer.strip()
                       for writer in movie.writer.split(',')] if movie.writer else []
            genres = [genre.strip()
                      for genre in movie.genre.split(',')] if movie.genre else []
            countries = [country.strip()
                         for country in movie.country.split(',')] if movie.country else []
            awards = [award.strip()
                      for award in movie.awards.split(',')] if movie.awards else []

            result[movie.imdb_id] = {
                Dc.title(): movie.title.strip() if movie.title else "",
                Dc.rating(): movie.rating,
                Dc.year(): movie.year,
                Dc.director(): movie.director.strip() if movie.director else "",
                Dc.actors(): actors,
                Dc.writer(): writers,
                Dc.genre(): genres,
                Dc.plot(): movie.plot.strip() if movie.plot else "",
                Dc.language(): movie.language.strip() if movie.language else "",
                Dc.awards(): awards,
                Dc.poster(): movie.poster.strip() if movie.poster else "",
                Dc.country(): countries
            }

            if movie.notes:
                result[movie.imdb_id][Dc.notes()] = movie.notes.strip()

        return result

    def __save_json_to_db(self, json_data):
        """Save JSON data back to the database as Movie objects."""
        updated_movies = []

        for imdb_id, movie_data in json_data.items():
            movie_data = self.get_movie_object_from_json(imdb_id, movie_data)

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

    def get_movie_object_from_json(self, imdb_id, movie_data):
        """Convert JSON data to a Movie object with proper formatting."""
        movie_data[Dc.actors()] = ','.join(
            [actor.strip() for actor in movie_data.get(Dc.actors(), [])])
        movie_data[Dc.writer()] = ','.join(
            [writer.strip() for writer in movie_data.get(Dc.writer(), [])])
        movie_data[Dc.genre()] = ','.join(
            [genre.strip() for genre in movie_data.get(Dc.genre(), [])])
        movie_data[Dc.country()] = ','.join(
            [country.strip() for country in movie_data.get(Dc.country(), [])])
        movie_data[Dc.awards()] = ','.join(
            [award.strip() for award in movie_data.get(Dc.awards(), [])])

        for key in [Dc.title(), Dc.director(), Dc.plot(),
                    Dc.language(), Dc.poster(), Dc.notes()]:
            if key in movie_data and isinstance(movie_data[key], str):
                movie_data[key] = movie_data[key].strip()

        # if the rating is "N/A" in the movie_data, set it to 0
        try:
            movie_data[Dc.rating()] = float(movie_data[Dc.rating()])
        except ValueError:
            movie_data[Dc.rating()] = 0

        movie_data[Dc.imdb_id()] = imdb_id.strip() if isinstance(imdb_id, str) else imdb_id
        return movie_data

    # endregion
