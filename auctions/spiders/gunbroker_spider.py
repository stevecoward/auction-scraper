from scrapy.http import Request
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.conf import settings

from auctions.items import SearchResultItem

from auctions.models.base import Session
from auctions.models.auction import Auction

class GunBrokerSpider(BaseSpider):
    name = "gunbroker"
    allowed_domains = ["gunbroker.com"]
    domain_prefix = "http://www.gunbroker.com"

    # intentionally blank. to be populated dynamically.
    start_urls = ["http://www.gunbroker.com/Firearms/BI.aspx?Keywords=Glock+27+40+cal&Timeframe=16&Sort=5&PageSize=75"]

    def parse(self, response):
        print '18'
        print Session().query(Auction).filter(Auction.id == 1731540).first().listing
