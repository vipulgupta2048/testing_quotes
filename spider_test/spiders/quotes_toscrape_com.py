# -*- coding: utf-8 -*-
import scrapy
from spider_test.items import TestItem1, TestItem2

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
