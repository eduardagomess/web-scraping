import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json

url = "https://stats.nba.com/players/traditional/?PerMode=Totals&Season=2019-20&SeasonType=Regular%20Season&sort=PTS&dir=-1"

option = Options()
option.headless = True
driver = webdriver.Chrome()
driver.get(url)
time.sleep(10)
driver.find_element_by_xpath("//div[@class='nba-stat-table']//table//thead//tr//th[@data-field='PTS']").click()

element = driver.find_element_by_xpath("//div[@class='nba-stat-table']//table")
htmlContent = element.get_attribute("outerHTML")

soup = BeautifulSoup(htmlContent, 'html.parser')
table = soup.find(name="table")

dataFrameFull= pd.read_html(str(table))[0].head(10)
df = dataFrameFull[['Unnamed: 0', 'PLAYER', 'TEAM', 'PTS']]
df.columns = ['pos', 'player', 'team', 'total']

ranking = {}
ranking["points"] = df.to_dict('records')
js = json.dumps(ranking)
jsonFile = open("ranking.json", "w")
jsonFile.write(js)
jsonFile.close()

driver.quit()
