# -*- coding: utf-8 -*-
import scrapy
import os
from ..items import TutorialItem

class JiandanSpider(scrapy.Spider):
    name = "jiandan_spider"
    # allowed_domains = ["dmoz.org"]
    allowed_domains = ["jandan.net"]
    start_urls = (
        'http://jandan.net/ooxx/page-2094',
    )

    def parse(self, response):
        # tittle = response.css("#main > div:nth-child(4) > table > tr.tr1.do_not_catch > th:nth-child(2) > table > tr > td > h4::text").extract()
        list = response.css("#comments > ol > li > div:nth-child(1) > div > div.text > p > img::attr(src)").extract()
        for result in list:
            item = TutorialItem()
            item['tittle'] = u'煎蛋'
            item['link'] = result
            yield item