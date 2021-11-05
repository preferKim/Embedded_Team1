import requests
r = requests.get('https://search.naver.com/search.naver?query=%EA%B5%AD%EB%A6%BD%EA%B3%B5%EC%9B%90&where=news&ie=utf8&sm=nws_hty')
html_doc = r.text
print(html_doc)
