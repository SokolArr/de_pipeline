import yaml

def read_yaml(file_name: str) -> dict:
    with open(file_name) as stream:
        try:
            return dict(yaml.safe_load(stream))
        except yaml.YAMLError as exc:
            raise exc