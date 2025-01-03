import utils.yaml_parser as yaml_parser
from dags.modules.api.nasa_api import NasaAPI

# get api key
api_key = yaml_parser.read_yaml("./nasa_api_module/creds.yaml")["main_params"][
    "nasa_api_key"
]

# init nasa api
nasa_api = NasaAPI(api_key)

print(nasa_api.parse_neo_data()["objects"][0])


# TODO make universal module for any apis (link, scheme)
