import requests
import pytest
import json
# from src.api.fetch_data import fetch_nba_data
import os
from dotenv import load_dotenv
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from api.fetch_data import fetch_nba_data


load_dotenv()


url = "https://api-nba-v1.p.rapidapi.com/players/statistics"
api_key = os.environ['API_KEY']
querystring = {"game":"8133"}

headers = {
	"x-rapidapi-key": api_key,
	"x-rapidapi-host": "api-nba-v1.p.rapidapi.com"
}

def test_api_response_status():
    """Test if API returns a 200 status code."""
    response = requests.get(url, headers=headers, params=querystring)

    assert response.status_code == 200
    

def test_api_response_json():
    """Test if API returns valid JSON format."""
    response = requests.get(url, headers=headers, params=querystring)
    try:
        data = response.json()
        assert isinstance(data, dict) 
    except json.JSONDecodeError:
        pytest.fail("Response is not valid JSON")

def test_fetch_nba_data():
    """Test our fetch_nba_data function for expected output."""
    data = fetch_nba_data()  # Function should return JSON
    assert isinstance(data, dict)
    assert "response" in data  # Check that the "data" key exists
    assert isinstance(data["response"], list)  # The "data" key should contain a list of games
