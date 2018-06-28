from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://www.santostang.com/2017/03/02/hello-world/')
# 使用brew安装chromedriver: brew cask install chromedriver



# 代码中的 JavaScript 解析成了一个 iframe, 所有的评论都装在这个框架之中
# 解析 iframe

# driver.switch_to.frame(driver.find_element_by_css_selector("iframe[title='livere']"))
# comment = driver.find_element_by_css_selector('div.reply-content')
# content = comment.find_element_by_tag_name('p')
# print (content.text)

driver.get("http://www.santostang.com/2017/03/02/hello-world/")
driver.switch_to.frame(driver.find_element_by_css_selector("iframe[title='livere']"))

comments = driver.find_elements_by_css_selector('div.reply-content')
for eachcomment in comments:
    content = eachcomment.find_element_by_tag_name('p')
    print (content.text)



