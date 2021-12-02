#############################################
#=======     Crypto Price Scraper     ======#
#=======         Data Access          ======#
#======   MSIS 5193 - Group Project   ======#
#       Dobler, Miller, Moss & Salmon       #
#############################################

#=============Read in Libraries=============#
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#############################################
#====== Read in Crypto Currency data =======#
#  Using the library Selenium to scrape web #
#############################################
driver = webdriver.Firefox(executable_path=r'C:\Users\Baylee\Documents\Applications\geckodriver.exe')

##Define CoinMarketCap URL
coinmarket_url = 'https://coinmarketcap.com/'
driver.get(coinmarket_url)

##Find Search Bar Element using Selector
search = driver.find_element_by_css_selector('div.sc-1xvlii-0:nth-child(2)>svg:nth-child(1)').click() #Open Search Bar
search_text = driver.find_element_by_css_selector('.bzyaeu-3')
search_text.send_keys('Doge' + Keys.ENTER) ##search DogeCoin

##Find Historical Data Tab & Click
historic = driver.find_element_by_css_selector('a.x0o17e-0:nth-child(3)').click()
##Load crypto values until 12/30/2018
load = driver.find_element_by_css_selector('.b4d71h-0>p:nth-child(3)>button:nth-child(1)').click()
#===== Scrape Crypto Data Values =====#
##Date
crypto_date_elem = driver.find_elements_by_css_selector('table.h7vnx2-2>tbody>tr>td:nth-child(1)')
crypto_date = []
for i in crypto_date_elem:
    crypto_date.append(i.text)
crypto_date
##Starting Price
starting_price_elem = driver.find_elements_by_css_selector('table.h7vnx2-2>tbody>tr>td:nth-child(2)')
starting_price = []
for i in starting_price_elem:
    starting_price.append(i.text)
starting_price
##Closing Price 
closing_price_elem = driver.find_elements_by_css_selector('table.h7vnx2-2>tbody>tr>td:nth-child(3)')
closing_price = []
for i in closing_price_elem:
    closing_price.append(i.text)
closing_price
##High Price
high_price_elem = driver.find_elements_by_css_selector('table.h7vnx2-2>tbody>tr>td:nth-child(4)')
high_price = []
for i in high_price_elem:
    high_price.append(i.text)
high_price
##Low Price
low_price_elem = driver.find_elements_by_css_selector('table.h7vnx2-2>tbody>tr>td:nth-child(5)')
low_price = []
for i in low_price_elem:
    low_price.append(i.text)
low_price
##Volume
volume_elem = driver.find_elements_by_css_selector('table.h7vnx2-2>tbody>tr>td:nth-child(6)')
volume = []
for i in volume_elem:
    volume.append(i.text)
volume
##Market Cap
market_cap_elem = driver.find_elements_by_css_selector('table.h7vnx2-2>tbody>tr>td:nth-child(7)')
market_cap = []
for i in market_cap_elem:
    market_cap.append(i.text)
market_cap
##Add columns with values to a dataframe
temp_doge = {'crypto_date':crypto_date,'starting_price':starting_price,'closing_price':closing_price, 'high_price':high_price,'low_price':low_price,'volume':volume,'market_cap':market_cap}
doge = pd.DataFrame(temp_doge)
##Add column to data frame with crypto name for each row
doge.insert(0, 'crypto', 'Dogecoin')
##Print Created Data Frame
doge
## ======= Repeat for Bitcoin ====== #
##Find Search Bar Element using Selector
search = driver.find_element_by_css_selector('div.sc-1xvlii-0:nth-child(2)>svg:nth-child(1)').click() #Open Search Bar
search_text = driver.find_element_by_css_selector('.bzyaeu-3')
search_text.send_keys('BTC' + Keys.ENTER) ##search Bitcoin

##Find Historical Data Tab & Click
historic = driver.find_element_by_css_selector('a.x0o17e-0:nth-child(3)').click()
##Load crypto values until 12/30/2018
load = driver.find_element_by_css_selector('.b4d71h-0>p:nth-child(3)>button:nth-child(1)').click()
#===== Scrape Crypto Data Values =====#
##Date
crypto_date_elem = driver.find_elements_by_css_selector('table.h7vnx2-2>tbody>tr>td:nth-child(1)')
crypto_date = []
for i in crypto_date_elem:
    crypto_date.append(i.text)
crypto_date
##Starting Price
starting_price_elem = driver.find_elements_by_css_selector('table.h7vnx2-2>tbody>tr>td:nth-child(2)')
starting_price = []
for i in starting_price_elem:
    starting_price.append(i.text)
starting_price
##Closing Price 
closing_price_elem = driver.find_elements_by_css_selector('table.h7vnx2-2>tbody>tr>td:nth-child(3)')
closing_price = []
for i in closing_price_elem:
    closing_price.append(i.text)
closing_price
##High Price
high_price_elem = driver.find_elements_by_css_selector('table.h7vnx2-2>tbody>tr>td:nth-child(4)')
high_price = []
for i in high_price_elem:
    high_price.append(i.text)
high_price
##Low Price
low_price_elem = driver.find_elements_by_css_selector('table.h7vnx2-2>tbody>tr>td:nth-child(5)')
low_price = []
for i in low_price_elem:
    low_price.append(i.text)
low_price
##Volume
volume_elem = driver.find_elements_by_css_selector('table.h7vnx2-2>tbody>tr>td:nth-child(6)')
volume = []
for i in volume_elem:
    volume.append(i.text)
volume
##Market Cap
market_cap_elem = driver.find_elements_by_css_selector('table.h7vnx2-2>tbody>tr>td:nth-child(7)')
market_cap = []
for i in market_cap_elem:
    market_cap.append(i.text)
market_cap
##Quit driver
driver.quit()
##Add columns with values to a dataframe
temp_bit = {'crypto_date':crypto_date,'starting_price':starting_price,'closing_price':closing_price, 'high_price':high_price,'low_price':low_price,'volume':volume,'market_cap':market_cap}
bit = pd.DataFrame(temp_bit)
##Add column to data frame with crypto name for each row
bit.insert(0, 'crypto', 'Bitcoin')
##Print Created Data Frame
bit
#===== Create Crypto Currency DataFrame ====#
##Merge Bitcoin and DogeCoin Data Frames
crypto_data = pd.concat([doge, bit])
crypto_data

##Export to CSV
crypto_data.to_csv('crypto_data_11.30.csv')