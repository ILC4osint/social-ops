# pylint: disable=unsupported-binary-operation,unused-argument,missing-timeout,broad-exception-raised,too-few-public-methods,wrong-import-order
import os

import requests
from ..models.outlets import FbPost
from dotenv import load_dotenv

load_dotenv()
VETRIC_API_KEY = os.environ.get("VETRIC_API_KEY")
class VetricAdapter:
    """The Ventric Adapter used to make API connetions to Social Media outlets
    https://docs.vetric.io
    Raises:
        Exception: _description_

    Returns:
        _type_: _description_
    """
    BASE_URL = {
        "ventric": "https://api.vetric.io/facebook/v1/search/posts"
    }

    def __init__(self,source: str,api_key: str|None = None):
        """Initialize the VetricAdapter.

        Args:
            source (str): _description_
            api_key (str | None, optional): _description_. Defaults to None.
        """
        self.api_key = api_key = os.environ.get("VETRIC_API_KEY", VETRIC_API_KEY)
        self.source = source

    def search_posts(self, query: str) -> list[FbPost]:
        """Use to search for Facebook posts usinga query

        Args:
            query (str): _description_

        Raises:
            Exception: _description_

        Returns:
            list[FbPost]: _description_
        """
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.post(self.BASE_URL[self.source], headers=headers, data=f'typed_query={query}')

        if response.status_code != 200:
            raise Exception("Error fetching data from Vetric")

        data = response.json()
        posts = data.get('data', [])

        return [FbPost(content=post['message']) for post in posts]  # Adjust field extraction accordingly
