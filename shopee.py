from selenium import webdriver
from selenium.common.exceptions import *

webdriver_path = '/Users/chokniran/Downloads/chromedriver' # Enter the file directory of the Chromedriver
shopee_url = 'https://shopee.co.th'
search_item = 'ipadmini5' # Chose this because I often search for coffee!

# Select custom Chrome options
options = webdriver.ChromeOptions()
options.add_argument('--headless') 
options.add_argument('start-maximized') 
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')

# Open the Chrome browser
browser = webdriver.Chrome(webdriver_path, options=options)
browser.get(shopee_url)

#search_bar = browser.find_element_by_id('q')
#search_bar.send_keys(search_item)
#search_bar.submit()

item_titles = browser.find_elements_by_class_name('_1UIe83')
item_prices = browser.find_elements_by_class_name('_341bF0')

# Initialize empty lists
titles_list = []
prices_list = []
# Loop over the item_titles and item_prices
for title in item_titles:
    print(title.text)
    #print(titles_list) 
    #titles_list.append(title.text)
    




