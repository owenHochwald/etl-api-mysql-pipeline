import requests
import os
from dotenv import load_dotenv


load_dotenv()


def fetch_nba_data():

    url = "https://api-nba-v1.p.rapidapi.com/players/statistics"
    api_key = os.environ['API_KEY']


    querystring = {"game":"8133"}

    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "api-nba-v1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response.json()

