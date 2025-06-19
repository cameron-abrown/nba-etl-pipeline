import requests
import pandas as pd

#  SETUP 

# NOTE: Insert your API key here or use environment variable for security
API_KEY = "YOUR_API_KEY_HERE"
headers = {
    "Authorization": f"Bearer {API_KEY}"
}

# STEP 1: Pull games from Jan–Mar 2025 using pagination 
all_games = []

for page in range(1, 5):  # Up to 4 pages (100 games max)
    url = f"https://api.balldontlie.io/v1/games?start_date=2025-01-01&end_date=2025-03-15&per_page=25&page={page}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        # Inspect metadata and page size
        meta = data.get("meta", {})
        print(f"\n Page {page} Meta:", meta)

        games = data.get("data", [])
        print(f"Games returned on page {page}: {len(games)}")

        if not games:
            print("No more games found — breaking loop.")
            break

        all_games.extend(games)

    else:
        print(f"Error on page {page}: {response.status_code}")
        break


# STEP 2: Convert to DataFrame 
df_games = pd.json_normalize(all_games)
print(f"\n Total games collected: {len(df_games)}")
print(f"Unique game IDs: {df_games['id'].nunique()} of {len(df_games)} total rows")

# STEP 3: Trim and clean 
df_cleaned = df_games[[
    'id', 'date', 'home_team.full_name', 'visitor_team.full_name',
    'home_team_score', 'visitor_team_score', 'season'
]].copy()

df_cleaned.columns = [
    'game_id', 'date', 'home_team', 'visitor_team',
    'home_score', 'visitor_score', 'season'
]

df_cleaned['date'] = pd.to_datetime(df_cleaned['date']).dt.date

# 🧹 NEW: Remove duplicate games
df_cleaned.drop_duplicates(subset='game_id', inplace=True)

print("\nCleaned Data Preview:")
print(df_cleaned.head())

import sqlite3

conn = sqlite3.connect("nba_stats.db") # Creates file if it doesn't exist
df_cleaned.to_sql("games", conn, if_exists="replace", index=False)
conn.close()
print("\n Data successfully saved to 'nba_stats.db' in 'games' table. ")