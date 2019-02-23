# -*- coding: utf-8 -*-
import scrapy

from doubanMovie.items import DoubanmovieItem


class DoubanmovieSpider(scrapy.Spider):
    name = 'doubanmovie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/people/85965842/collect']

    custom_settings = {
        "DEFAULT_REQUEST_HEADERS": {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        }
    }

    def parse(self, response):
        items = []
        # 获取列表页中每一部电影的条目
        for index, div in enumerate(response.xpath("//div[@class='item']")):
            item = DoubanmovieItem()
            # 获取电影标题
            # title = div.xpath(".//em/text()").extract()[0]
            # 获取电影详情页链接
            url = div.xpath(".//li[@class='title']//a/@href").extract()[0]
            # 将详情页链接添加到待爬取队列，新链接用parse_detail函数解析
            yield scrapy.Request(url, meta={"item": item}, callback=self.parse_detail)
            # item["title"] = title
            # item["url"] = url
            # yield item
            # items.append(item)
        # 获取列表页中的下一页链接
        next_page_href = response.xpath("//link[@rel='next']/@href").extract()[0]
        print(response.urljoin(next_page_href))
        next_page_url = response.urljoin(next_page_href)
        # 将下一页的链接添加到待爬取队列，新链接用parse函数解析
        yield scrapy.Request(next_page_url, callback=self.parse)
        # return items

    def parse_detail(self, response):
        title = response.xpath("//*[@id='content']/h1/span").extract()[0]
        # print(str)
        item = response.meta["item"]
        item["title"] = title
        item["url"] = ""
        return item
