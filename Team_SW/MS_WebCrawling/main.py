import requests
from bs4 import BeautifulSoup
from news_scrap import daum_news, daum_sports_ws, naver_weather


daum_news()
daum_sports_ws()
naver_weather()