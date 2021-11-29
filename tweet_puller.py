from os import write
import pandas as pd
import numpy as np
from time import sleep
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common import exceptions

def create_webdriver_instance():
    options = EdgeOptions()
    options.use_chromium = True
    driver = Edge(options=options)
    return driver
    
def login_to_twitter(username, password, driver):
    url = 'twitter.com/login'
    try:
        driver.get(url)
        xpath_username = '//input[@name="session[username_or_email]"]'
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, xpath_username)))
        uid_input = driver.find_element_by_xpath(xpath_username)
        uid_input.send_keys(username)
    except exceptions.TimeoutException:
        print("Timeout while waiting for Login screen")
        return False

    pwd_input = driver.find_element_by_xpath('//input[@name="session[password]"]')
    pwd_input.send_keys(password)
    try:
        pwd_input.send_keys(Keys.RETURN)
        url = "https://twitter.com/home"
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(url))
    except exceptions.TimeoutException:
        print("Timeout while waiting for home screen")
    return True
###Find search and input term
def find_search_input_criteria(search_term, driver):
     xpath_search = ''
     search_input = driver.find_element_by_xpath(xpath_search)
     search_input.send_keys(search_term)
     search_input.send_keys(Keys.RETURN)
     return True

def change_page_sort(tab_name, driver):
    """Options for this program are 'Latest' and 'Top'"""
    tab=driver.find_element_by_llink('inserttab name')
    tab.click()
    xpath_tab_state = f''
    
def generate_tweet_id(tweet):
    return ''.join(tweet)

def scroll_down_page(driver, last_position, num_seconds_to_load=.5, scroll_attempt=0, max_attempts=5):
    end_of_scroll_region=False
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(num_seconds_to_load)
    curr_position = driver.execute_script("return window.pageYOffset;")
    if curr_position == last_position:
        if scroll_attempt < max_attempts:
            end_of_scroll_region = True
        else:
            scroll_down_page(last_position,curr_position,scroll_attempt + 1)
    last_position=curr_position
    return last_position, end_of_scroll_region

def save_tweet_data_to_csv(records, filepath, mode='a+'):
    header = ['User', 'Handle', 'PostDate', 'TweetText', 'ReplyCount', 'RetweetCount', 'LikeCount']
    with open(filepath, mode=mode, newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if mode == 'w':
            writer.writerow(header)
        if records:
            writer.writerow(records)

def collect_all_tweets_from_current_view(driver, lookback_limit=15):
    page_cards = driver.find_elements_by_xpath()
    if len(page_cards) <= lookback_limit:
        return page_cards
    else:
        return page_cards[-lookback_limit:]

def extract_data_from_current_tweet_card(card):
    try:
        user = card.find_element_by_xpath('').text
    except exceptions.NoSuchElementException:
        user = ""
    except exceptions.StaleElementReferenceException:
        return
    try:
        handle = card.find_element_by_xpath('').text
    except exceptions.NoSuchElementException:
        handle=""
    try:
        postdate = card.find_element_by_xpath('').get_attribute('datetime')
    except exceptions.NoSuchElementException:
        return
    try:
        _comment = card.find_element_by_xpath('').text
    except exceptions.NoSuchElementException:
        _comment = ""
    try:
         _responding = card.find_element_by_xpath('.//div[2]/div[2]/div[2]').text
    except exceptions.NoSuchElementException:
        _responding = ""
    tweet_text = _comment + _responding
    try:
        reply_count = card.find_element_by_xpath('.//div[@data-testid="reply"]').text
    except exceptions.NoSuchElementException:
        reply_count = ""
    try:
        retweet_count = card.find_element_by_xpath('.//div[@data-testid="retweet"]').text
    except exceptions.NoSuchElementException:
        retweet_count = ""
    try:
        like_count = card.find_element_by_xpath('.//div[@data-testid="like"]').text
    except exceptions.NoSuchElementException:
        like_count = ""

    tweet = (user, handle, postdate, tweet_text, reply_count, retweet_count, like_count)
    return tweet 

