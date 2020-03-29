# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CountrySpider(CrawlSpider):
    """
    name：爬虫名称
    allowed_domains：可以爬取的域名列表，若不定义则可爬取任意域名
    start_urls：爬虫起始url列表
    rules：告知爬虫需要跟踪哪些链接
         callback 函数， 用于解析下载得到的响应
         parseitem() 从响应中获取数据的例子
    """
    name = 'country'
    allowed_domains = ['example.webscraping.com']
    start_urls = ['http://example.webscraping.com/']

    rules = (
        Rule(LinkExtractor(allow='/index/'), follow=True),
        Rule(LinkExtractor(allow='/index/'), callback='parse_item'),
    )

    def parse_item(self, response):
        item = {}
        name_css ='tr#places_country_row td.w2p_fw::text'
        item['name'] = response.css(name_css).extract()
        pop_css ='tr#places population__row td.w2p_fw::text'
        item['population'] = response.css (pop_css ) . extract ( )
        return item








