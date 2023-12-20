import pandas as pd

###################################### Abre a base crua #########################################

df = pd.read_csv('base_nba.csv')

df = df.drop('Unnamed: 0', axis=1)

###################################### Cria o dataframe com as colunas definidas #########################################

# # df_final = pd.DataFrame(columns=['Team', 'a.Team', 'Match Up', 'a.Match Up', 'Game Date', 'a.Game Date', 'W/L', 'a.W/L', 'PTS', 'a.PTS', 'FGM', 'a.FGM', 'FGA', 'a.FGA', '3PM', 'a.3PM', '3PA', 'a.3PA', 'FTM', 'a.FTM', 'FTA', 'a.FTA', 'OREB', 'a.OREB', 'DREB', 'a.DREB', 'REB', 'a.REB', 'AST', 'a.AST', 'STL', 'a.STL', 'BLK', 'a.BLK', 'TOV', 'a.TOV', 'PF', 'a.PF', '+/-', 'a.+/-'])
# df_final = pd.DataFrame(columns=['Team', 'Match Up', 'Game Date', 'W/L', 'PTS', 'FGM', 'FGA', '3PM', '3PA', 'FTM', 'FTA', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', '+/-', 'a.Team', 'a.Match Up', 'a.Game Date', 'a.W/L', 'a.PTS', 'a.FGM', 'a.FGA', 'a.3PM', 'a.3PA', 'a.FTM', 'a.FTA', 'a.OREB',  'a.DREB', 'a.REB', 'a.AST', 'a.STL', 'a.BLK', 'a.TOV', 'a.PF', 'a.+/-'])
df_final = pd.DataFrame(columns=['Team', 'Match Up', 'Game Date', 'W/L', 'PTS', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'FTM', 'FTA', 'FT%', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', '+/-', 'a.Team', 'a.Match Up', 'a.Game Date', 'a.W/L', 'a.PTS', 'a.FGM', 'a.FGA', 'a.FG%', 'a.3PM', 'a.3PA', 'a.3P%', 'a.FTM', 'a.FTA', 'a.FT%', 'a.OREB', 'a.DREB', 'a.REB', 'a.AST', 'a.STL', 'a.BLK', 'a.TOV', 'a.PF', 'a.+/-'])

###################################### Gerando variáveis #########################################

l, c = df.shape #Quantidade de linhas e colunas da base crua
cont = 0 #Linha dos primeiros dados
cont2 = [] #Lista de linhas já salvas da base crua
cont3 = 0 #Contador de linhas para a base final
lista = [] #Lista de primeiros e segundos dados
lista2 = [] #Lista auxiliar de organização de casa e visitante

###################################### Abre primeiros dados do jogo #########################################

for i in range(l):
    
    num = df['+/-'][i]
    nome = df['Match Up'][i]
    time1 = df['Team'][i]
    cont = i
    
###################################### Adiciona os primeiros dados na lista #########################################
    
    if cont not in cont2:
        
        if '@' in nome:
            for k in range(c):
                el = df.iloc[i, k]
                lista2.append(el)
                
        elif 'vs' in nome:
            for k in range(c):
                el = df.iloc[i, k]
                lista.append(el)

###################################### Abre segundos dados do jogo #########################################
        
        for j in range(l):
            
            num2 = df['+/-'][j]
            nome2 = df['Match Up'][j]
            
            if (num == (num2*(-1))) and (j not in cont2 and i not in cont2) and (time1 in nome2):

###################################### Adiciona em linhas já visitadas #########################################

                cont2.append(i)
                cont2.append(j)
                
###################################### Adiciona os segundos dados na lista #########################################
                
                if '@' in nome2:
                    
                    for m in range(c):
                        # el = df.iloc[i, m]
                        # lista.append(el)
                        el = df.iloc[j, m]
                        lista.append(el)
                
                elif 'vs' in nome2:          
                
                    for m in range(c):                        
                        el = df.iloc[j, m]
                        lista.append(el)
                        # lista.append(lista2[m])
                                                
                    for n in range(c):
                        lista.append(lista2[n]) 

###################################### Adiciona os dados na base final #########################################

                print("Convertendo jogo nº: ", cont3)
                df_final.loc[cont3] = lista
                cont3 = cont3 + 1
                lista.clear()
                lista2.clear()
                break

###################################### Salva base final #########################################

print("Jogos convertidos com sucesso")

df_final.to_csv('base_nba_final.csv')