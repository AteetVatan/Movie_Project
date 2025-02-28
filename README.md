# Data Maintenance System

## Overview
This project is based on **CRUD with MVC pattern**.
It allows users to **manage and interact with a collection of data**. 
It provides a **user-friendly menu-driven interface** 
for performing operations such as viewing, adding, editing, or deleting data.
The architecture is designed using a modular approach with separate controllers, enumerations, helpers, and models.

## Features
- Read movie data from storage
- Display an interactive user menu
- Perform CRUD (Create, Read, Update, Delete) operations on movies
- Validates user input for accurate operations

## Project Structure
```
Movie_Project/
│── controllers/
│   │── base_controller.py
│   │── menu_controller.py
│   │── movies_controller.py
│   └── managers/
│       │── menu_manager.py
│── enumerations/
│   │── app_types.py
│── helpers/
│   │── base_print_input_helper.py
│   │── data_helpers.py
│── models/
│   │── base_model.py
│   │── file_handler_model.py
│   │── menu_operation_output_model.py
│   │── movie_model.py
│   └── managers/
│       │── data_manager.py
│── views/
│   │── movie_view.py
│── validation/
│   │── movie_validation_manager.py
│── data/
│   │── movie.json
│   │── movie_backup.json
│── constants/
│   │── constant_strings.py
│   │── json_constants.py
│── movies.py
│── requirements.txt
│── .gitignore
│── README.md
```

## Installation
### 1. Clone the Repository
```sh
git clone <repo-url>
cd Movie_Project
```
### 2. Set Up Virtual Environment (Optional but Recommended)
```sh
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate  # Windows
```
### 3. Install Dependencies (If requirements.txt exists)
```sh
pip install -r requirements.txt
```

## Usage
To start the program, run:
```sh
python movies.py
```
Follow the on-screen menu to interact with the movie collection.

## Future Improvements
* Implement a database for persistent movie storage.
* Add exception handling and logging for better error tracking. 
* Extend support for additional app types (e.g., TV Shows, Documentaries).

## Contributing
Feel free to submit **pull requests** or open **issues** for improvements.

## License
This project is open-source under the **MIT License**.

---
🚀 Happy Coding!

