from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas
from bs4 import BeautifulSoup

# needed to move exe location to PATH first
 
PATH = "/Users/feliciachan/Documents/chrome_driver/chromedriver"

driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")
print(driver.title)

# find_element_by_name has deprecated, use find_element("name", "thing")
search = driver.find_element("name", "s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

# potential error: since it takes a bit to search "test",
# we could start looking for "main" before we reach the
# correct page.

try: # waits ten seconds for main id element to be located
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )

    articles = main.find_elements(By.TAG_NAME, "article")
    for article in articles:
        header = article.find_element(By.CLASS_NAME, "entry-summary")
        print(header.text)

except: # if main not found in 10 seconds, quits
    driver.quit()

# main = driver.find_element("id", "main")



