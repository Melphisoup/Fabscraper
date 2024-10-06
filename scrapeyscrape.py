from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import random




#Start the session
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

URL = "https://fabrary.net/decks?tab=latest"
driver.get(URL)
#Wait for the front page to load
time.sleep(10)
page_source = driver.page_source


#Find all the decks links
desired = driver.find_elements(By.XPATH, '//a[@href]')
des = driver.find_elements(By.CLASS_NAME, 'css-bveltq')
#Move links into a list. 
for d in des:
    deck_links = d.get_attribute('href')
    link_list = []
    link_list.append(deck_links)
#Randomize the links
random.shuffle(link_list)
#Print out the first link in the randomized list
print(link_list[0])
    
    




    







driver.quit()
 






