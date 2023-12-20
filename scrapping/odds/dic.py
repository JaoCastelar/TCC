import pandas as pd

nba_team_mapping = {
    "Atlanta Hawks": "ATL",
    "Boston Celtics": "BOS",
    "Brooklyn Nets": "BKN",
    "Charlotte Hornets": "CHA",
    "Chicago Bulls": "CHI",
    "Cleveland Cavaliers": "CLE",
    "Dallas Mavericks": "DAL",
    "Denver Nuggets": "DEN",
    "Detroit Pistons": "DET",
    "Golden State Warriors": "GSW",
    "Houston Rockets": "HOU",
    "Indiana Pacers": "IND",
    "Los Angeles Clippers": "LAC",
    "Los Angeles Lakers": "LAL",
    "Memphis Grizzlies": "MEM",
    "Miami Heat": "MIA",
    "Milwaukee Bucks": "MIL",
    "Minnesota Timberwolves": "MIN",
    "New Orleans Pelicans": "NOP",
    "New York Knicks": "NYK",
    "Oklahoma City Thunder": "OKC",
    "Orlando Magic": "ORL",
    "Philadelphia 76ers": "PHI",
    "Phoenix Suns": "PHX",
    "Portland Trail Blazers": "POR",
    "Sacramento Kings": "SAC",
    "San Antonio Spurs": "SAS",
    "Toronto Raptors": "TOR",
    "Utah Jazz": "UTA",
    "Washington Wizards": "WAS"
}

def convert_team_names_to_abbreviations(df):
    df = pd.read_csv(df)
    filtered_df = df[df.index % 7 == 0]
    
    df_copy = filtered_df.copy()
    df_copy['Team'] = df_copy.apply(lambda row: row['Team'] if row.name % 7 != 0 else nba_team_mapping.get(row['Team'], row['Team']), axis=1)
    df_copy['a.Team'] = df_copy.apply(lambda row: row['a.Team'] if row.name % 7 != 0 else nba_team_mapping.get(row['a.Team'], row['a.Team']), axis=1)
    
    result_df = df_copy[['Team', 'a.Team']]
    
    result_df.to_csv('matches.csv', index=False)
    
    
convert_team_names_to_abbreviations('odds.csv')
