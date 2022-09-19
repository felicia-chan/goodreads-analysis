from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas 
from bs4 import BeautifulSoup

PATH = "/Users/feliciachan/Documents/chrome_driver/chromedriver"

URL = "https://www.goodreads.com"

driver = webdriver.Chrome(executable_path=PATH)

driver.get(URL)

search = driver.find_element(By.ID, "sitesearch") # find where search box is located
search = driver.find_element(By.ID, "searchBox")
search = search.find_element(By.XPATH, '//input[@id="sitesearch_field"]')

search.send_keys("Harry Potter 1") # input search Harry Potter
search.send_keys(Keys.RETURN)

# close login sign

try:
    modal = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "modal__content"))
    )

    close_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='modal__content']//button[@class='gr-iconButton']"))
    ).click()

    print('SUCCESSFUL.')

except:
    print('Not found.')
    driver.close()

try:
    book_title = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='bookTitle']"))
    ).click()

    print('Successful')

except:
    print('Not found.')
    driver.close()


# try to open a single truncated review to reveal "show more", then loop over all reviews in page load, opening all
# future: open multiple pages in loop
# scrape reviews from each page

try:
    # reviews = WebDriverWait(driver, 10).until(
    #   EC.element_to_be_clickable((By.XPATH, "//div[@id='other_reviews']//div[@class='friendReviews elementListBrown']//div[@class='reviewText stacked']//a[@href='#']"))
    #).click()
    
    # reviews2 = driver.find_elements(By.XPATH, "//div[@id='other_reviews']//div[@class='friendReviews elementListBrown']//div[@class='reviewText stacked']//a[@href='#']").click()
    
    ## THIS IS PROBABLY UNNEEDED. YOU CAN GET THE TEXT WITHOUT CLICKING ON "...more" ##
    reviews = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "...more"))
    )
    reviews = driver.find_elements(By.LINK_TEXT, "...more")
    print(len(reviews))
    for review in reviews:
        review.click()

    print('version 1 website.')

except:

    pass


time.sleep(10)

# enter_site()

