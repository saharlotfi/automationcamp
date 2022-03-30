from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("http://www.yahoo.com")
driver.find_element('name','q').send_keys("hgjhsgdjhg")
sleep(2)
