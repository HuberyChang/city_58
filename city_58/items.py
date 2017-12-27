# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item,Field


class City58Xiaoqu(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = Field()
    name = Field()
    reference_price = Field()
    address = Field()
    times = Field()


class City58ChuzuInfo(Item):
    id = Field()
    name = Field()
    zu_price = Field()
    type = Field()
    mianji = Field()
    zu_price_per = Field()
    url = Field()
    price_per = Field()

