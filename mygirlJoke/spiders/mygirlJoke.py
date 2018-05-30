# -*- coding: utf-8 -*-

import scrapy
from scrapy.http import Request
import os

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
            callback=self.parse_content
        )

    def parse_content(self, response):
        Laugh_Selector = response.xpath('.//div[@class="article block untagged noline mb15"]')
        Laugh_Content = Laugh_Selector.xpath('.//div[@class="content"]/text()').extract()[0]
        print(Laugh_Content)

