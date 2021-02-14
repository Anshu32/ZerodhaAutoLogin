import bs4, requests 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome('E:/documents/sem 5/chromedriver.exe')
timeout = 5

driver.get('https://kite.zerodha.com/')

username = driver.find_element_by_id('userid')
username.send_keys("Your username")

password = driver.find_element_by_id('password')
password.send_keys("Your password")

driver.implicitly_wait(200)

driver.find_element_by_tag_name('button').click()

try:
    element_present = EC.presence_of_element_located((By.ID, "pin"))
    WebDriverWait(driver,timeout).until(element_present)
except TimeOutException:
    print ("Timed out waiting for finding password type to load")

pin = driver.find_element_by_id('pin')
pin.send_keys("Your pin")

driver.implicitly_wait(200)

driver.find_element_by_tag_name('button').click()


try:
    element_present = EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/ul/li[2]"))
    WebDriverWait(driver,timeout).until(element_present)
except TimeOutException:
    print ("Timed out waiting for finding password type to load")


#optional
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/ul/li[2]").click() #  watchlist 2









