# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
from scrapy.conf import settings
from scrapy import log

class MongoDBPipeline(object):

    def __init__(self):
        self.mongo_uri = settings['MONGO_URI']
        self.client = None
        self.board_db = None
        self.new_collection = None

    @classmethod
    def from_crawler(cls, crawler):
        return cls()

    def open_spider(self, spider):
        if self.client == None:
            self.client = MongoClient(self.mongo_uri)
            self.board_db = self.client[settings['MONGODB_TECHBOARD_DB']]
            if self.new_collection == None:
                self.new_collection = \
                self.board_db[settings['MONGODB_BOARD_NEWS_COLLECTION']]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        #avoid dupication
        if self.new_collection.find({"url": item["url"]}).count() > 0:
            log.msg("URL is already in the MongoDB database!",
                level=log.DEBUG, spider=spider)      
            return item

        if valid:
            self.new_collection.insert(dict(item))
            log.msg("news added to MongoDB database!",
                level=log.DEBUG, spider=spider)
        return item