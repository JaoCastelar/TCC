import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


# url = "https://www.flashscore.com.br/basquete/eua/nba/#/4CS5kbsl/table/overall"
url = 'https://www.flashscore.com.br/basquete/eua/nba-2022-2023/resultados/'
    
option = Options()
option.headless = True
driver = webdriver.Chrome()

driver.get(url)

time.sleep(10)

botao = driver.find_element(By.XPATH, '//*[@id="live-table"]/div[1]/div/div/a')

driver.execute_script("arguments[0].scrollIntoView();", botao)

time.sleep(5)

botao.click()

time.sleep(5)

driver.execute_script("arguments[0].scrollIntoView();", botao)

time.sleep(5)

botao.click()

time.sleep(5)

parent = driver.find_element(By.XPATH, '//*[@id="live-table"]/div[1]/div/div')
element = parent.find_elements(By.CLASS_NAME, 'event__match--twoLine')

off = pd.DataFrame(columns=['Team', 'a.Team'])
j = 0
res = []

for i in range(len(element[:])):
    id = str(element[i].get_attribute('id'))
    of = id.split('_')
    
    path = str('//*[@id="'+id+'"]/div[1]')
    
    dataHtml = driver.find_element(By.XPATH, path)
    dataP = dataHtml.get_attribute('innerHTML')
    dataTxt = BeautifulSoup(dataP, 'html.parser')
    
    data = str(dataTxt).split(' ')
    
    dia = data[0].split('.')
    
    dataGameDia = '09'
    dataGameMes = '04'
    
    
    if (dia[0] <= dataGameDia) and (dia[1] <= dataGameMes) :
        print(dia, dataGameDia, dataGameMes)
        
        scoreHome = '//*[@id="'+id+'"]/div[4]'
        scoreAway = '//*[@id="'+id+'"]/div[5]'
        
        scoreHomeHtml = driver.find_element(By.XPATH, scoreHome)
        scoreAwayHtml = driver.find_element(By.XPATH, scoreAway)
        
        scorePH = scoreHomeHtml.get_attribute('innerHTML')
        scorePA = scoreAwayHtml.get_attribute('innerHTML')
        
        scoreHomeTxt = BeautifulSoup(scorePH, 'html.parser')
        scoreAwayTxt = BeautifulSoup(scorePA, 'html.parser')
        
        res.append(scoreHomeTxt)
        res.append(scoreAwayTxt)
        
        off.loc[j] = res
        
        j += 1
        
        res.clear()

    

print(off, len(off))

off.to_csv('res.csv', index=False)