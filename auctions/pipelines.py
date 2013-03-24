from scrapy.exceptions import DropItem
from scrapy.conf import settings

from dumptruck import DumpTruck
from bs4 import BeautifulSoup
from delorean import Delorean, parse
import phonenumbers
import re

class AuctionsPipeline(object):
    def open_spider(self, spider):
        self.dt = DumpTruck(dbname=settings['DB_PATH'],auto_commit=True)

        id_data = self.dt.execute('SELECT id FROM auctions')
        self.ids = [x['id'] for x in id_data]

    def process_item(self, item, spider):
        item['id'] = int(item['id'][0])
        item['auctioneer'] = ' '.join(item['auctioneer'])
        item['contact_number'] = ' '.join(item['contact_number'])
        item['date'] = '%s %s' % (' '.join(item['date']), ' '.join(item['time']))
        item['location'] = ' '.join(item['location'])
        item['link'] = ' '.join(item['link'])
        item['listing'] = ' '.join(item['listing'])

        #format phonenumber
        parsed_number = phonenumbers.parse(item['contact_number'],'US')
        item['contact_number'] = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumber())

        # format listing / remove any html cludge
        soup_listing = BeautifulSoup(item['listing'])
        item['listing'] = soup_listing.get_text()

        # format date and time to standard format
        dt = parse(item['date'])
        item['date'] = dt.datetime.strftime('%Y-%m-%d %H:%M:%S')

        if item['id'] in self.ids:
            raise DropItem('Dupe auction stored, ignoring listing: %s' % item)
        else:
            self.dt.insert({
                'id': item['id'],
                'auctioneer': item['auctioneer'],
                'contact_number': item['contact_number'],
                'date': item['date'],
                'location': item['location'],
                'link': item['link'],
                'listing': item['listing'],
            }, 'auctions')

            return item
