import requests
from bs4 import BeautifulSoup

r = requests.get('https://news.naver.com/',headers={'User-Agent':'Mozilla/5.0'})
html_doc = r.text
bs = BeautifulSoup(html_doc,'html.parser')

print(bs.select('#today_main_news > div.hdline_news > ul > li:nth-child(1) > div.hdline_article_tit > a')[0].text)
print(bs.select('#today_main_news > div.hdline_news > ul > li:nth-child(2) > div.hdline_article_tit > a')[0].text)
print(bs.select('#today_main_news > div.hdline_news > ul > li:nth-child(3) > div.hdline_article_tit > a')[0].text)
print(bs.select('#today_main_news > div.hdline_news > ul > li:nth-child(4) > div.hdline_article_tit > a')[0].text)





