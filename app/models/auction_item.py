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

