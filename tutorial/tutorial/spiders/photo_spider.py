# -*- coding: utf-8 -*-
import scrapy
import os
from ..items import TutorialItem

class PhotoSpiderSpider(scrapy.Spider):
    name = "photo_spider"
    # allowed_domains = ["dmoz.org"]
    allowed_domains = ["http://cl.anrqk.com"]
    start_urls = (
        'http://cl.lbawk.com/thread0806.php?fid=16&search=&page=2',
    )

    def start_requests(self):
        reqs = []
        for i in range(1,3 ):
            req = scrapy.Request("http://cl.lbawk.com/thread0806.php?fid=16&search=&page=%s" % i)
            reqs.append(req)
        return reqs

    def parse(self, response):
        urls = response.css("#ajaxtable > tbody:nth-child(2) > tr > td:nth-child(2) > h3 > a::attr(href)").extract()
        for url in urls:
            url = 'http://cl.anrqk.com/' + url
            yield scrapy.Request(url=url, callback=self.parse_detail, dont_filter=True)

    def parse_detail(self, response):
        item = TutorialItem()
        title = response.css("#main > div:nth-child(4) > table > tr.tr1.do_not_catch > th:nth-child(2) > table > tr > td > h4::text").extract()
        title = ''.join(title)
        list = response.css("#main > div:nth-child(4) > table > tr.tr1.do_not_catch > th:nth-child(2) > table  > tr > td > div.tpc_content.do_not_catch > input::attr(src)").extract()
        data = response.css("#main > div:nth-child(4) > table > tr:nth-child(2) > th > div.tipad::text").re(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}")
        for result in list:
            item['url'] = response.url
            item['title'] = title
            item['link'] = result
            item['data'] = data
            yield item
