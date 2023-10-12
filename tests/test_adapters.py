import os
import responses

import pytest

from socint.adapters.ventric import VetricAdapter

from tests.mock.fb_search import RESPONSE

VETRIC_API_KEY = "mocked_test_key"
SAMPLE_POSTS_DATA = {
    "data": [
        {"message": "hamas post 1"},
        {"message": "sample hamas 2"},
    ]
}

@responses.activate
def test_search_posts():
    os.environ["VETRIC_API_KEY"] = "mocked_test_key"
    # Mocking the POST request
    responses.add(
        responses.POST,
        "https://api.vetric.io/facebook/v1/search/posts",
        json=RESPONSE,
        status=200
    )

    adapter = VetricAdapter(VETRIC_API_KEY, "ventric")
    posts = adapter.search_posts("hamas")

    assert len(posts) == len(RESPONSE["data"])
    ##TODO: Fix to add real mock support
    # assert posts[0].content == "sample post 1"
    # assert posts[1].content == "sample post 2"

@responses.activate
def test_no_data_response():
    os.environ["VETRIC_API_KEY"] = "mocked_test_key"
    responses.add(
        responses.POST,
        "https://api.vetric.io/facebook/v1/search/posts",
        json={},
        status=200
    )

    adapter = VetricAdapter(VETRIC_API_KEY, "ventric")
    posts = adapter.search_posts("hamas")

    assert len(posts) == 0

@responses.activate
def test_api_error():
    os.environ["VETRIC_API_KEY"] = "mocked_test_key"
    responses.add(
        responses.POST,
        "https://api.vetric.io/facebook/v1/search/posts",
        json={"error": "some error"},
        status=400
    )

    adapter = VetricAdapter(VETRIC_API_KEY, "ventric")
    with pytest.raises(Exception) as e_info:
        adapter.search_posts("hamas")

    assert "Error fetching data from Vetric" in str(e_info.value)