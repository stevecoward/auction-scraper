# Scrapy settings for auctions project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'auctions'

SPIDER_MODULES = ['auctions.spiders']
NEWSPIDER_MODULE = 'auctions.spiders'

# Pipeline checks for listing and inserts into db if not exists
ITEM_PIPELINES = [
    'auctions.pipelines.AuctionsPipeline',
]

#FEED_URI = '/private/var/log/auction-pro/auctions.json'
#FEED_FORMAT = 'json'

# Sqlite3 database path
DB_PATH = '/Users/scoward/Development/auction-pro/auction_pro.db'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 4.0; InfoPath.3; MS-RTC LM 8; .NET4.0C; .NET4.0E)'

BASE_SEARCH_URL_GB = "http://www.gunbroker.com/Firearms/BI.aspx?Keywords={keyword}&Timeframe=16&Sort=5&PageSize=75"
BASE_SEARCH_URL_AL = "http://www.armslist.com/classifieds/search?location=usa&category=guns&search={keyword}"
BASE_SEARCH_URL_GUSA = "http://www.gunsamerica.com/Search.htm?ltid-all=1&t={keyword}&og=1&as=365&numberperpage=50"
BASE_SEARCH_URL_GAUC = "http://www.gunauction.com/shop/{keyword}"

# XPath references for scraping auctionzip.com
AUCTION_URLS = "//div[contains(concat(' ', @class, ' '), ' rsInner ')]//@href[contains(., 'auctionview')]"
AUCTION_AUCTIONEER = "/html/body/div[@id='body']/div[@id='bodyInner']/div[@id='innerContent']/div[@id='theContent']/div[@id='innersContent']/div[contains(concat(' ', @class, ' '), ' main3 ')]/table/tr/td[1]/table/tr/td/table/tr[2]/td[2]/text()"
AUCTION_CONTACT_NUMBER = "/html/body/div[@id='body']/div[@id='bodyInner']/div[@id='innerContent']/div[@id='theContent']/div[@id='innersContent']/div[contains(concat(' ', @class, ' '),     ' main3 ')]/table/tr/td[1]/table/tr/td/table/tr[2]/td[3]/text()"
AUCTION_DATE = "/html/body/div[@id='body']/div[@id='bodyInner']/div[@id='innerContent']/div[@id='theContent']/div[@id='innersContent']/div[contains(concat(' ', @class, ' '), ' main3 '    )]/table/tr/td[1]/table/tr/td/table/tr[3]/td[2]/text()"
AUCTION_TIME = "/html/body/div[@id='body']/div[@id='bodyInner']/div[@id='innerContent']/div[@id='theContent']/div[@id='innersContent']/div[contains(concat(' ', @class, ' '), ' main3 '    )]/table/tr/td[1]/table/tr/td/table/tr[4]/td[2]/text()"
AUCTION_LOCATION = "/html/body/div[@id='body']/div[@id='bodyInner']/div[@id='innerContent']/div[@id='theContent']/div[@id='innersContent']/div[contains(concat(' ', @class, ' '), ' main3 ')]/table/tr/td[1]/table/tr/td/table/tr[3]/td[4]/div[1]/text()"
AUCTION_LISTING = "//*[@id='listingReset']"
