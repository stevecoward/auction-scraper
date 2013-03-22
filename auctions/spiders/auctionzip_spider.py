from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

class AuctionZipSpider(BaseSpider):
    name = "auctionzip"
    allowed_domains = ["auctionzip.com"]
    domain_prefix = "http://www.auctionzip.com"
    start_urls = [
        "http://www.auctionzip.com/cgi-bin/auctionlist.cgi?txtSearchZip=19115&txtSearchRadius=100&idxSearchCategory=0&gid=0&year=2013&month=3&day=23&txtSearchKeywords=firearm"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        
        # featured auction + regular auction url list
        featured_url = hxs.select("//div[contains(concat(' ', @class, ' '), ' rsInner ')]//div[1]//table//tr//td//table[1]//tr//td[1]//b//u//a//@href").extract()
        remaining_urls = hxs.select("//div[2]//table//tr//td//table[1]//tr//td[1]//b//u//a//@href").extract()

        auction_links = featured_url + remaining_urls
        for link in auction_links:
            print "%s%s" % (self.domain_prefix,link)
