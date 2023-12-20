import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from lxml import etree

###################################### Abre o site da NBA #########################################

url = "https://www.nba.com/stats/teams/boxscores?SeasonType=Regular+Season"
    
option = Options()
option.headless = True
driver = webdriver.Chrome()

driver.get(url)

time.sleep(10)

###################################### Abre todos os elementos #########################################

driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[2]/div[1]/div[3]/div/label/div/select').click()

time.sleep(5)

driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[2]/div[1]/div[3]/div/label/div/select/option[1]').click()

time.sleep(5)

###################################### Pega o número de linhas da tabela #########################################

html = driver.page_source

soup2 = BeautifulSoup(html, 'html.parser')

dom = etree.HTML(str(soup2))

x = dom.xpath('//*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[2]/div[1]/div[1]/text()[1]')[0].split()[0]

x = int(x)

###################################### Recebe o html puro da tabela #########################################

element = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[3]/table')
html_content = element.get_attribute('outerHTML')

###################################### Converte html pra tabela #########################################

soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find(name='table')

###################################### Recebe e trata a tabela #########################################

df_full = pd.read_html( str(table) )[0].head(x)
# df = df_full[['Team', 'Match Up', 'Game Date', 'W/L', 'PTS', 'FGM', 'FGA', '3PM', '3PA', 'FTM', 'FTA', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', '+/-']]
# df.columns = ['Team', 'Match Up', 'Game Date', 'W/L', 'PTS', 'FGM', 'FGA', '3PM', '3PA', 'FTM', 'FTA', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', '+/-']
df = df_full[['Team', 'Match Up', 'Game Date', 'W/L', 'PTS', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'FTM', 'FTA', 'FT%', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', '+/-']]
df.columns = ['Team', 'Match Up', 'Game Date', 'W/L', 'PTS', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'FTM', 'FTA', 'FT%', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', '+/-']


print(df)

###################################### Exporta a tabela pra csv #########################################

df.to_csv('base_nba.csv')

time.sleep(10)


driver.quit()