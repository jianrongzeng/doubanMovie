from scrapy import cmdline

cmdline.execute("scrapy crawl doubanmovie -o test.json".split())