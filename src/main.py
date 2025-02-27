import os
from datetime import datetime
import logging
from dotenv import load_dotenv

from src.etl.extract import extract_data
from src.etl.load import insert_player, create_database, create_players_table
from src.etl.transform import transform_data

# this creates a variable that tracks the time we executed the script
start_time = datetime.now()

# make a connection to redshift and extract online transactions data with transformation tasks
print("\nExtracting and transforming data in sql...")
data = extract_data()
print('\nExtraction and transformation in sql completed')

# transform data
print("\nTransforming data...")
cleaned_data = transform_data(data)
print('\nTransformed data completed successfully')

# checking for existence of database and table
print("\nChecking for existence of database...")
create_database()

print("\nChecking for existence of table...")
create_players_table()

# inserting players
print("\nLoading data into database...")


for player in cleaned_data:
    insert_player(player)

execution_time = datetime.now() - start_time
print(f"\nTotal execution time (hh:mm:ss.ms) {execution_time}")