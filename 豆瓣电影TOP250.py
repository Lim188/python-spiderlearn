import requests
from bs4 import BeautifulSoup

def get_movies():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
        'Host': 'movie.douban.com'
    }
    for i in range(0, 10):
        link = 'https://movie.douban.com/top250?start=' + str(i * 25)
        r = requests.get(link, headers=headers, timeout=10)
        print(str(i+1), '页响应状态码：', r.status_code)
        print(r.text)

# 得到网页的HTML代码
#
# get_movies()


movie_list = []
def get_movies():
    headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
            'Host': 'movie.douban.com'
        }


    for i in range(0, 10):
        link = 'https://movie.douban.com/top250?start=' + str(i * 25)
        r = requests.get(link, headers=headers, timeout=10)
        print(str(i+1), '页响应状态码：', r.status_code)

        soup = BeautifulSoup(r.text, 'lxml')
        div_list = soup.find_all('div', class_='hd')
        for each in div_list:
            movie = each.a.span.text.strip()
            movie_list.append(movie)

    return movie_list

movies = get_movies()
print(movie_list)

#进阶：获取TOP250电影的英文名、港台名、导演、主演、上映年份、电影分类、评分

