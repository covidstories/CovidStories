import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
PATH = "/Users/manushanbhog/chromedriver"
driver = webdriver.Chrome(PATH)


#Enter any link below to get a story. The link below works as well.


link = "https://medicine.iu.edu/blogs/student-life/i-am-not-invincible-my-covid-19-story"
driver.get(link)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main-content"))
    )
    text_file = open("covidstories.txt", "w")
    n = text_file.write(main.text)
    text_file.close()





finally:
    driver.quit()

#the story is saved in the file named below.


link_file = open("link_file.txt", "w")
n = link_file.write(link)
link_file.close






