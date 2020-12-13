from selenium import webdriver
from selenium.common.exceptions import *

webdriver_path = '/Users/chokniran/Downloads/chromedriver' # Enter the file directory of the Chromedriver
Lazada_url = 'https://www.lazada.co.th'
search_item = 'ipadmini5' # Chose this because I often search for coffee!

# Select custom Chrome options
options = webdriver.ChromeOptions()
options.add_argument('--headless') 
options.add_argument('start-maximized') 
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')

# Open the Chrome browser
browser = webdriver.Chrome(webdriver_path, options=options)
browser.get(Lazada_url)

search_bar = browser.find_element_by_id('q')
search_bar.send_keys(search_item)
search_bar.submit()

item_titles = browser.find_elements_by_class_name('c16H9d')
item_prices = browser.find_elements_by_class_name('c13VH6')

# Initialize empty lists
titles_list = []
prices_list = []
# Loop over the item_titles and item_prices
for title in item_titles:
    titles_list.append(title.text)
    
for price in item_prices:
    prices_list.append(price.text)

print(titles_list)
print(prices_list)

