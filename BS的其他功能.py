from bs4 import BeautifulSoup

# 用soup对HTML代码进行美化显示
#print(soup.prettify())

html="""

<div class="qq_article">
<div class="hd">
<h1>法国VS克罗地亚前瞻：决战莫斯科！世界杯迎新霸主</h1>
<div class="qq_bar clearfix" bosszone="titleDown">
<div class="a_Info">
<span class="a_catalog" bosszone="ztTopic"><a target="_blank" accesskey="5" href="http://2018.qq.com/l/team/france/roll.htm" title="更多C组-法国相关内容列表">C组-法国</a></span><span class="a_source" bosszone="jgname"><a target="_blank" href="http://sports.qq.com/">腾讯体育</a></span><span class="a_time">2018-07-14 01:54</span>
</div>
<div class="a_share" id="shareBtn">
    <a class="shareTitle" style="cursor: pointer;">分享<i></i></a>
    <div class="shareBd">
        <ul class="shareBtn16">
            <li bosszone="msQzone" class=""><a href="javascript:void(0)" class="s_qzone" data-node="shareQzone">QQ空间</a></li>
            <li bosszone="msQQ" class=""><a href="javascript:void(0)" class="s_qq" data-node="shareQQ">QQ好友</a></li>
            <li bosszone="msSina"><a href="javascript:void(0)" class="s_sina" data-node="shareSina">新浪微博</a></li>
            <li bosszone="msWx" id="shareWx" class="shareWx">
                <a href="javascript:void(0)" class="s_wx">微信好友</a>
                <div class="ewmBox" id="upshareqrcode"></div>

"""
soup = BeautifulSoup(html, 'html.parser')
#print(soup.prettify())

soup.select('header.h1')
print(soup.select('header > h1'))
print(soup.select('div > a'))



