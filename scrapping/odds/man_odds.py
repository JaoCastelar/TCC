import pandas as pd

df = pd.read_csv('odds.csv')

df = df.drop(['TitHome', 'TitAway'], axis=1)

df.to_csv('odds.csv', index=False)