# nba-etl-pipeline
This is an End-to-end ETL pipeline that extracts NBA game data from a public API, transforms the data with Python/pandas, and then loads it into SQLite for analysis.

# NBA Game Data ETL Pipeline
This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline using live NBA game data from the [balldontlie](https://www.balldontlie.io) API.

## API Key

This project uses the [balldontlie](https://www.balldontlie.io) API.  
You will need to sign up for a free API key and add it to 'extract.py'

Data is extracted from the API, cleaned and transformed using Python and pandas, then loaded into a SQLite database for analysis with SQL queries.

## Features

- Extracts NBA game data (2025 season)
- Handles API pagination and data deduplication
- Cleans and formats data for querying
- Loads data into a local SQLite database (`nba_stats.db`)
- Includes example SQL queries to analyze game outcomes

## Tech Stack

- Python 3.8+
- pandas
- requests
- sqlite3
- SQL

## Example SQL Query

```sql
SELECT 
    date, home_team, visitor_team, 
    home_score, visitor_score, 
    (home_score + visitor_score) AS total_points
FROM games
ORDER BY total_points DESC
LIMIT 10;
