# -*- coding: utf-8 -*-
import scrapy
# from spider_test.items import TestItem1, TestItem2


class QuotesToscrapeComSpider(scrapy.Spider):
    name = "quotes.toscrape.com"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        for quote in response.css(".quote"):
            yield {
                "quote": quote.css(".text::text").get(),
                "author": quote.css(".author::text").get(),
                "author_url": response.urljoin(
                    quote.css(".author a::attr(href)").get()
                ),
                "tags": quote.css(".tag *::text").getall(),
            }

        # if you are going for multple items and need to test individually
        # x = TestItem1()
        # y = TestItem2()
        # for quote in response.css(".quote"):
        #     x['quote'] = quote.css(".text::text").get()
        #     y['author'] = quote.css(".author::text").get()

        #     yield x
        #     yield y
