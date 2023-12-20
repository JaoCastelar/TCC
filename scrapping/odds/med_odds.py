import pandas as pd

df_odds = pd.read_csv('odds.csv')

df_odds_med = pd.DataFrame

df_odds_med.columns = ['']

md_oddHome = 0
md_oddAway = 0
md_oddsHome = []
md_oddsAway = []

oL, oC = df_odds.shape

for i in range(oL):
    if i % 7 == 0:
        for j in range(i+7):
            md_oddHome = float(df_odds['Home'][j])
            md_oddAway = float(df_odds['Away'][j])
        
        md_oddsHome.append((md_oddHome/7))
        md_oddsAway.append((md_oddAway/7))