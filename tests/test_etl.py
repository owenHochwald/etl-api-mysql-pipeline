import pytest
from src.etl.extract import extract_data
from src.etl.transform import transform_data

def test_extract_data():
    """Test that extract_data fetches NBA game data."""
    data = extract_data()
    assert isinstance(data, list)  # Data should be a dictionary
    assert 2 == data[:][0]['id']  # Checking if first player has id element

def test_transform_data():
    """Test that transform_data cleans and processes the data correctly."""
    sample_data = [{
        'id': 2,
        'firstname': 'Quincy',
        'lastname': 'Acy',
        'birth': {
            'date': '1990-10-06',
            'country': 'USA'
        },
        'nba': {
            'start': 2012,
            'pro': 6
        },
        'height': {
            'feets': '6',
            'inches': '7',
            'meters': '2.01'
        },
        'weight': {
            'pounds': '240',
            'kilograms': '108.9'
        },
        'college': 'Baylor',
        'affiliation': 'Baylor/USA',
        'leagues': {
            'standard': {
                'jersey': 4,
                'active': True,
                'pos': 'F'
            }
        }
    }]

    transformed = transform_data(sample_data)
    
    assert isinstance(transformed, list)
    assert len(transformed) == 1
    
    player = transformed[0]
    assert player["player_id"] == 2
    assert player["name"] == "Quincy Acy"
    assert player["nba_start_year"] == 2012
    assert player["height"] == '2.01'
    assert player["weight"] == '108.9'
    assert player["position"] == "F"
    assert player["jersey_number"] == 4
