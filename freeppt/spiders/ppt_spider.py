# -*- coding: utf-8 -*-
import scrapy
import json
from lxml import etree
import requests
from time import sleep
class PPTSpider(scrapy.Spider):
    name = "ppt_spider"
    allowed_domains = ["freeppt7.com/"]
    start_urls = ['https://www.freeppt7.com/']
    headers = {"authorization": "oauth c3cef7c66a1843f8b3a9e6a1e3160e20"}

    def parse(self,response):
        resp = requests.get(start_urls, headers=headers)
        print(resp)




if __name__ == "__main__":
    parse()