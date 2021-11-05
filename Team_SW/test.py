import requests
from bs4 import BeautifulSoup


r = requests.get('https://news.daum.net/')

html_doc = r.content
#print(html_doc)

soup = BeautifulSoup(html_doc, 'html.parser')

news_tit = soup.find_all("a", {"data-tiara-layer":"article"})

for i in range(len(news_tit)):
  print(i+1, news_tit[i].text)