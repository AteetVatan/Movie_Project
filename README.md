# Movie Management System 🎬

## Live Website : https://movie-app-kufy.onrender.com/

## Overview
This project is based on **CRUD with MVC pattern**.
Its is a Flask-based web application for managing and organizing movie collections 
with user-specific favorites, search capabilities, and detailed movie information from IMDB.
The architecture is designed using a modular approach with separate controllers, enumerations, helpers, and models.

## Features

### Movie Management
- Search user movies.
- Add user movie using IMDB API integration.
- View detailed movie information including:
  - Title, Year, Rating
  - Director, Actors, Plot
  - Genre, Country, Language
  - Awards and Poster
- Sort movies by:
  - Rating (High to Low/Low to High)
  - Year (Newest/Oldest)
  - Title (A-Z/Z-A)
- Filter movies by rating and year range
- View movie statistics and rankings
- The Data is persisted in Flask App SQL LITE DataBase

### User Features
- Create and manage user profiles
- Personal movie collections for each user
- Add/Remove movies from favorites
- Add personal notes to movies
- Track movie count per user

### Interface
- Clean, modern UI with Bulma CSS framework
- Responsive design for all devices
- Dynamic search with dropdown suggestions
- Real-time updates using AJAX
- Movie posters with fallback images
- Country flags for movie origins
- Star rating visualization
- Loading indicators for better UX

## Technical Architecture

### MVC Pattern
- **Models**: Handle data operations and business logic
  - `MovieFlaskModel`: Main model for web interface `Used for Flask APP`
  - `MovieCliModel`: Model for CLI operations
  - Data managers for file/DB operations

- **Views**: Handle data presentation
  - `MovieFlaskView`: Web interface views `Used for Flask APP`
  - `MovieCliView`: CLI interface views
  - Template-based rendering

- **Controllers**: Handle request processing
  - `MovieFlaskController`: Main web controller `Used for Flask APP`
  - `MovieCliController`: Main CLI controller
  - `MenuController`: Menu CLI controller
  - Route handlers for all operations
  - Error handling and validation

### Project Structure
```
Movie_Project/
├── config/
│   ├── __init__.py
│   ├── config.py
│   ├── load_enviorments.py
│   └── .env
├── constants/
│   ├── __init__.py
│   ├── constant_strings.py
│   ├── data_constants.py
│   └── odmb_constants.py
├── controllers/
│   ├── movie_flask_controller.py
│   ├── movies_cli_controller.py
│   └── base_controller.py
├── models/
│   ├── movie_flask_model.py
│   ├── movie_cli_model.py
│   ├── api_request_model.py
│   ├── base_model.py
│   ├── csv_file_handler_model.py
│   ├── file_handler_model.py
│   ├── html_file_handler_model.py
│   ├── json_file_handler_model.py
│   ├── menu_operation_output_model.py
│   └── movie_model.py
├── views/
│   ├── movie_flask_view.py
│   └── movie_cli_view.py
├── static/
│   ├── css/
│   │   ├── common.css
│   │   ├── home.css
│   │   └── add_user_movie.css
│   └── js/
│       ├── home.js
│       ├── add_user_movie.js
│       └── update_movie.js
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── users.html
│   ├── user_movies.html
│   ├── add_user_movie.html
│   ├── update_movie.html
│   └── error.html
├── helpers/
│   ├── port_helper.py
│   ├── api_helper.py
│   ├── base_print_input_helper.py
│   ├── data_helpers.py
│   └── file_helpers.py
├── validation/
│   └── movie_validation_manager.py
├── enumerations/
│   ├── __init__.py
│   ├── app_types.py
│   ├── file_types.py
│   └── omdb_api_param_types.py
├── _static/
│   ├── flags/
│   ├── index.html
│   ├── index_template.html
│   └── style.css
├── data/
│   ├── data.json
│   └── data.csv
│   └── movie_project.db               - Flask App SQL LITE DataBase
├── scripts/
│   └── setup.py
├── singletons/
│   └── __init__.py
├── .gitignore
├── main.py                            - Flask App Entry POINT
├── main_cli.py
├── movie_app.py
├── requirements.txt
└── README.md
```

## API Endpoints

### User Operations
- `GET /users` - List all users
- `POST /add_user` - Create new user
- `GET /users/<user_id>` - Get user's movies
- `POST /users/<user_id>/add_movie` - Add movie to favorites
- `POST /users/<user_id>/update_movie/<movie_id>` - Update movie notes
- `GET /users/<user_id>/delete_movie/<movie_id>` - Remove from favorites

### Movie Operations
- `GET /` - Home page with all movies
- `POST /search` - Search movies
- `GET /movie/<movie_id>` - Get movie details
- `POST /get_imdb_movie` - Fetch movie data from IMDB
- `GET /sort` - Sort movies list

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Movie_Project
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure OMDB API:
Create `.env` file in the config directory:
```bash
OMDB_API_KEY_NAME=apikey
OMDB_API_KEY_VALUE=your_api_key_here
```

5. Run the application:
```bash
python main.py
```

## Dependencies
- Flask: Web framework
- Requests: HTTP library for IMDB API
- Bulma: CSS framework
- Font Awesome: Icons
- pycountry: Country data and flags

## Error Handling
- 400 Bad Request - Invalid input data
- 404 Not Found - Resource not found
- 500 Internal Server Error - Server-side issues
- Custom error messages for specific scenarios
- AJAX error handling with user feedback

## Data Storage
- SQLLite DataBase (default)
- JSON file-based storage 
- Optional database storage support
- Data validation and sanitization
- Automatic data persistence

## Browser Support
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Development Features
- CRUD operations for all entities
- Modular code structure
- Type hints and documentation

## Future Improvements
1. User authentication system
2. Database integration
3. Advanced search filters
4. Movie recommendations
5. Social features (sharing, comments)
6. Performance optimizations
7. Additional movie data sources
8. Mobile app version

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- OMDB API for movie data
- Bulma for UI framework
- Flask community
- Font Awesome for icons

---
🚀 Happy Coding!

