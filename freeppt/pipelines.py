# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline
class FreepptPipeline(ImagesPipeline):
    # def process_item(self, item, spider):
    #
    #     return item

    # def file_path(self, request, response=None, info=None):
    #     url = request.url
    #     file_name = url.split('/')[-1]
    #     return file_name
    #
    # def item_completed(self, results, item, info):
    #     image_paths = [x['path'] for ok, x in results if ok]
    #     if not image_paths:
    #         raise DropItem('Image Download Failed')
    #     return item
    def get_media_requests(self, item, info):
        for image_url in item['img_url']:
            yield Request(image_url)