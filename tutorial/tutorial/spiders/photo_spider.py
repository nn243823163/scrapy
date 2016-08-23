# -*- coding: utf-8 -*-
import scrapy
import os
from ..items import TutorialItem

class PhotoSpiderSpider(scrapy.Spider):
    name = "photo_spider"
    # allowed_domains = ["dmoz.org"]
    allowed_domains = ["http://cl.anrqk.com"]
    start_urls = (
        'http://cl.anrqk.com/thread0806.php?fid=16&search=&page=1',
    )

    def start_requests(self):
        reqs = []
        for i in range(1, 5):
            req = scrapy.Request("http://cl.anrqk.com/thread0806.php?fid=16&search=&page=%s" % i)
            reqs.append(req)
        return reqs

    def parse(self, response):
        item = TutorialItem()
        urls = response.css("#ajaxtable > tbody:nth-child(2) > tr > td:nth-child(2) > h3 > a::attr(href)").extract()
        for url in urls:
            url = 'http://cl.anrqk.com/' + url
            item['url'] = url
            yield scrapy.Request(url=url, meta={'item':item},callback=self.parse_detail, dont_filter=True)

    def parse_detail(self, response):
        title = response.css(
            "#main > div:nth-child(4) > table > tr.tr1.do_not_catch > th:nth-child(2) > table > tr > td > h4::text").extract()
        title = ''.join(title)
        list = response.css(
            "#main > div:nth-child(4) > table > tr.tr1.do_not_catch > th:nth-child(2) > table  > tr > td > div.tpc_content.do_not_catch > input::attr(src)").extract()
        for result in list:
            item = response.meta['item']
            item['title'] = title
            item['link'] = result
            yield item
