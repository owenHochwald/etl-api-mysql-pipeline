import datetime
from src.etl.extract import extract_data




def transform_data(raw_data):
    """Cleans and transforms NBA game data for database storage."""
    if not raw_data:
        return []

    transformed_data = []
    
    for player in raw_data:
        
        if not player.get("id") or not player.get("firstname"):
            continue
    
        leagues = player.get("leagues", {})
        standard_league = leagues.get("standard", {})
    
        transformed_data.append({
            "player_id": player["id"],
            "name": player["firstname"] + " " + player["lastname"], 
            "nba_start_year": player["nba"]["start"],
            "height": player["height"]["meters"],
            "weight": player["weight"]["kilograms"],
            "jersey_number": standard_league.get("jersey"),
            "position": standard_league.get("pos")
        })

    return transformed_data

    
response = extract_data()
print(transform_data(response))
