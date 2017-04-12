import requests
from bs4 import BeautifulSoup

newurl = "http://news.sina.com.cn/o/2017-03-30/doc-ifycwunr8229709.shtml"
res = requests.get(newurl)
res.encoding = "utf-8"

html_news = res.text

soup = BeautifulSoup(res.text,"html.parser")
title = soup.select("#artibodyTitle")
time_test = soup.select("#navtimeSource")[0]
#souce_test = soup.select("#navtimeSource a")

article=[]
for p in soup.select('#artibody p')[:-1]:
    article.append(p.text.strip())
    ' '.join(article)
    
print(title[0].text)
print(time_test.contents[0].strip())
print(time_test.contents[1].text)

