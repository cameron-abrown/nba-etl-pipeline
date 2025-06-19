import sqlite3
import pandas as pd

#Connect to DB
conn = sqlite3.connect("nba_stats.db")

# Top 10 highest scoring games
query = """
SELECT
    date,
    home_team, 
    visitor_team,
    home_score, 
    visitor_score, 
    (home_score + visitor_score) AS total_points
FROM games
ORDER BY total_points DESC
LIMIT 10;
"""
df = pd.read_sql_query(query,conn)
print("\n Top 10 Highest Scoring Games:")
print(df)

conn.close()