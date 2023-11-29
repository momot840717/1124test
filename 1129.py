from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<p>Hello world</p>'

from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


import requests
from bs4 import BeautifulSoup

@app.route('/news/<name>')
def news(name=None):
    try:
        url = f'https://tw.stock.yahoo.com/quote/{name}.TW'
        # headers = {
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
        # }
        html_doc = requests.get(url)
        if html_doc.status_code != 200:
            return '<p>Error Market Stock Code.</p>'
        soup = BeautifulSoup(html_doc.text, 'html.parser')
        all_a = soup.find_all('h3', {'class':"Mt(0) Mb(8px)"})
        news_collect = []
        for element in all_a:
            news_collect.append(
                {
                    'title':  element.a.contents[1],
                    'link': element.a.get('href')
                }
            )
        return render_template('news.html', news_list=news_collect)
    except:
        return '<p>Error Market Stock Code.</p>'