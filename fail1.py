import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import requests
from bs4 import BeautifulSoup as BS
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()

driver = webdriver.Chrome('chromedriver.exe',options=options)

target_link = "https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl"
text= driver.get(target_link)
print(text.pifind_elements(By.CSS_SELECTOR,'#dismissible'))

# titles = driver.find_elements(By.CSS_SELECTOR, "#dismissible")

# for title in titles:
#     main_title=title.find_elements(By.CSS_SELECTOR, "#video-title").get_property("title")
#     print(main_title)
