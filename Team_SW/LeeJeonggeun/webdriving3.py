#!/sur/bin/evn python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyvirtualdisplay import Display
import time

#This code is only for www.daum.net
ID = ''
PW = ''

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('-headless')
chrome_options.add_argument('-no-sandbox')
chrome_options.add_argument('-single-process')
chrome_options.add_argument('-disable-dev-shm-usage')
path='/usr/lib/chromium-browser/chromedriver'

print('starting')
display = Display(visible=0, size=(1600,1200))
display.start()
driver = webdriver.Chrome(path, chrome_options=chrome_options)
print('webdriver loaded')

#Navigate to target website
driver.get('https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F')

element = WebDriverWait(driver,200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="id"]')))

driver.find_element_by_xpath('//*[@id="id"]').send_keys(ID)
driver.find_element_by_xpath('//*[@id="inputPwd"]').send_keys(PW)
driver.find_element_by_xpath('//*[@id="loginBtn"]').click()

element = WebDriverWait(driver,200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mArticle"]/div[1]/div[2]/ul/li[1]/a')))
driver.find_element_by_xpath('//*[@id="mArticle"]/div[1]/div[2]/ul/li[1]/a').click()

element = WebDriverWait(driver,200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mailList"]/div[1]/div/ul/li[1]/div[3]/a[1]/strong')))
mail_subject = driver.find_element_by_xpath('//*[@id="mailList"]/div[1]/div/ul/li[1]/div[3]/a[1]/strong').text
print(mail_subject)
print('target page loaded and mail subject captured')
print('Done')
