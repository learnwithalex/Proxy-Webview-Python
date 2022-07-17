# importing webdriver from selenium
from selenium import webdriver
from time import sleep

# Here Chrome will be used
driver = webdriver.Chrome("C:\\chromedriver.exe")

# URL of the website
url = "https://www.reddit.com/"

# Opening the URL
driver.get(url)

# Getting current URL source code
get_source = driver.page_source.encode('utf-8')


input1 = "reddit"
filename = 'webpages/'+input1+'.html'
file_ = open('webpages/'+input1+'.html', 'wb')
# Write the entire page content in result.html
file_.write(get_source)

# Closing the file
file_.close()
print(filename)

# Printing the URL


sleep(60)

driver.close()