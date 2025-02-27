import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv() 

def get_db_connection(database=None):
    """Establishes and returns a MySQL database connection."""
    return mysql.connector.connect(
        host="localhost",
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        database=database if database else None   
    )
    
def create_database():
    """Creates the database if it does not already exist."""
    conn = get_db_connection() 
    cursor = conn.cursor()

    cursor.execute(f"CREATE DATABASE IF NOT EXISTS NBA;")

    cursor.close()
    conn.close()
    print(f"Database NBA created.")

def create_players_table():
    """Creates the 'players' table if it doesn't already exist."""
    conn = get_db_connection('NBA')
    cursor = conn.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS players (
        player_id INT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        nba_start_year INT NULL,
        height DECIMAL(4,2) NULL,
        weight DECIMAL(5,2) NULL,
        position VARCHAR(5) NULL,
        jersey_number INT NULL
    );
    """
    
    cursor.execute(create_table_query)
    conn.commit()
    cursor.close()
    conn.close()
    print("Players table created.")

def insert_player(player):
    """Inserts a new player into the database or updates existing record."""
    conn = get_db_connection('NBA')
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO players (player_id, name, nba_start_year, height, weight, position, jersey_number)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE 
        name = VALUES(name),
        nba_start_year = VALUES(nba_start_year),
        height = VALUES(height),
        weight = VALUES(weight),
        position = VALUES(position),
        jersey_number = VALUES(jersey_number);
    """

    data_tuple = (
        player["player_id"],
        player["name"],
        player["nba_start_year"],
        player["height"],
        player["weight"],
        player["position"],
        player["jersey_number"]
    )

    cursor.execute(insert_query, data_tuple)
    conn.commit()
    cursor.close()
    conn.close()

