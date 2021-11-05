import requests
from bs4 import BeautifulSoup
import time
r = requests.get('https://daum.net')
html_doc = r.text

soup = BeautifulSoup(html_doc, 'html.parser')

while True:
    print(soup.select('#news > div.news_prime.news_tab1 > div > ul > li:nth-child(1) > a')[0].text)
    print(soup.select('#news > div.news_prime.news_tab1 > div > ul > li:nth-child(2) > a')[0].text)
    print(soup.select('#news > div.news_prime.news_tab1 > div > ul > li:nth-child(3) > a')[0].text)
    print(soup.select('#news > div.news_prime.news_tab1 > div > ul > li:nth-child(4) > a')[0].text)
    print(soup.select('#news > div.news_prime.news_tab1 > div > ul > li:nth-child(5) > a')[0].text)
    time.sleep(60)