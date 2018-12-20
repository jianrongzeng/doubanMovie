from scrapy import cmdline

cmdline.execute("scrapy crawl doubanmovie -o title.json".split())