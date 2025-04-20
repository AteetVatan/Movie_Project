from flask import Flask, render_template, request, redirect, url_for, jsonify
from controllers.base_controller import BaseController
from models import MovieFlaskModel

class MovieFlaskController():    
    def __init__(self, app: Flask): 
        self.app = app        
        self.movie_model = MovieFlaskModel()
        self.register_routes()
        
    def register_routes(self):
        @self.app.route("/")
        def home():
            """Showcase Mode (For a Portfolio/Viewer App)
                / → Home Page Contents
                📢 Title: "🎥 Welcome to MovieWeb!"
                🔍 Search bar: "Search for a movie"
                🏆 Show all movies
                🎯 Navigation: Links to  /users
                on home page we can  view all the movies in the Data base
                and there are navigation link to go to the user"""
            return self.movie_model.home()

        @self.app.route("/search", methods=['POST'])
        def search():
            """Search for movies based on user input."""
            search_text = request.form.get('search_text', '')
            try:
                # Call the model's search_data method
                movies = self.movie_model.search_data(search_text)
                
                # Check if the request is AJAX
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return jsonify({
                        'movies': movies,
                        'search_text': search_text
                    })
                
                # Regular form submission
                return self.movie_model.view.render_home_page(
                    title=f"🎥 Search Results for '{search_text}'",
                    movies=movies,
                    search_placeholder="Search for another movie"
                )
            except ValueError as e:
                # Handle search errors
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return jsonify({
                        'error': str(e),
                        'movies': {}
                    })
                
                return self.movie_model.view.render_home_page(
                    title="🎥 Search Error",
                    movies={},
                    search_placeholder=str(e)
                )

        @self.app.route("/users")
        def list_users():
            """Display list of all users."""
            users = self.movie_model.get_all_users()
            return render_template('users.html', users=users)

        @self.app.route("/users/<int:user_id>")
        def user_movies(user_id):
            """Display movies for a specific user."""
            user = self.movie_model.get_user_by_id(user_id)
            if not user:
                return "User not found", 404
            movies = self.movie_model.get_user_movies(user_id)
            return render_template('user_movies.html', user=user, movies=movies)

        @self.app.route("/add_user", methods=['GET', 'POST'])
        def add_user():
            """Add a new user."""
            if request.method == 'POST':
                name = request.form.get('name')
                if name:
                    success = self.movie_model.add_user(name)
                    if success:
                        return redirect(url_for('list_users'))
            return render_template('add_user.html')

        @self.app.route("/users/<int:user_id>/add_movie", methods=['GET', 'POST'])
        def add_user_movie(user_id):
            """Add a movie to user's favorites."""
            user = self.movie_model.get_user_by_id(user_id)
            if not user:
                return "User not found", 404
                
            if request.method == 'POST':
                movie_id = request.form.get('movie_id')
                if movie_id:
                    success = self.movie_model.add_movie_to_user(user_id, movie_id)
                return redirect(url_for('user_movies', user_id=user_id))
                
            movies = self.movie_model.get_all_movies()
            return render_template('add_user_movie.html', user=user, movies=movies)

        @self.app.route("/users/<int:user_id>/update_movie/<int:movie_id>", methods=['GET', 'POST'])
        def update_user_movie(user_id, movie_id):
            """Update a movie in user's favorites."""
            user = self.movie_model.get_user_by_id(user_id)
            movie = self.movie_model.get_movie_by_id(movie_id)
            if not user or not movie:
                return "User or movie not found", 404
                
            if request.method == 'POST':
                title = request.form.get('title', movie.title)
                rating = float(request.form.get('rating', movie.rating))
                success = self.movie_model.update_movie(movie_id, title=title, rating=rating)
                if success:
                    return redirect(url_for('user_movies', user_id=user_id))
            return render_template('update_movie.html', user=user, movie=movie)

        @self.app.route("/users/<int:user_id>/delete_movie/<int:movie_id>")
        def delete_user_movie(user_id, movie_id):
            """Remove a movie from user's favorites."""
            success = self.movie_model.remove_movie_from_user(user_id, movie_id)
            if success:
                return redirect(url_for('user_movies', user_id=user_id))
            return "Failed to remove movie", 400

        @self.app.route("/movie/<movie_id>")
        def get_movie(movie_id):
            """Display detailed information for a specific movie.
            
            Args:
                movie_id: The ID of the movie to display
                
            Returns:
                Rendered movie detail template or 404 if movie not found
            """
            try:
                # Get movie data
                movie = self.movie_model.get_movie_by_id(movie_id)
                if not movie:
                    return "Movie not found", 404
                    
                # Check if it's an AJAX request
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return jsonify({
                        'success': True,
                        'movie': movie
                    })
                
                # Regular request - render full page
                return render_template(
                    'movie_detail.html',
                    movie=movie,
                    title=f"🎬 {movie.get('title', 'Movie Details')}"
                )
                
            except Exception as e:
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return jsonify({
                        'success': False,
                        'error': str(e)
                    }), 400
                return f"Error loading movie: {str(e)}", 400

    #   # region CREATE
    # def add_data(self) -> bool:
    #     """Abstract method to add data."""
    #     return False

    # # endregion CREATE

    # # region READ  
    # def list_data(self) -> bool:
    #     """Abstract method to list data."""
    #     return False

   
    # def show_random_item_in_data(self) -> bool:
    #     """Abstract method to show random item in data."""
    #     return False

   
    # def search_data(self) -> bool:
    #     """Abstract method to search data."""
    #     return False

    
    # def sort_data(self, key, reverse=False) -> bool:
    #     """Abstract method to Sort data by given key."""
    #     return False

    
    # def data_stats(self) -> bool:
    #     """Abstract method for data stat."""
    #     return False

    
    # def data_filter(self) -> bool:
    #     """Abstract method for data filter."""
    #     return False

    
    # def generate_website(self) -> bool:
    #     """Abstract method to delete item in data."""
    #     return False

    # # endregion READ

    # # region UPDATE @abstractmethod
    # def update_data(self) -> bool:
    #     """Abstract method to update data."""
    #     return False

   
    # def show_data_histogram(self) -> bool:
    #     """Abstract method to show histogram for data."""
    #     return False

    # # endregion UPDATE

    # # region DELETE
   
    # def delete_data(self) -> bool:
    #     """Abstract method to delete item in data."""
    #     return False

   
    # def save_data(self) -> bool:
    #     """Abstract method to delete item in data."""
    #     return False

    # # endregion DELETE

    # # region EXIT
   
    # def exit(self) -> bool:
    #     """Abstract method to exit the run time environment."""
    #     return False

    # endregion EXIT
