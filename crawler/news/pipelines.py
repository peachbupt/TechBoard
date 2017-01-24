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
        self.hackernews_collection = None
        self.citrix_collection = None

    @classmethod
    def from_crawler(cls, crawler):
        return cls()

    def open_spider(self, spider):
        if self.client == None:
            self.client = MongoClient(self.mongo_uri)
            self.board_db = self.client[settings['MONGODB_TECHBOARD_DB']]
        if spider.name == "hackernews":
            self.hackernews_collection = self.board_db[settings['MONGODB_HACK_NEWS_COLLECTION']]
        elif spider.name == "citrix":
            self.citrix_collection = self.board_db[settings['MONGODB_CITRIX_BLOG_COLLECTION']]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        valid = True
        if spider.name == "hackernews":
            for data in item:
                if not data:
                    valid = False
                    raise DropItem("Missing {0}!".format(data))
            if valid:
                self.hackernews_collection.insert(dict(item))
                log.msg("news added to MongoDB database!",
                    level=log.DEBUG, spider=spider)
        elif spider.name == "citrix":
            for data in item:
                if not data:
                    valid = False
                    raise DropItem("Missing {0}!".format(data))
            if valid:
                self.citrix_collection.insert(dict(item))
                log.msg("blog added to MongoDB database!",
                    level=log.DEBUG, spider=spider)
        return item