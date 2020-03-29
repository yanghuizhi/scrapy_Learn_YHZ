# -*- coding: utf-8 -*-
import scrapy


class MaitianSpider(scrapy.Spider):
    # 爬虫名字
    name = 'maitian'

    # 爬取的域名范围
    allowed_domains = ['maitian.cn']

    # 开始的url
    start_urls = ['http://bj.maitian.cn/zfall/R2C55']


    def parse(self, response):
        # 解析方法
        print(response.body)
