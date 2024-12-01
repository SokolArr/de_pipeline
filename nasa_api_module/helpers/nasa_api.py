import requests
from typing import Dict, List

from .my_logger.my_logger import MyLogger

my_logger = MyLogger(log_level="DEBUG")
my_logger.configure_logger()


class NasaAPI:
    """
    A class to interact with NASA's free APIs.

    Attributes:
        api_key (str): The key parameter for accessing the API.
        api_links (dict): A dictionary of links to various NASA APIs.
        neo_attrs (list): A list of attributes to extract from the API response.

    Methods:
        get_api_link_by_key(api_links_key: str) -> str:
            Retrieves an API link based on a given key.
        get_neo_data(link: str) -> dict:
            Fetches data from the API.
        parse_neo_data(neo_attrs: list = neo_attrs) -> dict:
            Parses data from the API response.
    """

    api_links: Dict[str, str] = dict(
        {"neo": "https://api.nasa.gov/neo/rest/v1/neo/browse", "geo": ""}
    )
    neo_attrs: List[str] = [
        "id",
        "neo_reference_id",
        "name",
        "designation",
        "orbital_data",
    ]

    def __init__(self, api_key: str, api_links: Dict[str, str] = api_links):
        """
        Initializes an instance of the NasaAPI class.

        Arguments:
            api_key (str): The key parameter for accessing the API.
            api_links (dict, optional): A dictionary of links to various NASA APIs.
                                         Defaults to {"neo": "https://api.nasa.gov/neo/rest/v1/neo/browse"}.
        """
        self.api_key = "?api_key=" + api_key
        self.api_links = api_links

    def get_api_link_by_key(self, api_links_key: str) -> str:
        """
        Retrieves the full API link based on the provided key.

        Arguments:
            api_links_key (str): The key used to retrieve the corresponding link from the api_links dictionary.

        Returns:
            str: The complete API link including the key parameter.

        Raises:
            Exception: If the key is not found in the api_links dictionary.
        """
        try:
            return self.api_links.get(api_links_key) + self.api_key
        except Exception as err:
            my_logger.logger.error(
                f"bad try get nasa api link by keyword. error: {err}"
            )
            return ""

    def get_neo_data(self, link: str) -> dict:
        """
        Fetches data from the API using the provided link.

        Arguments:
            link (str): The API link to make the request to.

        Returns:
            dict: The API response in JSON format.

        Raises:
            Exception: If the API response is empty or another error occurs.
        """
        try:
            response = requests.get(link)
            if response:
                data = response.json()
                return data
            else:
                raise Exception(
                    f"no data in response. link: {link}. Check if link correct!"
                )
        except Exception as err:
            my_logger.logger.error(f"bad try get data from api with error: {err}")
            raise err

    def parse_neo_data(self, neo_attrs: List[str] = neo_attrs) -> dict:
        """
        Parses data from the API response.

        Arguments:
            neo_attrs (list, optional): A list of attributes to extract from the API response.
                                        Defaults to ["id", "neo_reference_id", "name", "designation", "orbital_data"].

        Returns:
            dict: A dictionary with two keys: 'metadata' and 'objects'.
                  'metadata' contains page metadata, while 'objects' contains a list of objects with selected attributes.

        Raises:
            Exception: If there is an issue parsing the data.
        """
        try:
            data = self.get_neo_data(self.get_api_link_by_key("neo"))
            neo_metadata = data.get("page")
            neo_data_objects = data.get("near_earth_objects")
            neo_objects = []

            if not neo_data_objects:
                my_logger.logger.warning("No near earth objects found in API response.")
                return {"metadata": {}, "objects": []}

            for obj in neo_data_objects:
                inline_obj = {}
                for attr in neo_attrs:
                    inline_obj[attr] = obj[attr]
                neo_objects.append(inline_obj)

            return {
                "metadata": neo_metadata,
                "objects": neo_objects,
            }
        except:
            my_logger.logger.error("bad try parse neo data")
            return {
                "metadata": {},
                "objects": [{}],
            }
