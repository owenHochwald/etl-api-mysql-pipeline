import os
import sys
from src.api.fetch_data import fetch_nba_data

import requests

def extract_data():
    """Fetches NBA game data from the API and selects info out."""
    response = fetch_nba_data()
    return response.get('response')


