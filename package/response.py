import os
from dotenv import load_dotenv

load_dotenv()

class Response:
    """
    Class encapsulating the response to a Movie Request
    """
    def __init__(self, status_code, content):
        self._status_code = status_code
        self._content = content
        self._base_url = os.environ.get("base-url")
