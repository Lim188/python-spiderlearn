import requests

#传递URL参数
r = requests.get('http://www.santostang.com/')
#返回一个名为 r 的 response对象

print('文本编码：', r.encoding)
print('响应状态码：', r.status_code)
print('字符串方式的响应体：', r.text)


key_dict = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get', params=key_dict)
print('URL 已正确编码：', r.url)
print('字符串方式的响应体：\n', r.text)


#定制请求头
headers = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
'Host':'www.santostang.com'
}

r = requests.get('http://www.santostang.com', headers=headers)
print('响应状态码：', r.status_code)



key_dict = {'key1': 'value1', 'key2': 'value2'}
r = requests.post('http://httpbin.org/post', data=key_dict)
print(r.text)
#from变量的值为key_dict输入的值，一个POST请求发送成功

link = 'http://www.santostang.com/'
r = requests.get(link, timeout=0.01)
#异常：时间限制0.01秒内，连接到地址为www.santostang.com的时间已到。