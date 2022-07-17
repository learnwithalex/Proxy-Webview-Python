# Importing important library
from selenium import webdriver
import os
from hashlib import md5
import sys
from urllib.parse import urlencode
from webdriver_manager.chrome import ChromeDriverManager

# using chrome browser
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)


input1 = input("Enter url to crawl: ")
# Target url
driver.get(
	input1)

page = driver.page_source.encode('utf-8')

# encode string

input1 = str(input1)
input1 = input1.encode()
input1 = hash(input1)
input1 = str(input1)
filename = 'webpages/'+input1+'.html'
file_ = open('webpages/'+input1+'.html', 'wb')
# Write the entire page content in result.html
file_.write(page)

# Closing the file
file_.close()
print(filename)
# Closing the driver
driver.close()
