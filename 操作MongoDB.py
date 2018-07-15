import requests
import datetime
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.blog_database
collection = db.blog

link = 'http://www.santostang.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
r = requests.get(link, headers=headers)

soup = BeautifulSoup(r.text, 'html.parser')
title_list = soup.find_all('h1', class_='post-title')
for eachone in title_list:
    url = eachone.a['href']
    title = eachone.a.text.strip()
    post = {'url': url,
            'title': title,
            'date': datetime.datetime.utcnow()

    }
    collection.insert_one(post)