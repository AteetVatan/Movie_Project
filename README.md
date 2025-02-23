# Movie Management System

## Overview
This project is a **Movie Management System** that allows users to **manage and interact with a collection of movies**. It provides a **user-friendly menu-driven interface** for performing operations such as viewing, adding, editing, or deleting movies.

## Features
- Read movie data from storage
- Display an interactive user menu
- Perform CRUD (Create, Read, Update, Delete) operations on movies
- Validates user input for accurate operations

## Project Structure
```
Movie_Project/
│-- movies.py  # Main script
│-- base/
│   ├── movies_controller.py  # Handles movie operations
│-- data/
│   ├── data_handler.py  # Reads and writes movie data
│-- helpers/
│   ├── main_print.py  # Handles user interface printing
│-- .venv/  # Virtual environment (optional)
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

## Contributing
Feel free to submit **pull requests** or open **issues** for improvements.

## License
This project is open-source under the **MIT License**.

---
🚀 Happy Coding!

