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
#Open file
link_file = open("links.txt", 'a')

with link_file as lf:
    for items in link_list:
        lf.write('%s\n' %link_list)
    print("Sucess!")

lf.close()





    
    




    







driver.quit()
 






