"""
建立虛擬環境
python -m venv 虛擬環境名稱
"""
from bs4 import BeautifulSoup
import requests
import time
import json
from pprint import pprint 

# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>

# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>

# <p class="story">...</p>
# """

url = 'https://tw.stock.yahoo.com/quote/3006.TW'
now = time.time()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
}
html_doc = requests.get(url).text
# print(html_doc)
# with open('3006html.txt', encoding='utf8', mode='w+') as f:
#     f.write(html_doc)


soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.h3)
all_a = soup.find_all('h3', {'class':"Mt(0) Mb(8px)"})
# print(all_a)
news_collect = []
for element in all_a:
    news_collect.append(
        {
            'title':  element.a.contents[1],
            'link': element.a.get('href')
        }
    )
print(news_collect)
print(time.time()-now)
# print(soup.find(id="link3"))
# print(soup.a.get('href'))
# print(soup.p)
# print(soup.p['class'])