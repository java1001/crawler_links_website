from scrapy.item import Item, Field
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import TakeFirst


class Link(Item):
    link = Field()

class LinkLoader(XPathItemLoader):
    default_item_class = Link
    default_output_processor = TakeFirst()
