# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class DoubanmoviePipeline(object):
    def __init__(self):
        self.client = pymysql.connect(host='127.0.0.1',
                        port=3306,
                        user='root',
                        password='123456',
                        db='douban',
                        charset='utf8'
                        )
        self.cur = self.client.cursor()

    def process_item(self, item, spider):
        keys = item.keys()
        values = tuple(item.values())
        field = ','.join(keys)
        temp = ','.join(['%s'] * len(keys))
        sql = 'insert into movie (%s) values (%s)' % (field, temp)
        self.cur.execute(sql, values)
        self.client.commit()
        return item
