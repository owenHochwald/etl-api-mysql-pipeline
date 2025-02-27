# NBA Players ETL Pipeline

A Python-based ETL (Extract, Transform, Load) pipeline that fetches NBA player data from the RapidAPI NBA API, processes it, and stores it in a MySQL database for analysis.

## Features

- **Data Extraction**: Fetches NBA player data from the RapidAPI NBA API
- **Data Transformation**: Cleans and standardizes player information including:
  - Player identification
  - Personal details (name)
  - Physical attributes (height in meters, weight in kilograms)
  - Professional information (NBA start year, position, jersey number)
- **Data Loading**: Stores processed data in a MySQL database with automatic table creation
- **Error Handling**: Robust error checking during transformation
- **Performance Monitoring**: Tracks execution time for the entire ETL process
- **Testing**: Comprehensive test suite for API connectivity and data processing

## Technical Stack

- Python 3.x
- MySQL
- RapidAPI NBA API
- Key Libraries:
  - `mysql-connector-python` for database operations
  - `requests` for API calls
  - `python-dotenv` for environment variable management
  - `pytest` for testing


## User Stories

1. **As a Data Analyst**
   - I want to access current NBA player data
   - So that I can perform analysis on player statistics and demographics

2. **As a Database Administrator**
   - I want automated database and table creation
   - So that I can easily set up the required infrastructure

3. **As a Sports Researcher**
   - I want standardized physical measurements
   - So that I can compare players using consistent metrics

4. **As a Development Team Member**
   - I want execution time tracking
   - So that I can monitor and optimize pipeline performance

## Development Process

1. **Initial Setup**
   - Environment configuration
   - API integration setup
   - Database schema design

2. **ETL Pipeline Development**
   - Extract: Implemented API data fetching
   - Transform: Created data cleaning and standardization processes
   - Load: Developed database operations with upsert capability

3. **Testing**
   - API connectivity testing
   - Data transformation validation
   - Database operation verification

4. **Performance Optimization**
   - Execution time tracking
   - Error handling implementation
   - Code modularization

## Setup and Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file with the following variables:
   ```
   API_KEY=your_rapidapi_key
   USER=your_mysql_user
   PASSWORD=your_mysql_password
   ```
4. Run the pipeline:
   ```bash
   python src/main.py
   ```

## Testing

Run the test suite using:
    ``` pytest tests/ ```

    
## License

This project is licensed under the MIT License - see the LICENSE file for details.