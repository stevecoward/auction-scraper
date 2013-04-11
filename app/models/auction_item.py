from sqlalchemy import Column, Integer, String
from sqlalchemy import distinct
from base import Base, Session
from app.main import main
from app.utilities import result_to_list

class AuctionItem(Base):
    __tablename__ = 'auction_items'

    id = Column(String(), primary_key=True, nullable=False)
    auction_id = Column(Integer())
    site = Column(String())
    link = Column(String())
    name = Column(String())
    price = Column(String())
    modified = Column(Integer())

    @staticmethod
    def get_items_by_auction(auction_id):
        results = []
        items = Session().query(distinct(AuctionItem.name).label('name')).filter(AuctionItem.auction_id == auction_id).all()

        # loop thru items and gather price data
        for item in items:
            data = Session().query(AuctionItem)\
                .filter(AuctionItem.auction_id == auction_id)\
                .filter(AuctionItem.name == item.name)\
                .all()

            results.append({
                'item': item.name, 
                'data': [{ 
                    'site': x.site,
                    'modified': x.modified,
                    'link': x.link,
                    'max': AuctionItem.max_price(x.price),
                    'avg': AuctionItem.avg_price(x.price)
                } for x in data]
            })

        return results

    @staticmethod
    def max_price(s):
        return max([float(x) for x in s.split(',')])

    @staticmethod
    def avg_price(s):
        return round(sum([float(x) for x in s.split(',')]) / float(len([float(x) for x in s.split(',')])),2)
