import pandas as pd
import numpy as np

df_home = pd.read_csv('nba_home_final.csv')
df_away = pd.read_csv('nba_away_final.csv')

df_tot_home = pd.read_csv('nba_home.csv')
df_tot_away = pd.read_csv('nba_away.csv')

# df_jg_int = pd.DataFrame(columns=['FGM', 'a.FGM', 'FGA', 'a.FGA', '3PM', 'a.3PM', '3PA', 'a.3PA', 'FTM', 'a.FTM', 'FTA', 'a.FTA', 'OREB', 'a.OREB', 'DREB', 'a.DREB', 'REB', 'a.REB', 'AST', 'a.AST', 'STL', 'a.STL', 'BLK', 'a.BLK', 'TOV', 'a.TOV', 'PF', 'a.PF'])
# df_jg_int = pd.DataFrame(columns=['FGM', 'FGA', '3PM', '3PA', 'FTM', 'FTA', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'a.FGM', 'a.FGA', 'a.3PM', 'a.3PA', 'a.FTM', 'a.FTA', 'a.OREB',  'a.DREB', 'a.REB', 'a.AST', 'a.STL', 'a.BLK', 'a.TOV', 'a.PF'])
df_jg_int = pd.DataFrame(columns=['FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'FTM', 'FTA', 'FT%', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'a.FGM', 'a.FGA', 'a.FG%', 'a.3PM', 'a.3PA', 'a.3P%', 'a.FTM', 'a.FTA', 'a.FT%', 'a.OREB', 'a.DREB', 'a.REB', 'a.AST', 'a.STL', 'a.BLK', 'a.TOV', 'a.PF'])

df_list_matches = pd.read_csv('../odds/matches.csv')

df_nome_ind = pd.DataFrame({'Team': df_home['Team']})
df_nome_final = pd.DataFrame(columns=['Team', 'a.Team'])

df_home = df_home.drop(['Unnamed: 0', 'Team'], axis=1)
df_away = df_away.drop(['Unnamed: 0', 'a.Team'], axis=1)

df_tot_nome = pd.DataFrame({'Team': df_tot_home['Team'], 'a.Team': df_tot_away['a.Team']})

df_tot_nome.to_csv('nomes.csv')

df_tot_home = df_tot_home.drop(['Unnamed: 0', 'Team'], axis=1)
df_tot_away = df_tot_away.drop(['Unnamed: 0', 'a.Team'], axis=1)

cont = 0
time_v = []
jogo = []
game = []

l, c = df_tot_home.shape

lm, cm = df_list_matches.shape

for i in range(lm):
    
    item1, item2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    item1v, item2v = 0, 0
    
    time_h = df_list_matches['Team'][i]
    time_a = df_list_matches['a.Team'][i]
    
    ind_h = df_nome_ind.index[df_nome_ind['Team'] == time_h].to_list()
    ind_a = df_nome_ind.index[df_nome_ind['Team'] == time_a].to_list()
    
    game.append(time_h)
    game.append(time_a)
    
    for i in range(l):
        if df_tot_nome['Team'][i] == time_h and df_tot_nome['a.Team'][i] == time_a:
            item1 = item1 + df_tot_home.iloc[i, :].values
            item2 = item2 + df_tot_away.iloc[i, :].values
            item1v = item1v + 1
            item2v = item2v + 1
                
    print(item1v, "\n", item2v, "\n", item1, "\n", item2)
    
    # if item1v != 0:
    #     for i in range(17):
    #         item1[i] = int(item1[i]/item1v)
    #         item2[i] = int(item2[i]/item2v)

    #     for i in range(17):
    #         el = item1[i]
    #         jogo.append(el)
            
    #     for i in range(17):
    #         el = item2[i]
    #         jogo.append(el)
    # else:
    for i in range(17):
        el = df_away.iloc[ind_a[0], i]
        time_v.append(el)
        
    for i in range(17):
        el = df_home.iloc[ind_h[0], i]
        jogo.append(el)
        
    for i in range(17):
        el = time_v[i]
        jogo.append(el)
    
    df_jg_int.loc[cont] = jogo
    df_nome_final.loc[cont] = game
    cont = cont + 1
    time_v.clear()
    jogo.clear()
    game.clear()
    print(df_jg_int)
    print(df_nome_final)

df_nome_final.to_csv('time_jogos_final.csv', index=False)
df_jg_int.to_csv('jogos_noite_final.csv', index=False)