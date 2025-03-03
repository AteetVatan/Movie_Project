"""Module For API requests"""
import requests

from enumerations import OMDBApiParamTypes
from models.api_request_model import ApiRequestModel


class ApiHelper:
    """Class For API requests"""
    __api_request_model: ApiRequestModel

    def __init__(self, api_request_model: ApiRequestModel):
        self.__api_request_model = api_request_model

    def get_data(self, value, param_type: OMDBApiParamTypes):
        """Method to get the data."""
        api_url = self.__api_request_model.endpoint_url
        query_string = self.__api_request_model.get_query_string(param_type, value)
        response = ApiHelper.__get_request_with_url(api_url + query_string)
        try:
            if response.status_code != requests.codes.ok:
                raise ValueError("Error:", response.status_code, response.text)

            return response.json()
        except ValueError:
            return {"error": "Invalid JSON response"}

    @staticmethod
    def __get_request_with_url(url):
        """Method to generate HTTP get request."""
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            return response

        except requests.exceptions.Timeout:
            return {"error": "Request timed out"}
        except requests.exceptions.ConnectionError:
            return {"error": "Failed to connect to the server"}
        except requests.exceptions.HTTPError as http_err:
            return {"error": f"HTTP error occurred: {http_err}"}
        except requests.exceptions.RequestException as err:
            return {"error": f"An error occurred: {err}"}
