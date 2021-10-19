import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox(executable_path=r'geckodriver.exe')

twitter_url = ('https://twitter.com/i/flow/login')

###Twitter Log In
driver.get(twitter_url)

#Username
driver.implicitly_wait(10)
twit_username = driver.find_element_by_class_name('r-30o5oe')
twit_username.send_keys('john.r.moss@okstate.edu' + Keys.ENTER)
#Suspicious
### Unncomment if Twitter Says susipicious activity
Username = driver.find_element_by_name('text').send_keys('JohnMos58788548' + Keys.ENTER)
#Password
Password = driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/label/div/div[2]/div/input').send_keys('Okstate21' + Keys.ENTER)


###Searching Twitter
search_crypto = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/label/div[2]/div/input').send_keys('#crypto' + Keys.ENTER)
#######################################################

clear_search = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/form/div[1]/div/div/label/div[2]/div/input').clear()
driver.implicitly_wait(10)
search_data = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/form/div[1]/div/div/label/div[2]/div/input').send_keys('#crytpocurrency' + Keys.ENTER)



#######################################################

clear_search = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/form/div[1]/div/div/label/div[2]/div/input').clear()
driver.implicitly_wait(10)
search_data = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/form/div[1]/div/div/label/div[2]/div/input').send_keys('@elonmusk' + Keys.ENTER)
#######################################################

clear_search = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/form/div[1]/div/div/label/div[2]/div/input').clear()
driver.implicitly_wait(10)
search_data = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/form/div[1]/div/div/label/div[2]/div/input').send_keys('@crypto' + Keys.ENTER)
#######################################################

clear_search = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/form/div[1]/div/div/label/div[2]/div/input').clear()
driver.implicitly_wait(10)
search_data = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/form/div[1]/div/div/label/div[2]/div/input').send_keys('@cryptocom' + Keys.ENTER)
#######################################################