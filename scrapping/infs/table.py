import pandas as pd
import matplotlib.pyplot as plt
from selenium import webdriver

df_odds = pd.read_csv('C:/Users/Castelar/Desktop/Faculdade/TCC/Aplicação/scrapping/odds/odds.csv')
df_rede = pd.read_csv('C:/Users/Castelar/Desktop/Faculdade/TCC/Aplicação/scrapping/infs/rede_result.csv')

colunas = ['Confronto', 'RedeNBA', 'bet365', 'Betano.br', '1xbet', 'Betfair', 'Marsbet', 'Novibet', 'Parimatch']

df_table = pd.DataFrame(columns=colunas)

l, c = df_odds.shape
k = 0

line = []

for i in range(l):
    if i % 7 == 0:
        for j in range(i, i+7):
            if j == i:
                line.append(df_odds['Team'][j]+' x '+df_odds['a.Team'][j])
                if df_rede['Home'][k] > df_rede['Away'][k]:
                    line.append(df_odds['Team'][j])
                else: 
                    line.append(df_odds['a.Team'][j])
            if df_odds['Home'][j] < df_odds['Away'][j]:
                line.append(df_odds['Team'][j])
            else:
                line.append(df_odds['a.Team'][j])


        df_table.loc[k] = line
        k += 1
        line.clear()
        

table = df_table.to_html('table.html', index=False)

# print(table)

driver = webdriver.Chrome()  # Certifique-se de ter o chromedriver instalado

# Abrir o arquivo HTML no navegador
driver.get('C:/Users/Castelar/Desktop/Faculdade/TCC/Aplicação/scrapping/infs/table.html')

# Tirar um screenshot da tabela
driver.save_screenshot('tabela.png')

# Fechar o navegador
driver.quit()