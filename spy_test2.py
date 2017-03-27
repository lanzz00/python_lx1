import requests
from bs4 import BeautifulSoup

newurl = "http://news.sina.com.cn/w/sy/2017-03-27/doc-ifycstww1243172.shtml"
res = requests.get(newurl)
res.encoding = "utf-8"

html_news = res.text

soup = BeautifulSoup(res.text,"html.parser")
title = soup.select("#artibodyTitle")
print(title[0].text)