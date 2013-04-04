# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class AuctionsItem(Item):
    id = Field()
    auctioneer = Field()
    contact_number = Field()
    date = Field()
    time = Field()
    location = Field()
    link = Field()
    listing = Field()

class SearchResultItem(Item):
    id = Field()
    auction_id = Field()
    site = Field()
    name = Field()
    link = Field()
    price = Field()
    modified = Field()
