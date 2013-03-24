from scrapy.http import Request
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.conf import settings

from auctions.items import AuctionsItem

import re

class AuctionZipSpider(BaseSpider):
    name = "auctionzip"
    allowed_domains = ["auctionzip.com"]
    domain_prefix = "http://www.auctionzip.com"
    start_urls = [
        "http://www.auctionzip.com/cgi-bin/auctionlist.cgi?txtSearchZip=19115&txtSearchRadius=100&idxSearchCategory=0&gid=0&year=2013&month=3&day=23&txtSearchKeywords=firearm",
        "http://www.auctionzip.com/cgi-bin/auctionlist.cgi?txtSearchZip=19115&txtSearchRadius=100&idxSearchCategory=0&gid=0&year=2013&month=3&day=24&txtSearchKeywords=firearm",
        "http://www.auctionzip.com/cgi-bin/auctionlist.cgi?txtSearchZip=19115&txtSearchRadius=100&idxSearchCategory=0&gid=0&year=2013&month=3&day=25&txtSearchKeywords=firearm",
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        
        # featured auction + regular auction url list
        auction_links = hxs.select(settings['AUCTION_URLS']).extract()
        for link in auction_links:
            yield Request("%s%s" % (self.domain_prefix, link), callback=self.parse_links)

    def parse_links(self, response):
        listing = re.findall(r"lid=(\d+)",response.url)

        loader = XPathItemLoader(item=AuctionsItem(), response=response)
        loader.add_value("id",listing[0])
        loader.add_xpath("auctioneer",settings['AUCTION_AUCTIONEER'])
        loader.add_xpath("contact_number",settings['AUCTION_CONTACT_NUMBER'])
        loader.add_xpath("date",settings['AUCTION_DATE'])
        loader.add_xpath("time",settings['AUCTION_TIME'])
        loader.add_xpath("location",settings['AUCTION_LOCATION'])
        loader.add_value("link",response.url)
        loader.add_xpath("listing",settings['AUCTION_LISTING'])

        return loader.load_item()
