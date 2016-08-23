# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from peewee import *
from playhouse.db_url import connect
import peewee
import MySQLdb

db = connect('mysql://root:@127.0.0.1:3306/caoliu_photo')  # 连接数据库
class Photo(Model):
    title = CharField()
    link = CharField()
    url = CharField()
    class Meta:
        database = db  # 要连接的数据库
        db_table = 'photo'  # 要映射的数据表,名称与原表一致

class TutorialPipeline(object):

    def process_item(self, item, spider):

        #mysqldb操作数据库
        # DBKWARGS = spider.settings.get('DBKWARGS')
        # con = MySQLdb.connect(**DBKWARGS)
        # cur = con.cursor()
        # # sql = ("insert into photo(tittle,link) "
        # #     "values(%s)")
        # # lis = ('111','222')
        # # try:
        # #     cur.execute(sql,lis)
        # # except Exception as e:
        # #     print ("Insert error:",e)
        # #     con.rollback()
        # # else:
        # #     con.commit()
        #
        # # a = "浦发银行"
        # # a = a.decode("utf-8").encode("utf-8")  # 编码转换为utf-8
        # # sql = "insert into photo (tittle,link) values (%s,%s)"  # 生成sql语句
        # # param = ('600000', a)  # 生成sql语句的参数
        # # n = cursor.execute(sql, param)  # 执行sql语句
        #
        # sql = """INSERT INTO photo(title,link)
        #          VALUES ('aaaa', 'Mohan')"""
        # try:
        #     # Execute the SQL command
        #     cur.execute(sql)
        #     # Commit your changes in the database
        #     con.commit()
        # except:
        #     # Rollback in case there is any error
        #     con.rollback()
        #
        # cur.close()
        # con.close()
        #

        item_title = item['title']
        item_link = item['link']
        item_url = item['url']

        if Photo.select().where(Photo.link==item_link):
            pass
        else:
            photo = Photo(title=item_title, link=item_link, url=item_url)
            photo.save()



        return item