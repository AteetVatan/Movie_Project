"""All Common Configurations"""

AllOW_USER_INPUT = True
LOAD_DATA_FROM_API = True

ANIMALS_JSON_DATA_FILE = "animals_data.json"
ANIMALS_JSON_DATA_FILE_DIR = "data"
ANIMALS_HTML_TEMPLATE = "animals_template.html"
ANIMALS_HTML_TEMPLATE_DIR = "data"
ANIMALS_HTML_FILE = "animals.html"
ANIMAL_HTML_PLACEHOLDER = "__REPLACE_ANIMALS_INFO__"
ANIMAL_DEFAULT_SEARCH = "cat"
# json_data search keys
JSON_DATA_SEARCH_KEYS = ("name", "diet", "locations", "type", "kingdom", "slogan", "diet",
                         "average_litter_size")

# API configs
ANIMAL_API_BASE_URL = "https://api.api-ninjas.com/v1"
ANIMAL_API_QUERY_ENDPOINT = "/animals"
ANIMAL_API_QUERY_PARAM_NAME = "name"
