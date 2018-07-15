import requests
from bs4 import BeautifulSoup

link = 'http://www.santostang.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
r = requests.get(link, headers=headers)
# 将网页响应体的字符串转换为soup对象
soup = BeautifulSoup(r.text, 'html.parser')
first_title = soup.find('h1', class_='post-title').a.text.strip()
print('第一篇文章的标题是：', first_title)

title_list = soup.find_all('h1', class_='post-title')

for i in range(len(title_list)):
    title = title_list[i].a.text.strip()

    print('第 %s 篇文章的标题是： %s' % (i+1, title))


