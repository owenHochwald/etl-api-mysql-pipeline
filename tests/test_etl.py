import pytest
from src.etl.extract import extract_data
from src.etl.transform import transform_data

def test_extract_data():
    """Test that extract_data fetches NBA game data."""
    data = extract_data()
    assert isinstance(data, dict)  # Data should be a dictionary
    assert "response" in data  # The "response" key should exist
    assert isinstance(data["response"], list)  # Should be a list of players

def test_transform_data():
    """Test that transform_data cleans and processes the data correctly."""
    sample_data = {
        "response": [
            {
                "id": 1,
                "date": "2023-02-15",
                "home_team": {"id": 10, "full_name": "Lakers"},
                "visitor_team": {"id": 20, "full_name": "Bulls"},
                "home_team_score": 110,
                "visitor_team_score": 105
            }
        ]
    }

    transformed = transform_data(sample_data)
    
    assert isinstance(transformed, list)
    assert len(transformed) == 1
    assert transformed[0]["home_team"] == "Lakers"
    assert transformed[0]["visitor_team"] == "Bulls"
