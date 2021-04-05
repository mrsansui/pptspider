# -*- coding: utf-8 -*-
import scrapy
from freeppt.items import FreepptItem

class PPTSpider(scrapy.Spider):
    name = "ppt_spider"
    allowed_domains = ["freeppt7.com/"]
    start_urls = ['https://www.freeppt7.com/arts/']
    headers = {"authorization": "oauth c3cef7c66a1843f8b3a9e6a1e3160e20"}

    def parse(self,response):
        # all_links = response.xpath('//*[@id="post-5582"]/div/div/ul/li/div/a/@href')

        item = FreepptItem()
        item['a_link'] = response.xpath('//*[@id="content"]/div/article/div/a/@href').extract()
        item['b_title'] = response.xpath('//*[@id="content"]/div/article/div/h2/a/b/text()').extract()
        item['img_url'] = response.xpath('//*[@id="content"]/div/article/div/a/img/@src').extract()
        item['p_content'] = response.xpath('//*[@id="content"]/div/article/div/p/text()').extract()
        item['categories_url'] = response.xpath('//*[@id="menu-primarynavigationmenu"]/li/ul/li/a/@href').extract()
        print(len(item['categories_url']),'*'*20)

        yield item
        print(item['img_url'],'#'*10)
