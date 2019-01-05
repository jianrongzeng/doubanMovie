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
        for index, div in enumerate(response.xpath("//div[@class='item']")):
            item = DoubanmovieItem()
            title = div.xpath(".//em/text()").extract()[0]
            url = div.xpath(".//li[@class='title']//a/@href").extract()[0]
            yield scrapy.Request(url, callback=self.parse_detail)
            # scrapy.Request()
            item["title"] = title
            item["url"] = url
            print("123:" + response.url)
            items.append(item)
        next_page_href = response.xpath("//link[@rel='next']/@href").extract()[0]
        print(response.urljoin(next_page_href))
        next_page_url = response.urljoin(next_page_href)
        yield scrapy.Request(next_page_url, callback=self.parse)
        return items

    def parse_detail(self, response):
        return 0
