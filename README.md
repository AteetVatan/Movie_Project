# Data Maintenance System

## Overview
This project is based on **CRUD with MVC pattern**.
It allows users to **manage and interact with a collection of data**. 
It provides a **user-friendly menu-driven interface** 
for performing operations such as viewing, adding, editing, or deleting data.
The architecture is designed using a modular approach with separate controllers, enumerations, helpers, and models.

## Features
- CRUD: Create, Read, Update, Delete.
- Project is based on MVC Pattern.
- Analytics: Top-rated data, least-rated data etc.
- Persistent Storage: JSON & CSV files.

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
Create or use existing (default) data.json
```sh
python main.py
```
Create or use existing xyz.json
```sh
python main.py xyz
```
Create or use existing abc.csv
```sh
python main.py abc.csv
```

Follow the on-screen menu to interact with the data collection.

## Project Structure
```
## Project Structure

```bash
Movie_Project/
├── _static/
│   ├── flags/
│   ├── index.html
│   ├── index_template.html
│   └── style.css
├── config/
│   └── config.py
├── constants/
│   ├── constant_strings.py
│   ├── data_constants.py
│   └── omdb_constants.py
├── controllers/
│   ├── base_controller.py
│   ├── menu_controller.py
│   ├── movies_controller.py
│   └── managers/
│       └── menu_manager.py
├── data/
│   ├── data.csv
│   └── data.json
├── enumerations/
│   ├── __init__.py
│   ├── app_types.py
│   ├── file_types.py
│   └── omdb_api_param_types.py
├── env/
│   ├── .env
│   └── load_envoirments.py
├── helpers/
│   ├── api_helper.py
│   ├── base_print_input_helper.py
│   ├── data_helpers.py
│   └── file_helpers.py
├── models/
│   ├── api_request_model.py
│   ├── base_model.py
│   ├── csv_file_handler_model.py
│   ├── file_handler_model.py
│   ├── html_file_handler_model.py
│   ├── json_file_handler_model.py
│   ├── menu_operation_output_model.py
│   ├── movie_model.py
│   ├── managers/
│   │   ├── data_manager.py
│   │   └── file_manager.py
│   └── storage/
│       ├── istorage.py
│       ├── storage_csv.py
│       ├── storage_json.py
│       └── storage_manager.py
├── validation/
│   └── movie_validation_manager.py
├── views/
│   └── movie_view.py
├── .gitignore
├── main.py
├── movie_app.py
├── README.md
└── requirements.txt
```
## Contributing
Feel free to submit **pull requests** or open **issues** for improvements.

## License
This project is open-source under the **MIT License**.

---
🚀 Happy Coding!

