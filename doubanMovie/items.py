# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanmovieItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    douban_url = scrapy.Field()
    title = scrapy.Field()
    director = scrapy.Field()
    screenwritter = scrapy.Field()
    actors = scrapy.Field()
    type = scrapy.Field()
    country = scrapy.Field()
    language = scrapy.Field()
    release_date = scrapy.Field()
    film_length = scrapy.Field()
    alias = scrapy.Field()
    imdb_url = scrapy.Field()
    synopsis = scrapy.Field()
    score = scrapy.Field()
    people_number = scrapy.Field()
