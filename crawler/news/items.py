# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class NewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class HackerNewsItem(scrapy.Item):
    title = Field()
    url = Field()
    points = Field()
    comments = Field()
    comments_url = Field()
    user_name = Field()
    since = Field()
