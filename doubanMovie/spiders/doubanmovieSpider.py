# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor

from doubanMovie.items import DoubanmovieItem


class DoubanmovieSpider(CrawlSpider):
    name = 'doubanmovie'
    allowed_domains = ['movie.douban.com']
    start_urls = [
        'https://movie.douban.com/people/85965842/collect'
    ]
    rules = (
        Rule(LinkExtractor(allow=('/people/85965842/collect\?start.*')), follow=True),
        Rule(LinkExtractor(allow=('movie.douban.com/subject/(\d)*/(\?from=subject-page)?$')),
             callback='parse_detail', follow=True),
    )

    # def parse(self, response):
    # 获取列表页中每一部电影的条目
    # print("parse----" + response.url)
    # for index, div in enumerate(response.xpath("//div[@class='item']")):

    # 获取电影标题
    # title = div.xpath(".//em/text()").extract()[0]
    # 获取电影详情页链接
    # url = div.xpath(".//li[@class='title']//a/@href").extract()[0]
    # 将详情页链接添加到待爬取队列，新链接用parse_detail函数解析
    # yield scrapy.Request(url, callback=self.parse_detail)
    # item["title"] = title
    # item["url"] = url
    # yield item
    # items.append(item)
    # 获取列表页中的下一页链接
    # next_page_href = response.xpath("//link[@rel='next']/@href").extract()[0]
    # print(response.urljoin(next_page_href))
    # next_page_url = response.urljoin(next_page_href)
    # 将下一页的链接添加到待爬取队列，新链接用parse函数解析
    # yield scrapy.Request(next_page_url, callback=self.parse)
    # return items

    def parse_detail(self, response):
        print("parse_detail----" + response.url)
        item = DoubanmovieItem()
        self.get_id(item, response)
        self.get_douban_url(item, response)
        self.get_title(item, response)
        self.get_director(item, response)
        self.get_screenwritter(item, response)
        self.get_actors(item, response)
        self.get_type(item, response)
        self.get_country(item, response)
        self.get_language(item, response)
        self.get_release_date(item, response)
        self.get_film_length(item, response)
        self.get_alias(item, response)
        self.get_imdb_url(item, response)
        self.get_synopsis(item, response)
        self.get_score(item, response)
        self.get_people_number(item, response)
        return item

    def get_id(self, item, response):
        item['id'] = re.findall(r"(?<=/subject/)\d+", response.url)[0]
        return item

    def get_douban_url(self, item, response):
        item['douban_url'] = response.url
        return item

    def get_title(self, item, response):
        title = response.xpath("//*[@id='content']/h1/span/text()").extract()
        if title:
            item['title'] = title[0]
        return item

    def get_director(self, item, response):
        item['director'] = response.xpath("//*[@id='info']/span[1]/span[2]/a/text()").extract()[0]
        return item

    def get_screenwritter(self, item, response):
        item['screenwritter'] = response.xpath("//*[@id='info']/span[2]/span[2]/a/text()").extract()[0]
        return item

    def get_actors(self, item, response):
        item['actors'] = response.xpath("string(//*[@id='info']/span[3]/span[2])").extract()[0]
        return item

    def get_type(self, item, response):
        item['type'] = ' / '.join(response.xpath("//span[@property='v:genre']/text()").extract())
        return item

    def get_country(self, item, response):
        item['country'] = response.xpath('//text()[preceding-sibling::span[text()="制片国家/地区:"]]['
                                         'following-sibling::br]').extract()[0].strip()
        return item

    def get_language(self, item, response):
        item['language'] = response.xpath('//text()[preceding-sibling::span[text()="语言:"]]['
                                          'following-sibling::br]').extract()[0].strip()
        return item

    def get_release_date(self, item, response):
        release_date = response.xpath("//span[@property='v:initialReleaseDate']/text()").extract()
        if release_date:
            item['release_date'] = release_date[0]
        return item

    def get_film_length(self, item, response):
        film_length = response.xpath("//span[@property='v:runtime']/text()").extract()
        if film_length:
            item['film_length'] = film_length[0]
        return item

    def get_alias(self, item, response):
        alias = response.xpath("//text()[preceding-sibling::span[text()='又名:']]["
                                       "following-sibling::br]").extract()
        if alias:
            item['alias'] = alias[0].strip()
        return item

    def get_imdb_url(self, item, response):
        imdb_url = response.xpath("//*[@id='info']/a/@href").extract()
        if imdb_url:
            item['imdb_url'] = imdb_url[0]
        return item

    def get_synopsis(self, item, response):
        synopsis = response.xpath("//span[@property='v:summary']/text()").extract()
        if synopsis:
            item['synopsis'] = synopsis[0].strip().replace('\r\n', '')
        return item

    # 需改进
    def get_score(self, item, response):
        score = response.xpath("//strong[@property='v:average']/text()").extract()
        if score:
            item['score'] = score[0]
        return item

    # 需改进
    def get_people_number(self, item, response):
        people_number = response.xpath("//span[@property='v:votes']/text()").extract()
        if people_number:
            item['people_number'] = people_number[0]
        return item
