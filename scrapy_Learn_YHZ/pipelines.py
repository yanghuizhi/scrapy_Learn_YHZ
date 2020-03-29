# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapyLearnYhzPipeline(object):
    def process_item(self, item, spider):
        return item


# 保存到 json
# import json
# class JsonPipeline(object):
#     file_name = base_dir + '/doubanTop250/data.json'  # json 文件路径
#     def process_item(self, item, spider):
#         file = open(self.file_name, 'r', encoding='utf-8')
#         load_data = json.load(file)
#         load_data.append({"title": item["title"].strip()}) # 追加数据
#         file = open(self.file_name, 'w', encoding='utf-8')
#         json.dump(load_data, file, ensure_ascii=False) # 保存数据
#         file.close()
#         return item

# 保存到cvs
# def appendDta2Csv(self, file_name, new_headers, new_data):
#     with open(file_name, 'r') as f:
#         f_csv = csv.reader(f)
#         try:  # 如何有源文件没有 headers ，将调用传进来的 headers
#             headers = next(f_csv)
#         except:
#             headers = new_headers
#         old_data = list(f_csv)
#         old_data.append(new_data)  # 追加新的数据
#         with open(file_name, 'w') as f2:  # 保存数据
#             f_csv = csv.writer(f2)
#             f_csv.writerow(headers)
#             f_csv.writerows(old_data)
#             f2.close()
#         f.close()
#
# def process_item(self, item, spider):
#     self.appendDta2Csv(self.file_name, ["title"], [item["title"].strip()])
#     return item

# 保存到 MongoDB
# from pymongo import MongoClient
# import os
# base_dir = os.getcwd()
# class MongoPipeline(object):
#     # 实现保存到mongo数据库的类，
#     collection = 'douban'  # mongo 数据库的 collection 名字
#
#     def __init__(self, mongo_uri, db_name, db_user, db_pass):
#         self.mongo_uri = mongo_uri
#         self.db_name = db_name
#         self.db_user = db_user
#         self.db_pass = db_pass
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         # scrapy 为我们访问settings提供了这样的一个方法，这里，
#         # 我们需要从 settings.py 文件中，取得数据库的URI和数据库名称
#         return cls(
#             mongo_uri=crawler.settings.get('MONGO_URI'),
#             db_name=crawler.settings.get('DB_NAME'),
#             db_user=crawler.settings.get('DB_USER'),
#             db_pass=crawler.settings.get('DB_PASS'))
#
#     def open_spider(self, spider):  # 爬虫启动时调用，连接到数据库
#         self.client = MongoClient(self.mongo_uri)
#         self.zfdb = self.client[self.db_name]
#         self.zfdb.authenticate(self.db_user, self.db_pass)
#
#     def close_spider(self, spider):  # 爬虫关闭时调用，关闭数据库连接
#         self.client.close()
#
#     def process_item(self, item, spider):
#         self.zfdb[self.collection].insert({"title": item["title"].strip()})
#         return item

# 保存到 MySQL
# from sqlalchemy import create_engine, Column, Integer, String, BIGINT, ForeignKey, UniqueConstraint, Index, and_, \
#     or_, inspect
# from sqlalchemy.orm import sessionmaker, relationship, contains_eager
# class MysqlPipeline(object):
#     MYSQL_URI = 'mysql+pymysql://username:password@localhost:3306/db_name'
#     # echo 为 True 将会输出 SQL 原生语句
#     engine = create_engine(MYSQL_URI, echo=True)
#     from sqlalchemy.ext.declarative import declarative_base
#     Base = declarative_base()
#
#     # 创建单表
#     class Movie(Base):
#         __tablename__ = 'movies'
#         id = Column(BIGINT, primary_key=True, autoincrement=True)
#         title = Column(String(200))
#     # 初始化数据库
#     def init_db(self):
#         self.Base.metadata.create_all(self.engine)
#     # 删除数据库
#     def drop_db(self):
#         self.Base.metadata.drop_all(self.engine)
#     def open_spider(self, spider):  # 爬虫启动时调用，连接到数据库
#         self.init_db()
#         Session = sessionmaker(bind=self.engine)
#         self.session = Session()
#     def process_item(self, item, spider):
#         new_movie = self.Movie(title=item["title"].strip())
#         self.session.add(new_movie)
#         self.session.commit()
#         return item

# douyu配置
import scrapy
import os
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings

class ImagesPipeline(ImagesPipeline):
    IMAGES_STORE = get_project_settings().get("IMAGES_STORE")

    def get_media_requests(self, item, info):
        image_url = item["imagesUrls"]
        yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        # 固定写法，获取图片路径，同时判断这个路径是否正确，如果正确，就放到 image_path里，ImagesPipeline源码剖析可见
        image_path = [x["path"] for ok, x in results if ok]

        os.rename(self.IMAGES_STORE + "/" + image_path[0], self.IMAGES_STORE + "/" + item["name"] + ".jpg")
        item["imagesPath"] = self.IMAGES_STORE + "/" + item["name"]

        return item

#get_media_requests的作用就是为每一个图片链接生成一个Request对象，这个方法的输出将作为item_completed的输入中的results，results是一个元组，每个元组包括(success, imageinfoorfailure)。如果success=true，imageinfoor_failure是一个字典，包括url/path/checksum三个key。