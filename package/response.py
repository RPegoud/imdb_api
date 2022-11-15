import os
import requests
from dotenv import load_dotenv

load_dotenv()

class Response:
    def __init__(self, status_code, content):
        self._status_code = status_code
        self._content = content
        self._base_url = os.environ.get("base-url")

    # def __repr__(self) -> str:
        
    #     if self._status_code == 200:
    #         print(f'Status code :{self._status_code}')
    #         return self._content
    #     else:
    #         return(f'Error, status code: {self._status_code}')

    # def get_content(self):
    #     _title = self._content['results'][0].get('title', 'title not found')
    #     _id = self._content['results'][0].get('id', 'id not found')
    #     _description = self._content['results'][0].get('description', 'description not found')
    #     return {
    #         'title' : _title,
    #         'id' : _id,
    #         'description' : {_description}
    #     }
