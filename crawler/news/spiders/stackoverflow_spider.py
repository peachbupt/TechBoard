from scrapy import Spider
from scrapy.selector import Selector
from news.items import BoardNewsItem

class StackOverflowSpider(Spider):
    name = "stackoverflow"
    allowed_domains = "stackoverflow.com"
    start_urls = ["http://stackoverflow.com/?tab=week"]

    def parse(self, response):
        questions = response.xpath('//div[@class="summary"]/h3')

        for question in questions:
            item = BoardNewsItem()
            item['title'] = question.xpath('a[@class="question-hyperlink"]/text()').extract()[0]
            item['url'] = "http://" + self.allowed_domains + question.xpath('a[@class="question-hyperlink"]/@href').extract()[0]
            yield item