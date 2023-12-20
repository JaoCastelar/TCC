import pandas as pd

df = pd.read_csv('base_nba_final.csv')

# df_home = pd.DataFrame(columns=['Team', 'FGM', 'FGA', '3PM', '3PA', 'FTM', 'FTA', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF'])
# df_away = pd.DataFrame(columns=['a.Team', 'a.FGM', 'a.FGA', 'a.3PM', 'a.3PA', 'a.FTM', 'a.FTA', 'a.OREB', 'a.DREB', 'a.REB', 'a.AST', 'a.STL', 'a.BLK', 'a.TOV', 'a.PF'])

df_home = pd.DataFrame(columns=['Team', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'FTM', 'FTA', 'FT%', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF'])
df_away = pd.DataFrame(columns=['a.Team', 'a.FGM', 'a.FGA', 'a.FG%', 'a.3PM', 'a.3PA', 'a.3P%', 'a.FTM', 'a.FTA', 'a.FT%', 'a.OREB', 'a.DREB', 'a.REB', 'a.AST', 'a.STL', 'a.BLK', 'a.TOV', 'a.PF'])

# df_home_final = pd.DataFrame(columns=['FGM', 'FGA', '3PM', '3PA', 'FTM', 'FTA', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF'])
# df_away_final = pd.DataFrame(columns=['a.FGM', 'a.FGA', 'a.3PM', 'a.3PA', 'a.FTM', 'a.FTA', 'a.OREB', 'a.DREB', 'a.REB', 'a.AST', 'a.STL', 'a.BLK', 'a.TOV', 'a.PF'])

df_home_final = pd.DataFrame(columns=['FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'FTM', 'FTA', 'FT%', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF'])
df_away_final = pd.DataFrame(columns=['a.FGM', 'a.FGA', 'a.FG%', 'a.3PM', 'a.3PA', 'a.3P%', 'a.FTM', 'a.FTA', 'a.FT%', 'a.OREB', 'a.DREB', 'a.REB', 'a.AST', 'a.STL', 'a.BLK', 'a.TOV', 'a.PF'])

df = df.drop(['Unnamed: 0'], axis=1)

#df.columns = ['Team', 'a.Team', 'Match Up', 'a.Match Up', 'Game Date', 'a.Game Date', 'W/L', 'a.W/L', 'PTS', 'a.PTS', 'FGM', 'a.FGM', 'FGA', 'a.FGA', '3PM', 'a.3PM', '3PA', 'a.3PA', 'FTM', 'a.FTM', 'FTA', 'a.FTA', 'OREB', 'a.OREB', 'DREB', 'a.DREB', 'REB', 'a.REB', 'AST', 'a.AST', 'STL', 'a.STL', 'BLK', 'a.BLK', 'TOV', 'a.TOV', 'PF', 'a.PF', '+/-', 'a.+/-']

df = df.drop(['Match Up', 'a.Match Up', 'Game Date', 'a.Game Date', 'W/L', 'a.W/L', 'PTS', 'a.PTS', '+/-', 'a.+/-'], axis=1)

l, c = df.shape

cont = 0
listah = []
listaa = []

#Home

for i in range(l):
    
    for j in range(c):
        
        el = df.iloc[i, j]
        if j <= 17:
            listah.append(el)
        else:
            listaa.append(el)
            
        
    df_home.loc[cont] = listah
    df_away.loc[cont] = listaa
    cont = cont + 1
    listah.clear()
    listaa.clear()

item1,item2,item3,item4,item5,item6,item7,item8,item9,item10,item11,item12,item13,item14,item15 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
item16,item17,item18,item19,item20,item21,item22,item23,item24,item25,item26,item27,item28,item29,item30 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

# lista1,lista2,lista3,lista4,lista5,lista6,lista7,lista8,lista9,lista10,lista11,lista12,lista13,lista14,lista15 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# lista16,lista17,lista18,lista19,lista20,lista21,lista22,lista23,lista24,lista25,lista26,lista27,lista28,lista29,lista30 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


lista1,lista2,lista3,lista4,lista5,lista6,lista7,lista8,lista9,lista10,lista11,lista12,lista13,lista14,lista15 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
lista16,lista17,lista18,lista19,lista20,lista21,lista22,lista23,lista24,lista25,lista26,lista27,lista28,lista29,lista30 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(l):
    timeh = df_home['Team'][i]
    
    if timeh == 'PHX':
        lista1 = lista1 + df_home.iloc[i, 1:].values
        item1 = item1 + 1
    elif timeh == 'DET':
        lista2 = lista2 + df_home.iloc[i, 1:].values
        item2 = item2 + 1
    elif timeh == 'GSW':
        lista3 = lista3 + df_home.iloc[i, 1:].values
        item3 = item3 + 1
    elif timeh == 'BOS':
        lista4 = lista4 + df_home.iloc[i, 1:].values
        item4 = item4 + 1
    elif timeh == 'LAC':
        lista5 = lista5 + df_home.iloc[i, 1:].values
        item5 = item5 + 1
    elif timeh == 'SAC':
        lista6 = lista6 + df_home.iloc[i, 1:].values
        item6 = item6 + 1
    elif timeh == 'UTA':
        lista7 = lista7 + df_home.iloc[i, 1:].values
        item7 = item7 + 1
    elif timeh == 'POR':
        lista8 = lista8 + df_home.iloc[i, 1:].values
        item8 = item8 + 1
    elif timeh == 'MIN':
        lista9 = lista9 + df_home.iloc[i, 1:].values
        item9 = item9 + 1
    elif timeh == 'MIL':
        lista10 = lista10 + df_home.iloc[i, 1:].values
        item10 = item10 + 1
    elif timeh == 'WAS':
        lista11 = lista11 + df_home.iloc[i, 1:].values
        item11 = item11 + 1
    elif timeh == 'ATL':
        lista12 = lista12 + df_home.iloc[i, 1:].values
        item12 = item12 + 1
    elif timeh == 'DAL':
        lista13 = lista13 + df_home.iloc[i, 1:].values
        item13 = item13 + 1
    elif timeh == 'MEM':
        lista14 = lista14 + df_home.iloc[i, 1:].values
        item14 = item14 + 1
    elif timeh == 'HOU':
        lista15 = lista15 + df_home.iloc[i, 1:].values
        item15 = item15 + 1
    elif timeh == 'NOP':
        lista16 = lista16 + df_home.iloc[i, 1:].values
        item16 = item16 + 1
    elif timeh == 'OKC':
        lista17 = lista17 + df_home.iloc[i, 1:].values
        item17 = item17 + 1
    elif timeh == 'SAS':
        lista18 = lista18 + df_home.iloc[i, 1:].values
        item18 = item18 + 1
    elif timeh == 'CLE':
        lista19 = lista19 + df_home.iloc[i, 1:].values
        item19 = item19 + 1
    elif timeh == 'CHI':
        lista20 = lista20 + df_home.iloc[i, 1:].values
        item20 = item20 + 1
    elif timeh == 'BKN':
        lista21 = lista21 + df_home.iloc[i, 1:].values
        item21 = item21 + 1
    elif timeh == 'TOR':
        lista22 = lista22 + df_home.iloc[i, 1:].values
        item22 = item22 + 1
    elif timeh == 'IND':
        lista23 = lista23 + df_home.iloc[i, 1:].values
        item23 = item23 + 1
    elif timeh == 'MIA':
        lista24 = lista24 + df_home.iloc[i, 1:].values
        item24 = item24 + 1
    elif timeh == 'PHI':
        lista25 = lista25 + df_home.iloc[i, 1:].values
        item25 = item25 + 1
    elif timeh == 'ORL':
        lista26 = lista26 + df_home.iloc[i, 1:].values
        item26 = item26 + 1
    elif timeh == 'NYK':
        lista27 = lista27 + df_home.iloc[i, 1:].values
        item27 = item27 + 1
    elif timeh == 'DEN':
        lista28 = lista28 + df_home.iloc[i, 1:].values
        item28 = item28 + 1
    elif timeh == 'LAL':
        lista29 = lista29 + df_home.iloc[i, 1:].values
        item29 = item29 + 1
    elif timeh == 'CHA':
        lista30 = lista30 + df_home.iloc[i, 1:].values
        item30 = item30 + 1

print(item1,item2,item3,item4,item5,item6,item7,item8,item9,item10,item11,item12,item13,item14,item15,item16,item17,item18,item19,item20,item21,item22,item23,item24,item25,item26,item27,item28,item29,item30)

# for i in range(14):
#     lista1[i] = int(lista1[i] / item1)
# df_home_final.loc[0] = lista1
# for i in range(14):
#     lista2[i] = int(lista2[i] / item2)
# df_home_final.loc[1] = lista2
# for i in range(14):
#     lista3[i] = int(lista3[i] / item3)
# df_home_final.loc[2] = lista3
# for i in range(14):
#     lista4[i] = int(lista4[i] / item4)
# df_home_final.loc[3] = lista4
# for i in range(14):
#     lista5[i] = int(lista5[i] / item5)
# df_home_final.loc[4] = lista5
# for i in range(14):
#     lista6[i] = int(lista6[i] / item6)
# df_home_final.loc[5] = lista6
# for i in range(14):
#     lista7[i] = int(lista7[i] / item7)
# df_home_final.loc[6] = lista7
# for i in range(14):
#     lista8[i] = int(lista8[i] / item8)
# df_home_final.loc[7] = lista8
# for i in range(14):
#     lista9[i] = int(lista9[i] / item9)
# df_home_final.loc[8] = lista9
# for i in range(14):
#     lista10[i] = int(lista10[i] / item10)
# df_home_final.loc[9] = lista10
# for i in range(14):
#     lista11[i] = int(lista11[i] / item11)
# df_home_final.loc[10] = lista11
# for i in range(14):
#     lista12[i] = int(lista12[i] / item12)
# df_home_final.loc[11] = lista12
# for i in range(14):
#     lista13[i] = int(lista13[i] / item13)
# df_home_final.loc[12] = lista13
# for i in range(14):
#     lista14[i] = int(lista14[i] / item14)
# df_home_final.loc[13] = lista14
# for i in range(14):
#     lista15[i] = int(lista15[i] / item15)
# df_home_final.loc[14] = lista15
# for i in range(14):
#     lista16[i] = int(lista16[i] / item16)
# df_home_final.loc[15] = lista16
# for i in range(14):
#     lista17[i] = int(lista17[i] / item17)
# df_home_final.loc[16] = lista17
# for i in range(14):
#     lista18[i] = int(lista18[i] / item18)
# df_home_final.loc[17] = lista18
# for i in range(14):
#     lista19[i] = int(lista19[i] / item19)
# df_home_final.loc[18] = lista19
# for i in range(14):
#     lista20[i] = int(lista20[i] / item20)
# df_home_final.loc[19] = lista20
# for i in range(14):
#     lista21[i] = int(lista21[i] / item21)
# df_home_final.loc[20] = lista21
# for i in range(14):
#     lista22[i] = int(lista22[i] / item22)
# df_home_final.loc[21] = lista22
# for i in range(14):
#     lista23[i] = int(lista23[i] / item23)
# df_home_final.loc[22] = lista23
# for i in range(14):
#     lista24[i] = int(lista24[i] / item24)
# df_home_final.loc[23] = lista24
# for i in range(14):
#     lista25[i] = int(lista25[i] / item25)
# df_home_final.loc[24] = lista25
# for i in range(14):
#     lista26[i] = int(lista26[i] / item26)
# df_home_final.loc[25] = lista26
# for i in range(14):
#     lista27[i] = int(lista27[i] / item27)
# df_home_final.loc[26] = lista27
# for i in range(14):
#     lista28[i] = int(lista28[i] / item28)
# df_home_final.loc[27] = lista28
# for i in range(14):
#     lista29[i] = int(lista29[i] / item29)
# df_home_final.loc[28] = lista29
# for i in range(14):
#     lista30[i] = int(lista30[i] / item30)
# df_home_final.loc[29] = lista30

for i in range(17):
    lista1[i] = int(lista1[i] / item1)
    lista2[i] = int(lista2[i] / item2)
    lista3[i] = int(lista3[i] / item3)
    lista4[i] = int(lista4[i] / item4)
    lista5[i] = int(lista5[i] / item5)
    lista6[i] = int(lista6[i] / item6)
    lista7[i] = int(lista7[i] / item7)
    lista8[i] = int(lista8[i] / item8)
    lista9[i] = int(lista9[i] / item9)
    lista10[i] = int(lista10[i] / item10)
    lista11[i] = int(lista11[i] / item11)
    lista12[i] = int(lista12[i] / item12)
    lista13[i] = int(lista13[i] / item13)
    lista14[i] = int(lista14[i] / item14)
    lista15[i] = int(lista15[i] / item15)
    lista16[i] = int(lista16[i] / item16)
    lista17[i] = int(lista17[i] / item17)
    lista18[i] = int(lista18[i] / item18)
    lista19[i] = int(lista19[i] / item19)
    lista20[i] = int(lista20[i] / item20)
    lista21[i] = int(lista21[i] / item21)
    lista22[i] = int(lista22[i] / item22)
    lista23[i] = int(lista23[i] / item23)
    lista24[i] = int(lista24[i] / item24)
    lista25[i] = int(lista25[i] / item25)
    lista26[i] = int(lista26[i] / item26)
    lista27[i] = int(lista27[i] / item27)
    lista28[i] = int(lista28[i] / item28)
    lista29[i] = int(lista29[i] / item29)
    lista30[i] = int(lista30[i] / item30)


df_home_final.loc[0] = lista1
df_home_final.loc[1] = lista2
df_home_final.loc[2] = lista3
df_home_final.loc[3] = lista4
df_home_final.loc[4] = lista5
df_home_final.loc[5] = lista6
df_home_final.loc[6] = lista7
df_home_final.loc[7] = lista8
df_home_final.loc[8] = lista9
df_home_final.loc[9] = lista10
df_home_final.loc[10] = lista11
df_home_final.loc[11] = lista12
df_home_final.loc[12] = lista13
df_home_final.loc[13] = lista14
df_home_final.loc[14] = lista15
df_home_final.loc[15] = lista16
df_home_final.loc[16] = lista17
df_home_final.loc[17] = lista18
df_home_final.loc[18] = lista19
df_home_final.loc[19] = lista20
df_home_final.loc[20] = lista21
df_home_final.loc[21] = lista22
df_home_final.loc[22] = lista23
df_home_final.loc[23] = lista24
df_home_final.loc[24] = lista25
df_home_final.loc[25] = lista26
df_home_final.loc[26] = lista27
df_home_final.loc[27] = lista28
df_home_final.loc[28] = lista29
df_home_final.loc[29] = lista30

df_home_final.insert(0, 'Team', ['PHX', 'DET', 'GSW', 'BOS', 'LAC', 'SAC', 'UTA', 'POR', 'MIN', 'MIL', 'WAS', 'ATL', 'DAL', 'MEM', 'HOU', 'NOP', 'OKC', 'SAS', 'CLE', 'CHI', 'BKN', 'TOR', 'IND', 'MIA', 'PHI', 'ORL', 'NYK', 'DEN', 'LAL', 'CHA'])

print(df_home_final)


item1,item2,item3,item4,item5,item6,item7,item8,item9,item10,item11,item12,item13,item14,item15 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
item16,item17,item18,item19,item20,item21,item22,item23,item24,item25,item26,item27,item28,item29,item30 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

# lista1,lista2,lista3,lista4,lista5,lista6,lista7,lista8,lista9,lista10,lista11,lista12,lista13,lista14,lista15 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# lista16,lista17,lista18,lista19,lista20,lista21,lista22,lista23,lista24,lista25,lista26,lista27,lista28,lista29,lista30 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


lista1,lista2,lista3,lista4,lista5,lista6,lista7,lista8,lista9,lista10,lista11,lista12,lista13,lista14,lista15 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
lista16,lista17,lista18,lista19,lista20,lista21,lista22,lista23,lista24,lista25,lista26,lista27,lista28,lista29,lista30 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(l):
    timea = df_away['a.Team'][i]
    
    if timea == 'PHX':
        lista1 = lista1 + df_home.iloc[i, 1:].values
        item1 = item1 + 1
    elif timea == 'DET':
        lista2 = lista2 + df_home.iloc[i, 1:].values
        item2 = item2 + 1
    elif timea == 'GSW':
        lista3 = lista3 + df_home.iloc[i, 1:].values
        item3 = item3 + 1
    elif timea == 'BOS':
        lista4 = lista4 + df_home.iloc[i, 1:].values
        item4 = item4 + 1
    elif timea == 'LAC':
        lista5 = lista5 + df_home.iloc[i, 1:].values
        item5 = item5 + 1
    elif timea == 'SAC':
        lista6 = lista6 + df_home.iloc[i, 1:].values
        item6 = item6 + 1
    elif timea == 'UTA':
        lista7 = lista7 + df_home.iloc[i, 1:].values
        item7 = item7 + 1
    elif timea == 'POR':
        lista8 = lista8 + df_home.iloc[i, 1:].values
        item8 = item8 + 1
    elif timea == 'MIN':
        lista9 = lista9 + df_home.iloc[i, 1:].values
        item9 = item9 + 1
    elif timea == 'MIL':
        lista10 = lista10 + df_home.iloc[i, 1:].values
        item10 = item10 + 1
    elif timea == 'WAS':
        lista11 = lista11 + df_home.iloc[i, 1:].values
        item11 = item11 + 1
    elif timea == 'ATL':
        lista12 = lista12 + df_home.iloc[i, 1:].values
        item12 = item12 + 1
    elif timea == 'DAL':
        lista13 = lista13 + df_home.iloc[i, 1:].values
        item13 = item13 + 1
    elif timea == 'MEM':
        lista14 = lista14 + df_home.iloc[i, 1:].values
        item14 = item14 + 1
    elif timea == 'HOU':
        lista15 = lista15 + df_home.iloc[i, 1:].values
        item15 = item15 + 1
    elif timea == 'NOP':
        lista16 = lista16 + df_home.iloc[i, 1:].values
        item16 = item16 + 1
    elif timea == 'OKC':
        lista17 = lista17 + df_home.iloc[i, 1:].values
        item17 = item17 + 1
    elif timea == 'SAS':
        lista18 = lista18 + df_home.iloc[i, 1:].values
        item18 = item18 + 1
    elif timea == 'CLE':
        lista19 = lista19 + df_home.iloc[i, 1:].values
        item19 = item19 + 1
    elif timea == 'CHI':
        lista20 = lista20 + df_home.iloc[i, 1:].values
        item20 = item20 + 1
    elif timea == 'BKN':
        lista21 = lista21 + df_home.iloc[i, 1:].values
        item21 = item21 + 1
    elif timea == 'TOR':
        lista22 = lista22 + df_home.iloc[i, 1:].values
        item22 = item22 + 1
    elif timea == 'IND':
        lista23 = lista23 + df_home.iloc[i, 1:].values
        item23 = item23 + 1
    elif timea == 'MIA':
        lista24 = lista24 + df_home.iloc[i, 1:].values
        item24 = item24 + 1
    elif timea == 'PHI':
        lista25 = lista25 + df_home.iloc[i, 1:].values
        item25 = item25 + 1
    elif timea == 'ORL':
        lista26 = lista26 + df_home.iloc[i, 1:].values
        item26 = item26 + 1
    elif timea == 'NYK':
        lista27 = lista27 + df_home.iloc[i, 1:].values
        item27 = item27 + 1
    elif timea == 'DEN':
        lista28 = lista28 + df_home.iloc[i, 1:].values
        item28 = item28 + 1
    elif timea == 'LAL':
        lista29 = lista29 + df_home.iloc[i, 1:].values
        item29 = item29 + 1
    elif timea == 'CHA':
        lista30 = lista30 + df_home.iloc[i, 1:].values
        item30 = item30 + 1
        
print(item1,item2,item3,item4,item5,item6,item7,item8,item9,item10,item11,item12,item13,item14,item15,item16,item17,item18,item19,item20,item21,item22,item23,item24,item25,item26,item27,item28,item29,item30)        

# for i in range(14):
#     lista1[i] = int(lista1[i] / item1)
# df_away_final.loc[0] = lista1
# for i in range(14):
#     lista2[i] = int(lista2[i] / item2)
# df_away_final.loc[1] = lista2
# for i in range(14):
#     lista3[i] = int(lista3[i] / item3)
# df_away_final.loc[2] = lista3
# for i in range(14):
#     lista4[i] = int(lista4[i] / item4)
# df_away_final.loc[3] = lista4
# for i in range(14):
#     lista5[i] = int(lista5[i] / item5)
# df_away_final.loc[4] = lista5
# for i in range(14):
#     lista6[i] = int(lista6[i] / item6)
# df_away_final.loc[5] = lista6
# for i in range(14):
#     lista7[i] = int(lista7[i] / item7)
# df_away_final.loc[6] = lista7
# for i in range(14):
#     lista8[i] = int(lista8[i] / item8)
# df_away_final.loc[7] = lista8
# for i in range(14):
#     lista9[i] = int(lista9[i] / item9)
# df_away_final.loc[8] = lista9
# for i in range(14):
#     lista10[i] = int(lista10[i] / item10)
# df_away_final.loc[9] = lista10
# for i in range(14):
#     lista11[i] = int(lista11[i] / item11)
# df_away_final.loc[10] = lista11
# for i in range(14):
#     lista12[i] = int(lista12[i] / item12)
# df_away_final.loc[11] = lista12
# for i in range(14):
#     lista13[i] = int(lista13[i] / item13)
# df_away_final.loc[12] = lista13
# for i in range(14):
#     lista14[i] = int(lista14[i] / item14)
# df_away_final.loc[13] = lista14
# for i in range(14):
#     lista15[i] = int(lista15[i] / item15)
# df_away_final.loc[14] = lista15
# for i in range(14):
#     lista16[i] = int(lista16[i] / item16)
# df_away_final.loc[15] = lista16
# for i in range(14):
#     lista17[i] = int(lista17[i] / item17)
# df_away_final.loc[16] = lista17
# for i in range(14):
#     lista18[i] = int(lista18[i] / item18)
# df_away_final.loc[17] = lista18
# for i in range(14):
#     lista19[i] = int(lista19[i] / item19)
# df_away_final.loc[18] = lista19
# for i in range(14):
#     lista20[i] = int(lista20[i] / item20)
# df_away_final.loc[19] = lista20
# for i in range(14):
#     lista21[i] = int(lista21[i] / item21)
# df_away_final.loc[20] = lista21
# for i in range(14):
#     lista22[i] = int(lista22[i] / item22)
# df_away_final.loc[21] = lista22
# for i in range(14):
#     lista23[i] = int(lista23[i] / item23)
# df_away_final.loc[22] = lista23
# for i in range(14):
#     lista24[i] = int(lista24[i] / item24)
# df_away_final.loc[23] = lista24
# for i in range(14):
#     lista25[i] = int(lista25[i] / item25)
# df_away_final.loc[24] = lista25
# for i in range(14):
#     lista26[i] = int(lista26[i] / item26)
# df_away_final.loc[25] = lista26
# for i in range(14):
#     lista27[i] = int(lista27[i] / item27)
# df_away_final.loc[26] = lista27
# for i in range(14):
#     lista28[i] = int(lista28[i] / item28)
# df_away_final.loc[27] = lista28
# for i in range(14):
#     lista29[i] = int(lista29[i] / item29)
# df_away_final.loc[28] = lista29
# for i in range(14):
#     lista30[i] = int(lista30[i] / item30)
# df_away_final.loc[29] = lista30

for i in range(17):
    lista1[i] = int(lista1[i] / item1)
    lista2[i] = int(lista2[i] / item2)
    lista3[i] = int(lista3[i] / item3)
    lista4[i] = int(lista4[i] / item4)
    lista5[i] = int(lista5[i] / item5)
    lista6[i] = int(lista6[i] / item6)
    lista7[i] = int(lista7[i] / item7)
    lista8[i] = int(lista8[i] / item8)
    lista9[i] = int(lista9[i] / item9)
    lista10[i] = int(lista10[i] / item10)
    lista11[i] = int(lista11[i] / item11)
    lista12[i] = int(lista12[i] / item12)
    lista13[i] = int(lista13[i] / item13)
    lista14[i] = int(lista14[i] / item14)
    lista15[i] = int(lista15[i] / item15)
    lista16[i] = int(lista16[i] / item16)
    lista17[i] = int(lista17[i] / item17)
    lista18[i] = int(lista18[i] / item18)
    lista19[i] = int(lista19[i] / item19)
    lista20[i] = int(lista20[i] / item20)
    lista21[i] = int(lista21[i] / item21)
    lista22[i] = int(lista22[i] / item22)
    lista23[i] = int(lista23[i] / item23)
    lista24[i] = int(lista24[i] / item24)
    lista25[i] = int(lista25[i] / item25)
    lista26[i] = int(lista26[i] / item26)
    lista27[i] = int(lista27[i] / item27)
    lista28[i] = int(lista28[i] / item28)
    lista29[i] = int(lista29[i] / item29)
    lista30[i] = int(lista30[i] / item30)


df_away_final.loc[0] = lista1
df_away_final.loc[1] = lista2
df_away_final.loc[2] = lista3
df_away_final.loc[3] = lista4
df_away_final.loc[4] = lista5
df_away_final.loc[5] = lista6
df_away_final.loc[6] = lista7
df_away_final.loc[7] = lista8
df_away_final.loc[8] = lista9
df_away_final.loc[9] = lista10
df_away_final.loc[10] = lista11
df_away_final.loc[11] = lista12
df_away_final.loc[12] = lista13
df_away_final.loc[13] = lista14
df_away_final.loc[14] = lista15
df_away_final.loc[15] = lista16
df_away_final.loc[16] = lista17
df_away_final.loc[17] = lista18
df_away_final.loc[18] = lista19
df_away_final.loc[19] = lista20
df_away_final.loc[20] = lista21
df_away_final.loc[21] = lista22
df_away_final.loc[22] = lista23
df_away_final.loc[23] = lista24
df_away_final.loc[24] = lista25
df_away_final.loc[25] = lista26
df_away_final.loc[26] = lista27
df_away_final.loc[27] = lista28
df_away_final.loc[28] = lista29
df_away_final.loc[29] = lista30
    

df_away_final.insert(0, 'a.Team', ['PHX', 'DET', 'GSW', 'BOS', 'LAC', 'SAC', 'UTA', 'POR', 'MIN', 'MIL', 'WAS', 'ATL', 'DAL', 'MEM', 'HOU', 'NOP', 'OKC', 'SAS', 'CLE', 'CHI', 'BKN', 'TOR', 'IND', 'MIA', 'PHI', 'ORL', 'NYK', 'DEN', 'LAL', 'CHA'])


print(df_away_final)

df_home_final.to_csv('nba_home_final.csv')
df_away_final.to_csv('nba_away_final.csv')

df_home.to_csv('nba_home.csv')
df_away.to_csv('nba_away.csv')