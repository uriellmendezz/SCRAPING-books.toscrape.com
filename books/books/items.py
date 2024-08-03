# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BooksItem(scrapy.Item):
    # define the fields for your item here like:
    
    url = scrapy.Field()
    gender = scrapy.Field()
    title = scrapy.Field()
    rating = scrapy.Field()
    description = scrapy.Field()
    upc = scrapy.Field()
    product_type = scrapy.Field()
    price_original = scrapy.Field()
    price_taxes = scrapy.Field()
    taxes = scrapy.Field()
    stock = scrapy.Field()
    reviews = scrapy.Field()
