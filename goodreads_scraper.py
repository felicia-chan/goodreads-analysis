from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas 
import requests
import re
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
    modal = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "modal__content"))
    )

    close_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='modal__content']//button[@class='gr-iconButton']"))
    ).click()

    print('searched harry potter 1 and closed modal.')

except:
    print('Not found.')
    driver.close()

try:
    book_title = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='bookTitle']"))
    ).click()

    print('clicked on harry potter 1')

except:
    print('Not found.')
    driver.close()


# try to open a single truncated review to reveal "show more", then loop over all reviews in page load, opening all
# future: open multiple pages in loop
# scrape reviews from each page

# try:
#     # reviews = WebDriverWait(driver, 10).until(
#     #   EC.element_to_be_clickable((By.XPATH, "//div[@id='other_reviews']//div[@class='friendReviews elementListBrown']//div[@class='reviewText stacked']//a[@href='#']"))
#     #).click()
    
#     # reviews2 = driver.find_elements(By.XPATH, "//div[@id='other_reviews']//div[@class='friendReviews elementListBrown']//div[@class='reviewText stacked']//a[@href='#']").click()
    
#     ## THIS IS PROBABLY UNNEEDED. YOU CAN GET THE TEXT WITHOUT CLICKING ON "...more" ##
#     reviews = WebDriverWait(driver, 5).until(
#         EC.presence_of_element_located((By.LINK_TEXT, "...more"))
#     )
#     reviews = driver.find_elements(By.LINK_TEXT, "...more")
#     print(len(reviews))
#     for review in reviews:
#         review.click()

#     print('version 1 website.')

# except:
#     print("THIS IS WRONG")
#     pass


# enter_site()


page = requests.get(driver.current_url)
soup = BeautifulSoup(page.content, "html.parser")
# print(driver.current_url)
# print(soup.prettify())

reviews = []
# reviews_selector = soup.find_all('div')

try:
    lazyloaded = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "lazyload-wrapper "))
    )
except:
    print("not found")

# need to scroll lazyload into view
pause_time = 0.5
i = 0
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(pause_time)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
    i += 1
    if i == 5:
        break


m = soup.find("div", attrs={"id":"ReviewsSection"})

time.sleep(1000)

# print(table.prettify())


# print(table.prettify())

# child = table.findChild("span", attrs={"class":"Formatted"})
# print(child)


# table2 = table.findChildren("div", attrs={"id":"reviewsSection"})
# print(table2)

# for row in table.findAll('span', attrs={"class": "Formatted"}):
#     review_list = {}
#     review_list['review'] = row.text
#     reviews.append(review_list)

# for row in table.findAll("div", attrs={''})

time.sleep(1000)
# table = soup.find('')

## to get a really good sentiment analysis, shouldn't i train on a certain amount of 5 star reviews, then 4 star, then 3...
# for sentiment analysis, correct? let's do this later...

# beta is slowly permanantly being rolled out on Goodreads, affects html