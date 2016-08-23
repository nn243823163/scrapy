#coding:utf-8
from peewee import *
import peewee
from playhouse.db_url import connect

db = peewee.MySQLDatabase(host = '127.0.0.1', user = 'root', passwd = '', database = 'caoliu_photo',charset='utf8')

# db = connect('mysql://root:@127.0.0.1:3306/caoliu_photo')  # 连接数据库
# db = MySQLdb.connect(host="localhost",    # your host, usually localhost
#                      user="root",         # your username
#                      passwd="",  # your password
#                      db="caoliu_photo")

# cur = db.cursor()
# Use all the SQL you like
# cur.execute("SELECT * FROM PHOTO")
# print all the first cell of all the rows
# for row in cur.fetchall():
#     print row[1]
# db.close()


class Photo(Model):
    title = CharField()
    link = CharField()
    class Meta:
        database = db  # 要连接的数据库
        db_table = 'photo'  # 要映射的数据表,名称与原表一致


photo = Photo(title=u'\u5a9a\u5a18\u7cfb\u5217\u4e4b\u697c\u9053\u9ed1\u4e1d\u540e\u5165\uff08\u5341\u516b\uff09', link=u'豆豆')
photo.save()

if not Photo.select().where(Photo.id == 111):
    print 'qqq'
else :
    print 'qqqqq'
