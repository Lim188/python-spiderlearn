#coding=UTF-8
import MySQLdb
import requests
from bs4 import BeautifulSoup

# connect() 方法用于创建数据库的连接，里面可以指定参数：用户名，密码，主机等信息
#这只是连接到了数据库，要想操作数据库需要创建游标
conn = MySQLdb.connect(host='localhost', user='root', passwd='your_password', db='MyScraping', charset='utf8')
# 通过获取到的数据库连接conn下的cursor()方法来创建游标。
cur=conn.cursor()

link = 'http://www.santostang.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
r = requests.get(link, headers=headers)

soup = BeautifulSoup(r.text, 'html.parser')
title_list = soup.find_all('h1', class_='post-title')
for eachone in title_list:
    url = eachone.a['href']
    title = eachone.a.text.strip()
    # 创建数据表,通过游标cur 操作execute()方法可以写入纯sql语句。通过execute()方法中写如sql语句来对数据进行操作
    cur.execute('INSERT INTO urls (url, content) VALUES (%s, %s)', (url, title))

cur.close()
conn.commit()
conn.close()