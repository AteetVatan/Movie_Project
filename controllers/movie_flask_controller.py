"""Controller for managing movie-related operations and user interactions."""
import json
from flask import Flask, render_template, request, redirect, url_for, jsonify
from models import MovieFlaskModel
from constants import DataConstants as Dc


class MovieFlaskController:
    """Controller for managing movie-related operations and user interactions."""

    def __init__(self, app: Flask):
        """Initialize the controller with Flask app instance and register routes."""
        self.app = app
        self.movie_model = MovieFlaskModel()
        self.register_routes()
        self.register_error_handlers()

    def register_routes(self):
        """Register all route handlers for the movie application."""

        # region READ Operations
        @self.app.route("/")
        def home():
            """Display the home page with all available movies."""
            try:
                movies = self.movie_model.get_all_movies()
                return self.movie_model.view.render_home_page(
                    title="🎥 Welcome to Rotten Potato",
                    movies=movies,
                    search_placeholder="Search for the User Movies."
                )
            except Exception as e:
                raise e

        @self.app.route("/search", methods=['POST'])
        def search():
            """Search for movies based on user-provided search text."""
            try:
                search_text = request.form.get('search_text', '')
                movies = self.movie_model.search_data(search_text)
                if MovieFlaskController.is_xhr(request):
                    return jsonify({
                        'movies': movies,
                        'search_text': search_text
                    })
                return self.movie_model.view.render_home_page(
                    title=f"🎥 Search Results for '{search_text}'",
                    movies=movies,
                    search_placeholder="Search for another movie"
                )
            except ValueError as e:
                if MovieFlaskController.is_xhr(request):
                    return jsonify({
                        'error': str(e),
                        'movies': {}
                    }), 400
                raise e
            except Exception as e:
                raise e

        @self.app.route("/users")
        def list_users():
            """Display a list of all registered users in the system."""
            try:
                users = self.movie_model.get_all_users()
                user_data = []

                if not users:
                    if MovieFlaskController.is_xhr(request):
                        return jsonify({
                            'success': True,
                            'users': [],
                            'message': 'No users found'
                        })
                    return render_template('users.html',
                                           users=[],
                                           title="🎬 Movie Users",
                                           message="No users found. Add some users to get started!")

                for user in users:
                    movie_count = len(self.movie_model.get_user_movies(user.id))
                    user_data.append({
                        'id': user.id,
                        'name': user.name,
                        'movie_count': movie_count
                    })

                if MovieFlaskController.is_xhr(request):
                    return jsonify({
                        'success': True,
                        'users': user_data
                    })

                return render_template('users.html',
                                       users=user_data,
                                       title="🎬 Movie Users")
            except Exception as e:
                raise e

        @self.app.route("/users/<int:user_id>")
        def user_movies(user_id):
            """Display all movies associated with a specific user."""
            try:
                user = self.movie_model.get_user_by_id(user_id)
                if not user:
                    raise ValueError("User not found")

                movies = self.movie_model.get_user_movies(user_id)
                movie_data = []
                for movie in movies:
                    movie_data.append({
                        Dc.id(): movie.id,
                        Dc.imdb_id(): movie.imdb_id,
                        Dc.title(): movie.title,
                        Dc.year(): movie.year,
                        Dc.rating(): movie.rating,
                        Dc.director(): movie.director,
                        Dc.actors(): movie.actors,
                        Dc.plot(): movie.plot,
                        Dc.poster(): movie.poster,
                        Dc.genre(): movie.genre,
                        Dc.country(): movie.country,
                        Dc.language(): movie.language,
                        Dc.awards(): movie.awards
                    })

                if MovieFlaskController.is_xhr(request):
                    return jsonify({
                        'success': True,
                        'user': {
                            'id': user.id,
                            'name': user.name
                        },
                        'movies': movie_data
                    })

                return render_template(
                    'user_movies.html',
                    user=user,
                    movies=movie_data,
                    title=f"🎬 {user.name}'s Movies"
                )
            except ValueError as e:
                raise e
            except Exception as e:
                raise e

        @self.app.route("/movie/<movie_id>")
        def get_movie(movie_id):
            """Display detailed information for a specific movie by its ID."""
            try:
                movie = self.movie_model.get_movie_by_id(movie_id)
                if not movie:
                    raise ValueError("Movie not found")

                if MovieFlaskController.is_xhr(request):
                    return jsonify({
                        'success': True,
                        'movie': movie
                    })

                return render_template(
                    'movie_detail.html',
                    movie=movie,
                    title=f"🎬 {movie.get('title', 'Movie Details')}"
                )
            except ValueError as e:
                raise e
            except Exception as e:
                raise e

        # endregion READ Operations

        # region CREATE Operations
        @self.app.route("/add_user", methods=['POST'])
        def add_user():
            """Create a new user in the system."""
            try:
                name = request.form.get('name', '').strip()

                if not name:
                    raise ValueError("Name is required")

                success = self.movie_model.add_user(name)

                if success:
                    if MovieFlaskController.is_xhr(request):
                        return jsonify({
                            'success': True,
                            'message': f'User {name} added successfully'
                        })
                    return redirect(url_for('list_users'))
                raise ValueError("Failed to add user")
            except ValueError as e:
                raise e
            except Exception as e:
                raise e

        @self.app.route("/users/<int:user_id>/add_movie", methods=['GET', 'POST'])
        def add_user_movie(user_id):
            """Add a new movie to a user's favorite list."""
            try:
                user = self.movie_model.get_user_by_id(user_id)
                if not user:
                    raise ValueError("User not found")

                if request.method == 'POST':
                    movie_data = request.form.get('movie_data')
                    if not movie_data:
                        raise ValueError("Movie data is required")

                    try:
                        movie = json.loads(movie_data)
                        success = self.movie_model.add_movie_to_user(user_id, movie)

                        if success:
                            if MovieFlaskController.is_xhr(request):
                                return jsonify({
                                    'success': True,
                                    'message': f'Movie "{movie["title"]}" added successfully',
                                    'movie': movie,
                                    'user_id': user_id
                                })
                            return redirect(url_for('user_movies', user_id=user_id))

                        if MovieFlaskController.is_xhr(request):
                            return jsonify({
                                'success': False,
                                'error': 'Movie already in user\'s favorites'
                            }), 200
                        return render_template('add_user_movie.html',
                                               user=user,
                                               title=f"🎬 Add Movie for {user.name}",
                                               message="Movie already in user's favorites"), 200
                    except ValueError as e:
                        raise e

                return render_template('add_user_movie.html',
                                       user=user,
                                       title=f"🎬 Add Movie for {user.name}")
            except ValueError as e:
                raise e
            except Exception as e:
                raise e

        # endregion CREATE Operations

        # region UPDATE Operations
        @self.app.route("/users/<int:user_id>/update_movie/<string:movie_id>",
                        methods=['GET', 'POST'])
        def update_user_movie(user_id, movie_id):
            """Update the notes for a movie in a user's favorite list."""
            try:
                user = self.movie_model.get_user_by_id(user_id)
                if not user:
                    raise ValueError("User not found")

                movie = self.movie_model.get_movie_by_id(movie_id)
                if not movie:
                    raise ValueError("Movie not found")

                if request.method == 'POST':
                    notes = request.form.get('notes', '').strip()
                    success = self.movie_model.update_data(movie_id, notes=notes)

                    if success:
                        if MovieFlaskController.is_xhr(request):
                            return jsonify({
                                'success': True,
                                'message': f'Notes updated successfully for "{movie["title"]}"',
                                'movie': movie
                            })
                        return redirect(url_for('user_movies', user_id=user_id))

                    raise ValueError("Failed to update movie notes")

                # Format movie data for display
                movie_data = {
                    'id': movie.get(Dc.id()),
                    'imdb_id': movie_id,
                    'title': movie.get(Dc.title()),
                    'year': movie.get(Dc.year()),
                    'rating': movie.get(Dc.rating()),
                    'director': movie.get(Dc.director()),
                    'actors': movie.get(Dc.actors()),
                    'plot': movie.get(Dc.plot()),
                    'poster': movie.get(Dc.poster()),
                    'genre': movie.get(Dc.genre()),
                    'country': movie.get(Dc.country()),
                    'language': movie.get(Dc.language()),
                    'awards': movie.get(Dc.awards()),
                    'notes': movie.get(Dc.notes(), '')
                }

                return render_template('update_movie.html',
                                       user=user,
                                       movie=movie_data,
                                       title=f"🎬 Update Notes for {movie_data['title']}")
            except ValueError as e:
                raise e
            except Exception as e:
                raise e

        # endregion UPDATE Operations

        # region DELETE Operations
        @self.app.route("/users/<int:user_id>/delete_movie/<string:movie_id>")
        def delete_user_movie(user_id, movie_id):
            """Remove a movie from a user's favorites list."""
            try:
                success = self.movie_model.remove_movie_from_user(user_id, movie_id)
                if success:
                    if MovieFlaskController.is_xhr(request):
                        return jsonify({
                            'success': True,
                            'message': 'Movie removed successfully'
                        })
                    return redirect(url_for('user_movies', user_id=user_id))
                raise ValueError("Failed to remove movie")
            except ValueError as e:
                raise e
            except Exception as e:
                raise e

        # endregion DELETE Operations

        # region API Operations
        @self.app.route("/get_imdb_movie", methods=['POST'])
        def get_imdb_movie():
            """Fetch movie details from the IMDB API based on title."""
            try:
                title = request.form.get('title', '').strip()
                if not title:
                    raise ValueError("Title is required")
                response = self.movie_model.get_imdb_data(title=title)
                return response
            except ValueError as e:
                raise e
            except Exception as e:
                raise e

        @self.app.route("/sort")
        def sort():
            """Sort and display movies based on specified criteria and order."""
            try:
                sort_by = request.args.get('sort', 'title')
                order = request.args.get('order', 'asc')

                movies = self.movie_model.sort_data(sort_by, order == 'desc')
                if MovieFlaskController.is_xhr(request):
                    return jsonify({
                        'success': True,
                        'movies': movies
                    })
                return self.movie_model.view.render_home_page(
                    title=f"🎥 Movies sorted by {sort_by}",
                    movies=movies,
                    search_placeholder="Search for a movie"
                )
            except Exception as e:
                raise e
        # endregion API Operations

    def register_error_handlers(self):
        """Register error handlers for the application."""

        @self.app.errorhandler(400)
        def bad_request(e):
            """Error handler for bad requests."""
            if MovieFlaskController.is_xhr(request):
                return jsonify({
                    'success': False,
                    'error': 'Bad Request',
                    'message': str(e)
                }), 400
            return render_template('error.html',
                                   message="Bad Request",
                                   title="400 - Bad Request"), 400

        @self.app.errorhandler(404)
        def page_not_found(e):
            """Error handler for page not found."""
            if MovieFlaskController.is_xhr(request):
                return jsonify({
                    'success': False,
                    'error': 'Not Found',
                    'message': str(e)
                }), 404
            return render_template('error.html',
                                   message="Page not found",
                                   title="404 - Not Found"), 404

        @self.app.errorhandler(500)
        def internal_server_error(e):
            """Error handler for internal server error."""
            if MovieFlaskController.is_xhr(request):
                return jsonify({
                    'success': False,
                    'error': 'Internal Server Error',
                    'message': str(e)
                }), 500
            return render_template('error.html',
                                   message="An internal server error occurred",
                                   title="500 - Internal Server Error"), 500

    @staticmethod
    def is_xhr(req) -> bool:
        return req.headers.get('X-Requested-With') == 'XMLHttpRequest'
