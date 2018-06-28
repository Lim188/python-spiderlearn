#!/usr/bin/python
#coding:UTF-8

import requests
from bs4 import BeautifulSoup

link = 'http://www.santostang.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}    #用request的headers伪装成浏览器访问
r = requests.get(link, headers=headers) # r是requests的Response回复对象
#print(r.text)
# 获取了博客首页的HTML代码

# 把HTML代码转化为soup对象
soup = BeautifulSoup(r.text, 'lxml')    #使用BeautifulSoup解析这段代码
title = soup.find('h1', class_='post-title').a.text.strip()
print(title)
# 从整个网页中提取第一篇文章的标题

with open('title.txt', 'a+') as f:
    f.write(title)
    f.close()
