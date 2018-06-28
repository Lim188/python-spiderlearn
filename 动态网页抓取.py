import json
import requests

def single_page_comment(link):
#link = 'https://api-zero.livere.com/v1/comments/list?callback=jQuery1124030126086598094437_1529672300768&limit=10&repSeq=3871836&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&_=1529672300770'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
    r = requests.get(link, headers=headers)
    #它是json数据
    #print(r.text)

    json_string = r.text
    json_string = json_string[json_string.find('{'):-2]     #仅仅提取字符串中符合json格式的部分

    #使用 json.loads 把字符串格式的响应体数据转化为json数据
    json_data = json.loads(json_string)
    #利用 json 数据的结构，提取到评论的列表comment_list
    comment_list = json_data['results']['parents']

    for eachone in comment_list:
        message = eachone['content']
        print(message)



# 截止测试时共69条评论
for page in range(1,7):
    link1 = 'https://api-zero.livere.com/v1/comments/list?callback=jQuery1124030126086598094437_1529672300768&limit=10&offset='
    link2 = '&repSeq=3871836&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&_=1529672300773'
    page_str = str(page)
    link = link1 + page_str + link2
    print(link)
    single_page_comment(link)