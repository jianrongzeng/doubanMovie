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
        # filename = "indexdouban.html"
        # open(filename, "w").write(response)
        print(response.body.decode('utf-8'))
        items = []
        for div in response.xpath("//div[@class='item']"):
            item = DoubanmovieItem()
            title = div.xpath("//em/text()").extract()

            item["title"] = title

            items.append(item)
        return items






