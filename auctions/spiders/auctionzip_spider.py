from scrapy.http import Request
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.conf import settings

from auctions.items import AuctionsItem

import re

class AuctionZipSpider(BaseSpider):
    name = "auctionzip"
    pipelines = ["auctions"]
    allowed_domains = ["auctionzip.com"]
    domain_prefix = "http://www.auctionzip.com"
    start_urls = [
        "http://www.auctionzip.com/cgi-bin/auctionlist.cgi?txtSearchZip=19115&txtSearchRadius=100&idxSearchCategory=0&gid=0&year=2013&month=4&day=02&txtSearchKeywords=firearm",
        "http://www.auctionzip.com/cgi-bin/auctionlist.cgi?txtSearchZip=19115&txtSearchRadius=100&idxSearchCategory=0&gid=0&year=2013&month=4&day=03&txtSearchKeywords=firearm",
        "http://www.auctionzip.com/cgi-bin/auctionlist.cgi?txtSearchZip=19115&txtSearchRadius=100&idxSearchCategory=0&gid=0&year=2013&month=4&day=04&txtSearchKeywords=firearm",
        "http://www.auctionzip.com/cgi-bin/auctionlist.cgi?txtSearchZip=19115&txtSearchRadius=100&idxSearchCategory=0&gid=0&year=2013&month=4&day=05&txtSearchKeywords=firearm",
        "http://www.auctionzip.com/cgi-bin/auctionlist.cgi?txtSearchZip=19115&txtSearchRadius=100&idxSearchCategory=0&gid=0&year=2013&month=4&day=06&txtSearchKeywords=firearm",
        "http://www.auctionzip.com/cgi-bin/auctionlist.cgi?txtSearchZip=19115&txtSearchRadius=100&idxSearchCategory=0&gid=0&year=2013&month=4&day=07&txtSearchKeywords=firearm",
        "http://www.auctionzip.com/cgi-bin/auctionlist.cgi?txtSearchZip=19115&txtSearchRadius=100&idxSearchCategory=0&gid=0&year=2013&month=4&day=08&txtSearchKeywords=firearm",
        "http://www.auctionzip.com/cgi-bin/auctionlist.cgi?txtSearchZip=19115&txtSearchRadius=100&idxSearchCategory=0&gid=0&year=2013&month=4&day=09&txtSearchKeywords=firearm",
        "http://www.auctionzip.com/cgi-bin/auctionlist.cgi?txtSearchZip=19115&txtSearchRadius=100&idxSearchCategory=0&gid=0&year=2013&month=4&day=10&txtSearchKeywords=firearm",
        "http://www.auctionzip.com/cgi-bin/auctionlist.cgi?txtSearchZip=19115&txtSearchRadius=100&idxSearchCategory=0&gid=0&year=2013&month=4&day=11&txtSearchKeywords=firearm",
        "http://www.auctionzip.com/cgi-bin/auctionlist.cgi?txtSearchZip=19115&txtSearchRadius=100&idxSearchCategory=0&gid=0&year=2013&month=4&day=12&txtSearchKeywords=firearm",
        "http://www.auctionzip.com/cgi-bin/auctionlist.cgi?txtSearchZip=19115&txtSearchRadius=100&idxSearchCategory=0&gid=0&year=2013&month=4&day=13&txtSearchKeywords=firearm",
        "http://www.auctionzip.com/cgi-bin/auctionlist.cgi?txtSearchZip=19115&txtSearchRadius=100&idxSearchCategory=0&gid=0&year=2013&month=4&day=14&txtSearchKeywords=firearm",
        "http://www.auctionzip.com/cgi-bin/auctionlist.cgi?txtSearchZip=19115&txtSearchRadius=100&idxSearchCategory=0&gid=0&year=2013&month=4&day=15&txtSearchKeywords=firearm",
        "http://www.auctionzip.com/cgi-bin/auctionlist.cgi?txtSearchZip=19115&txtSearchRadius=100&idxSearchCategory=0&gid=0&year=2013&month=4&day=16&txtSearchKeywords=firearm",
        "http://www.auctionzip.com/cgi-bin/auctionlist.cgi?txtSearchZip=19115&txtSearchRadius=100&idxSearchCategory=0&gid=0&year=2013&month=4&day=17&txtSearchKeywords=firearm",
        "http://www.auctionzip.com/cgi-bin/auctionlist.cgi?txtSearchZip=19115&txtSearchRadius=100&idxSearchCategory=0&gid=0&year=2013&month=4&day=18&txtSearchKeywords=firearm",
        "http://www.auctionzip.com/cgi-bin/auctionlist.cgi?txtSearchZip=19115&txtSearchRadius=100&idxSearchCategory=0&gid=0&year=2013&month=4&day=19&txtSearchKeywords=firearm",
        "http://www.auctionzip.com/cgi-bin/auctionlist.cgi?txtSearchZip=19115&txtSearchRadius=100&idxSearchCategory=0&gid=0&year=2013&month=4&day=20&txtSearchKeywords=firearm",
        "http://www.auctionzip.com/cgi-bin/auctionlist.cgi?txtSearchZip=19115&txtSearchRadius=100&idxSearchCategory=0&gid=0&year=2013&month=4&day=21&txtSearchKeywords=firearm",
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
