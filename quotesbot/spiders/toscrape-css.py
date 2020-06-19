# -*- coding: utf-8 -*-
import scrapy


class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css"
    start_urls = [
        'https://www.bestbuy.com/site/fitness-boxing-nintendo-switch-digital/6321671.p?skuId=6321671',
    ]

    def parse(self, response):
        for quote in response.css("div.shop-product-title"):
            yield {
                'text': quote.css("sku-title::text").extract_first(),
                'author': quote.css("small.author::text").extract_first(),
                'tags': quote.css("div.tags > a.tag::text").extract()
                }

        next_page_url = response.css("li.next > a::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url)
