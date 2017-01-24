import re
import scrapy
from scrapy.utils.sitemap import Sitemap
from news.items import CitrixBlogItem

class CitrixSpider(scrapy.Spider):
    name = "citrix"
    start_urls = ["https://www.citrix.com/blogs/sitemap.xml"]

    def parse(self, response):
        s = Sitemap(response.body)
        for sitelink in s:
            print sitelink
            url = sitelink['loc']
            # for test only
            if url == 'https://www.citrix.com/blogs/sitemap-pt-post-2017-01.xml':
                yield scrapy.Request(url, callback = self.parse_by_month)

    def parse_by_month(self, response):
        s = Sitemap(response.body)
        for month_link in s:
            item = CitrixBlogItem()
            #print month_link
            item['url'] = month_link['loc']
            item['lastmod'] = month_link['lastmod']
            item['title'] = re.findall(\
                r'https://www.citrix.com/blogs/(\d+)/(\d+)/(\d+)/(.+?)/', \
                item['url'])[0][3]
            yield item