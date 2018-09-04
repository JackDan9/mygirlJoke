# -*- coding: utf-8 -*-

'''
Name: mygirlJoke_english
Author: JackDan
Date: 2018-09-03 17:12
'''

import scrapy

import smtplib

import time
import datetime

import json
import random

import httplib
import urlparse

from email.mime.text import MIMEText
from email.header import Header
from scrapy.http import Request

import sys
reload(sys)
sys.setdefaultencoding('utf8')

class MygirlJokeSpider(scrapy.Spider):
    name="mygirlJoke"

    id_num = random.randint(4, 33)
    if (id_num == 6):
        page_number = random.randint(1, 7)
    elif (id_num ==  4):
        page_number = random.randint(1, 21)
    elif (id_num == 5):
        page_number = random.randint(1, 8)
    elif (id_num == 7):
        page_number = random.randint(1, 4)
    elif (id_num == 8):
        page_number = random.randint(1, 2)
    elif (id_num == 9):
        page_number = random.randint(1, 12)
    elif (id_num == 10):
        page_number = random.randint(1, 40)
    elif (id_num == 11):
        page_number = random.randint(1, 4)
    elif (id_num == 12):
        page_number = random.randint(1, 6)
    elif (id_num == 13):
        page_number = random.randint(1, 29)
    elif (id_num == 14):
        page_number = random.randint(1, 18)
    elif (id_num == 15):
        page_number = random.randint(1, 3)
    elif (id_num == 16):
        page_number = random.randint(1, 29)
    elif (id_num == 17):
        page_number = random.randint(1, 4)
    elif (id_num == 24):
        page_number = random.randint(1, 4)
    elif (id_num == 19):
        page_number = random.randint(1, 3)
    elif (id_num == 20):
        page_number = random.randint(1, 9)
    elif (id_num == 21):
        page_number = 1
    elif (id_num == 22):
        page_number = 1
    elif (id_num == 23):
        page_number = random.randint(1, 4)
    elif (id_num == 25):
        page_number = random.randint(1, 2)
    elif (id_num == 26):
        page_number = 1
    elif (id_num == 27):
        page_number = random.randint(1, 2)
    elif (id_num == 28):
        page_number = 1
    elif (id_num == 29):
        page_number = random.randint(1, 2)
    elif (id_num == 30):
        page_number = 1
    elif (id_num == 31):
        page_number = random.randint(1, 6)
    elif (id_num == 32):
        page_number = random.randint(1, 3)
    elif (id_num == 33):
        page_number = random.randint(1, 6)

    start_urls = [
        "http://news.iciba.com/appv3/wwwroot/ds.php?action=tags&id={}".format(id_num) + "&ob=1&order=2&page={}".format(page_number),
    ]

    def parse(self, response):
        '''
        Get the request new url
        :param response:
        :return:
        '''
        Sub_Selector_List = response.xpath('.//div[@id="content"]/div[@class="main fl"]/ul[@class="tagList clear"]/li')
        Li_List_Num = len(Sub_Selector_List)
        Li_Num = random.randint(1, Li_List_Num)
        Sub_Selector = response.xpath('.//div[@id="content"]/div[@class="main fl"]/ul[@class="tagList clear"]/li[' + str(Li_Num) + ']/div[1]/a/@href').extract()
        Sub_Selector_Link = ''.join(Sub_Selector)

        Id = Sub_Selector_Link[43:47]

        random_day = random.randint(1, 1000)
        time_now = (datetime.datetime.now() - datetime.timedelta(days = random_day))
        timestramp = int(time.mktime(time_now.timetuple()))
        timestramp_old = timestramp - 1000

        Sub_Selector_Link_Address = 'http://sentence.iciba.com/index.php?callback=jQuery19009826799941931723_' + str(timestramp_old) + '&c=dailysentence&m=getdetail&sid=' + Id + '&_=' + str(timestramp)

        yield Request(
            url=Sub_Selector_Link_Address,
            callback=self.parse_content
        )

    def parse_content(self, response):
        '''
        Get The Data Of Sub_Selector_Links
        :param response:
        :return:
        '''

        body = response.body

        len_before = 38
        len_after = len(body) - 1
        data_body = body[len_before:len_after]

        data_body_str = ''.join(data_body)
        data_body_json = json.loads(data_body_str)

        content = data_body_json["content"]
        note = data_body_json["note"]
        picture = data_body_json["picture"]

        host, path = urlparse.urlsplit(str(picture))[1:3]
        connection = httplib.HTTPConnection(host)
        connection.request("HEAD", path)
        response_object = connection.getresponse()
        if (response_object.status == 404):
            picture_url = 'http://b289.photo.store.qq.com/psb?/V10cP5hg0dYCOp/uOI7e77iET6v5HXPF2T0FDXnPnFOiDek91qWxZDd3aQ!/b/dCEBAAAAAAAA&bo=0AIABQAAAAARB.c!&rf=viewer_4'
        else:
            picture_url = picture
        mp3_url = data_body_json["tts"]

        today = datetime.datetime.today()
        anniversary = datetime.datetime(2018, 3, 14)
        loving_days = (today - anniversary).days
        loving_word = '爱你呦！！！'

        lst = [
            '<html><body>' +
            '<h3 style="font-family: cursive; font-weight: 500; font-size: 1，17em;">你好, 呆瓜:<br><br></h3>' +
            '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天是' + today.strftime('%Y-%m-%d') +
            ':<br></h4>' + '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">首先，今天已经是我们相恋的第' + str(
                loving_days) +
            '天了喔。然后大兵就要为你英语每日一句了！！</h4>' +
            '<img style="width: 620px;" src="' + str(picture_url) + '"><br>' +
            '<h4 style="font-family: PingFangSC-Medium, sans-serif; font-weight: 300; font-size: 1em;">今日每日一句内容:<br>' + content +
            '<br></h4><br>' +
            '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今日每日一句内容翻译:<br>' + note +
            '<br></h4><br>' +
            '<audio controls="controls" height="100" width="100"> <source src="' + str(mp3_url) +
            '" type="audio/mp3"/><embed height="100" width="100" src="' + str(mp3_url) +
            '"/></audio><br><br>' +
            '<h4 style="font-family: cursive; font-weight: 300; color: red; font-size: 1em;">' + loving_word + '</h4>' +
            '</body></html>']

        # It is receiver email word.
        mailto_list = "************@qq.com"
        mail_host = "smtp.qq.com"
        # It is your email word.z
        mail_user = "***********@qq.com"
        # It is your password
        mail_pass = "*************"

        content = ''.join(lst)
        msg = MIMEText(content, _subtype='html', _charset='utf-8')
        # print(content)
        msg['From'] = mail_user
        msg['To'] = mailto_list
        msg['Subject'] = Header('大兵男朋友的每日一句英语提供', 'utf-8')
        try:
            # s = smtplib.SMTP_SSL(mail_host, 465)
            s = smtplib.SMTP_SSL(mail_host, 465)
            s.login(mail_user, mail_pass)
            s.sendmail(mail_user, mailto_list, msg.as_string())
            s.close()
        except Exception as e:
            # traceback.print_exc()
            print(e)
