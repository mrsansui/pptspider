# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FreepptItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    a_link = scrapy.Field()
    b_title = scrapy.Field()
    # get all images url to the list
    img_url = scrapy.Field()
    # get all 'p' contents
    p_content = scrapy.Field()