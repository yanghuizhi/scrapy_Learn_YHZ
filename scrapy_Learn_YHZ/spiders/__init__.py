# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.


"""
要建立一个Spider，
必须用scrapy.Spider类创建一个子类，
并确定了三个强制的属性 和 一个方法。

name = ""
这个爬虫的识别名称，必须是唯一的，在不同的爬虫必须定义不同的名字。

allow_domains = []
是搜索的域名范围，也就是爬虫的约束区域，规定爬虫只爬取这个域名下的网页，不存在的URL会被忽略。

start_urls = ()
爬取的URL元祖/列表。爬虫从这里开始抓取数据，所以，第一次下载的数据将会从这些urls开始。其他子URL将会从这些起始URL中继承性生成。

parse(self, response)
    解析的方法，每个初始URL完成下载后将被调用，调用的时候传入从每一个URL传回的Response对象来作为唯一参数，
    主要作用如下：
    负责解析返回的网页数据(response.body)，提取结构化数据(生成item)
    生成需要下一页的URL请求。

"""

"""
import scrapy  # 必须有

class 类名(scrapy.Spider):  # 继承子类
    name = "爬虫的名字"
    allowed_domains = ["网址"]
    start_urls = (
        '链接',
    )

    def parse(self, response):
        pass
"""

