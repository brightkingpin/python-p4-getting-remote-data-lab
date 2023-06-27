import pytest
import json
from GetRequester import GetRequester

URL = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
JSON_STRING = b"[\n  {\n    \"name\": \"Daniel\",\n    \"occupation\": \"LG Fridge Salesman\"\n  },\n  {\n    \"name\": \"Joe\",\n    \"occupation\": \"WiFi Fixer\"\n  },\n  {\n    \"name\": \"Avi\",\n    \"occupation\": \"DJ\"\n  },\n  {\n    \"name\": \"Howard\",\n    \"occupation\": \"Mountain Legend\"\n  }\n]\n"
CONVERTED_DATA = [{'name': 'Daniel', 'occupation': 'LG Fridge Salesman'},
                  {'name': 'Joe', 'occupation': 'WiFi Fixer'},
                  {'name': 'Avi', 'occupation': 'DJ'},
                  {'name': 'Howard', 'occupation': 'Mountain Legend'}]

class TestGetRequester:
    def test_get_response(self):
        '''get_response_body function returns response.'''
        requester = GetRequester(URL)
        assert requester.get_response_body() == JSON_STRING

    def test_load_json(self):
        requester = GetRequester(URL)
        response = requester.get_response_body()
        response_str = response.decode('utf-8')  # Convert bytes to string
        assert json.loads(response_str) == CONVERTED_DATA
