from scrapy.http import Request
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.conf import settings

from auctions.items import SearchResultItem

from auctions.models.base import Session
from auctions.models.auction import Auction

import hashlib

class GunBrokerSpider(BaseSpider):
    name = "gunbroker"
    pipelines = ["search_results"]
    allowed_domains = ["gunbroker.com"]
    domain_prefix = "http://www.gunbroker.com"

    # intentionally blank. to be populated dynamically.
    start_urls = []

    def __init__(self, auction_id=None):
        self.auction_id = auction_id

    def start_requests(self):
        # fetch auction listing items and build out start_urls accordingly
        listing = Session().query(Auction.listing).filter(Auction.id == self.auction_id).first()
        listing = listing[0].split('\n') if len(listing) > 0 else []

        for item in listing:
            yield Request('%s' % settings['BASE_SEARCH_URL_GB'].replace('{keyword}',item.replace('&','%26')), self.parse)

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        item_name = hxs.select("//input[@id='ctl00_ctlPagePlaceHolder_Keywords']/@value").extract()
        item_hash = hashlib.md5('%s::%s' % (self.auction_id, item_name)).hexdigest()

        loader = XPathItemLoader(item=SearchResultItem(), response=response)
        loader.add_value("id",item_hash)
        loader.add_value("auction_id",self.auction_id)
        loader.add_value("site",self.name)
        loader.add_xpath("name","//input[@id='ctl00_ctlPagePlaceHolder_Keywords']/@value")
        loader.add_value("link",response.url)
        loader.add_xpath("price","//td[7]/text()")

        return loader.load_item()
