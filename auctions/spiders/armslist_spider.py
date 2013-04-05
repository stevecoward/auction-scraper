from scrapy.http import Request
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.conf import settings

from auctions.items import SearchResultItem

from auctions.models.base import Session
from auctions.models.auction import Auction

import hashlib

class ArmsListSpider(BaseSpider):
    name = "armslist"
    pipelines = ["search_results"]
    allowed_domains = ["armslist.com"]
    domain_prefix = "http://www.armslist.com"

    # intentionally blank. to be populated dynamically.
    start_urls = []

    def __init__(self, auction_id=None):
        self.auction_id = auction_id

    def start_requests(self):
        # fetch auction listing items and build out start_urls accordingly
        listing = Session().query(Auction.listing).filter(Auction.id == self.auction_id).first()
        listing = listing[0].split('\n') if len(listing) > 0 else []

        for item in listing:
            yield Request('%s' % settings['BASE_SEARCH_URL_AL'].replace('{keyword}',item.replace('&','%26')), self.parse)

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        parse_prices = lambda l: filter(bool,[item.strip() for item in l])

        item_name = hxs.select("//input[contains(concat(' ', @class, ' '), ' search-within ')]/@value").extract()
        item_hash = hashlib.md5('%s::%s::%s' % (self.auction_id, item_name, self.name)).hexdigest()
        item_price = parse_prices(hxs.select("//div[2]//div[2]/text()").extract())

        loader = XPathItemLoader(item=SearchResultItem(), response=response)
        loader.add_value("id",item_hash)
        loader.add_value("auction_id",self.auction_id)
        loader.add_value("site",self.name)
        loader.add_xpath("name","//input[contains(concat(' ', @class, ' '), ' search-within ')]/@value")
        loader.add_value("link",response.url)
        loader.add_value("price",item_price)

        return loader.load_item()
