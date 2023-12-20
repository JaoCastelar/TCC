import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

elements = pd.read_csv('id.csv')
# elements = ['CdcbfwIf']

l, c = elements.shape

df = pd.DataFrame(columns=['Team', 'a.Team', 'Data', 'CasaAposta', 'Home', 'TitHome', 'Away', 'TitAway'])

cont = 0
line = []

for i in range(l):
    print(elements['ID'][i])
    url = 'https://www.flashscore.com.br/jogo/' + elements['ID'][i] +'/#/comparacao-de-odds/home-away/tr-incluindo-prol'
    
    option = Options()
    option.headless = True
    driver = webdriver.Chrome()

    driver.get(url)

    time.sleep(5)
    
    home = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[4]/div[2]/div[3]/div[2]/a')
    homeHtml = home.get_attribute('innerHTML')
    
    homeCont = BeautifulSoup(homeHtml, 'html.parser')
    
    away = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[4]/div[4]/div[3]/div[1]/a')
    awayHtml = away.get_attribute('innerHTML')
    
    awayCont = BeautifulSoup(awayHtml, 'html.parser')
    
    date = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[4]/div[1]/div');
    dateHtml = date.get_attribute('innerHTML');
    
    dateCont = BeautifulSoup(dateHtml, 'html.parser')
    
    
    time.sleep(10)
    
    
    # parent = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[8]/div[3]/div/div[2]')
    # parent = driver.find_element(By.XPATH, '//*[@id="detail"]/div[8]/div[3]/div/div[2]')
    # parent = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="detail"]/div[8]/div[3]/div/div[2]')))
    element = driver.find_elements(By.CLASS_NAME, 'ui-table__row')
    
    
    for j in range(len(element)):
        
        a = element[j].find_element(By.CLASS_NAME, 'prematchLink')
        aHtml = a.get_attribute('title')
        
        aCont = BeautifulSoup(aHtml, 'html.parser')
        
        odds = element[j].find_elements(By.CLASS_NAME, 'oddsCell__odd')
        
        odd1Html = odds[0].find_element(By.TAG_NAME, 'span')
        odd1v = odd1Html.get_attribute('innerHTML')
        odd1 = BeautifulSoup(odd1v, 'html.parser')
        
        odd2Html = odds[1].find_element(By.TAG_NAME, 'span')
        odd2v = odd2Html.get_attribute('innerHTML')
        odd2 = BeautifulSoup(odd2v, 'html.parser')
        
        
        
        line.append(homeCont)
        line.append(awayCont)
        line.append(dateCont)
        line.append(aCont)
        line.append(odd1)
        line.append(odd2)
        
        df.loc[cont] = line
        
        cont += 1
        line.clear()
        
        
df.to_csv('odds.csv', index=False)