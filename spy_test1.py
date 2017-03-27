import requests
from bs4 import BeautifulSoup
newurl = "http://news.sina.com.cn/society/"
res = requests.get(newurl)
res.encoding = "utf-8"
html_sample = res.text
soup = BeautifulSoup(html_sample,'html.parser')
alink = soup.select('a')
'''
for link in alink:
    print(link['href'])
'''
slect_text = soup.select('#slt_01')
for option1 in slect_text:
    print(option1['option'])
    
#print(soup.text)
#print(res.text)
