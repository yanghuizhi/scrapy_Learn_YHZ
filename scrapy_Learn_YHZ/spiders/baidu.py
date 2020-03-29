import scrapy


class First(scrapy.Spider):
    name = "baidu"
    allowed_domains = ["baidu.com"]
    start_urls = [
        "https://www.baidu.com"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        # with open(filename.text.txt, 'wb') as f:
        #     f.write(response.body)
        print(filename.text)
