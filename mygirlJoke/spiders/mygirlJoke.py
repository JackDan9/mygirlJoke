# -*- coding: utf-8 -*-

import scrapy
import smtplib
import datetime
from email.mime.text import MIMEText
from email.header import Header
from scrapy.http import Request

class MygirlJokeSpider(scrapy.Spider):
    name="mygirlJoke"
    start_urls = [
        "https://qiushibaike.com/hot"
    ]

    def parse(self, response):
        Sub_Selector = response.xpath(
            './/div[@class="article block untagged mb15 typs_hot" or @class="article block untagged mb15 typs_old" or @class="article block untagged mb15 typs_long"]')
        Joke_Laugh_Numbers = []
        Joke_Article_Links = []
        for sub in Sub_Selector:
            Joke_Laugh_Number = sub.xpath('.//div[@class="stats"]/span/i/text()').extract()[0]
            Joke_Article_Link_Content = sub.xpath('.//a[@class="contentHerf"]/@href').extract()[0]
            Joke_Article_Link = "https://www.qiushibaike.com" + Joke_Article_Link_Content
            Joke_Article_Links.append(Joke_Article_Link)
            Joke_Laugh_Numbers.append(int(Joke_Laugh_Number))
        New_Joke_Url = Joke_Article_Links[Joke_Laugh_Numbers.index(max(Joke_Laugh_Numbers))]
        # print(New_Joke_Url
        yield Request(
            url=New_Joke_Url,
            # url="https://www.qiushibaike.com/article/110329808",
            callback=self.parse_content
        )

    def parse_content(self, response):
        Laugh_Selector = response.xpath('.//div[@class="article block untagged noline mb15"]')
        Laugh_Content_List = Laugh_Selector.xpath('.//div[@class="content"]/text()').extract()
        if (Laugh_Selector.xpath('.//div[@class="thumb"]/img/@src')):
            Laugh_Img_Pic = Laugh_Selector.xpath('.//div[@class="thumb"]/img/@src').extract()[0]
            Laugh_Img = "https:" + str(Laugh_Img_Pic)

        for Laugh_Content_Single in Laugh_Content_List:
            Laugh_Content = ''.join(Laugh_Content_Single)
        today = datetime.datetime.today()
        anniversary = datetime.datetime(2018, 3, 14)
        loving_days = (today - anniversary).days
        if (Laugh_Selector.xpath('.//div[@class="thumb"]/img/@src')):
            lst = [
                '<html><body><h3>你好, 呆瓜:<br><br></h3>' + 
                '<h4>今天是' +  today.strftime('%Y-%m-%d') +':<br></h4>' + 
                '<h4>首先，今天已经是我们相恋的第' + str(loving_days) + '天了喔。然后大兵就要为你带来欢声笑语了！！</h4>' +
                '<h4>今日笑话内容:<br>' + Laugh_Content.encode('utf-8') + '<br></h4>' +
                '<img src=' + str(Laugh_Img) +'><br><br>' +
                '<h4>爱你呦！！！</h4>'
                '</body></html>']
        else:
            lst = ['<html><body><h3>你好, 呆瓜:<br><br></h3>' + 
                '<h4>今天是' +  today.strftime('%Y-%m-%d') +':<br></h4>' + 
                '<h4>首先，今天已经是我们相恋的第' + str(loving_days) + '天了喔。然后大兵就要为你带来欢声笑语了！！</h4>' +
                '<h4>今日笑话内容:<br>' + Laugh_Content.encode('utf-8') + '<br></h4>' +
                '<h4>爱你呦！！！</h4>'
                '</body></html>']

            # It is receiver email word.
            mailto_list = "*********@qq.com"
            mail_host = "smtp.qq.com"
            # It is your email word.
            mail_user = "********@qq.com"
            # It is your password
            mail_pass = "**********"

        content = ''.join(lst)
        msg = MIMEText(content, _subtype='html', _charset='utf-8')
        msg['From'] = mail_user
        msg['To'] = mailto_list
        msg['Subject'] = Header('大兵男朋友的笑话', 'utf-8')
        try:
            # s = smtplib.SMTP_SSL(mail_host, 465)
            s = smtplib.SMTP_SSL(mail_host, 465)
            s.login(mail_user, mail_pass)
            s.sendmail(mail_user, mailto_list, msg.as_string())
            s.close()
        except Exception as e:
            # traceback.print_exc()
            print(e)
