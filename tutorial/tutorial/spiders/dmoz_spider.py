# -*- coding: utf-8 -*-
import scrapy
import os
from ..items import TutorialItem

class DmozSpiderSpider(scrapy.Spider):
    name = "dmoz_spider"
    # allowed_domains = ["dmoz.org"]
    allowed_domains = ["cl.anrqk.com"]


    def start_requests(self):
        reqs = []
        start_urls = (
            'http://cl.anrqk.com/htm_data/16/1608/2030741.html',
            'http://cl.anrqk.com/htm_data/16/1608/2030683.html',
            'http://cl.cuxqv.com/htm_data/16/1608/2032318.html',
            'http://cl.cuxqv.com/htm_data/16/1608/2033702.html',
            'http://cl.anrqk.com/htm_data/16/1608/2021935.html',
        )
        for i in start_urls:
            req = scrapy.Request(i)
            reqs.append(req)
        return reqs

    def parse(self, response):
        # filename = response.url.split('/')[-1]
        # basdir = os.getcwd() + '/../doc/'
        # basdir = os.path.abspath('..') + '/doc/'
        # os.chdir(basdir)
        # with open( '/Users/doudou/Documents/python/scrapy/tutorial/tutorial/doc/' + filename,'wb') as fp:
        #     fp.write(response.body)
        #     fp.close()

        # tittle = response.xpath('/html/body[@id="main"]/div[3]/table/tr[1]/th[2]/table/tr/td/div[4]/input[1]/text()').extract()
        # item = TutorialItem()
        # item['tittle'] = tittle
        # response.xpath('//*[@id="main"]/div[3]/table/tbody/tr[1]/th[2]/table/tbody/tr/td/div[4]/input[1]')
        # response.xpath('//*[@id="main"]/div[3]/table/tbody/tr[1]/th[2]/table/tbody/tr/td/div[4]/input[2]')
        # response.css('div.t:nth-child(4) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > th:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(8) > input:nth-child(28)')
        items = []
        title = response.css("#main > div:nth-child(4) > table > tr.tr1.do_not_catch > th:nth-child(2) > table > tr > td > h4::text").extract()
        title = ''.join(title)
        list = response.css("#main > div:nth-child(4) > table >  tr.tr1.do_not_catch > th:nth-child(2) > table > tr > td > div.tpc_content.do_not_catch > input::attr(src)").extract()
        for result in list:
            item = TutorialItem()
            item['title'] = title
            item['link'] = result
            items.append(item)

        return items

