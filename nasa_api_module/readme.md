# nasa_api_module

This module provides an interface for interacting with NASA APIs. It simplifies retrieving data about celestial objects and events provided by NASA.

## Main Features

- **Get API Link By Key:** Retrieves a URL for a specific API using a key.
- **Get NEO Data:** Retrieves data about Near Earth Objects (NEOs) from NASA API.
- **Parse NEO Data:** Parses NEO data for easy use.

## Requirements

- Python 3.x
- requests for making HTTP requests

## Usage

```python
from nasa_api_module import NasaAPI

# Initialize API object
api = NasaAPI("your_api_key")

# Get URL for specific API
url = api.get_api_link_by_key("neo")

# Retrieve NEO data
data = api.get_neo_data(url)

# Parse NEO data
parsed_data = api.parse_neo_data(data)
```

## Example Usage

```python
from nasa_api_module import NasaAPI

# Initialize API object
api = NasaAPI("your_api_key")

# Get URL for specific API
url = api.get_api_link_by_key("neo")

# Retrieve NEO data
data = api.get_neo_data(url)

# Parse NEO data
parsed_data = api.parse_neo_data(data)

# Print information about first object
print(parsed_data["objects"][0])
```
