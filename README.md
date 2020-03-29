# Scrapy Learn
```
项目名
  |-- 项目名
     |-- __init__.py
     |-- items.py           # 目标文件
     |-- middlewares.py     # Middlewares 中间件
     |-- pipelines.py       # 管道文件，可用于后续存储
     |-- settings.py        # 配置文件 
     |-- spiders            # 爬取主程序文件夹
        |-- __init_.py  
  |-- scrapy.cfg            # Scrapy 部署时的配置文件
```

```
scrapy startproject [name]  # 创建项目

genspider  # 快速生成爬虫模版
    scrapy genspider country example.webscraping.com --template=crawl
                      爬虫名、 域名以及可选的模板参数，就可以生成初始模板 。

crawl  # 运行爬虫
    scrapy crawl country -s LOG_LEVEL=ERROR
                 爬虫名    参数
    scrapy crawl country --output=countries.csv -s LOG_LEVEL=INFO
                         自动保存方法
     scrapy crawl country -s LOG_LEVEL=DEBUG -s JOBDIR=crawls/country
  暂停和继续方法

runspider  # 运行爬虫
    scrapy runspider examplee/spiders/maitian.py 

shell  # 时时查看抓取的数据
    scrapy shell http://example.webscraping.com/view/United-Kingdom-239
```