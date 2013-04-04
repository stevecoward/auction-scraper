from sqlalchemy import Column, Integer, String
from base import Base, Session
from app.main import main

class AuctionItem(Base):
    __tablename__ = 'auction_items'

    id = Column(String(), primary_key=True, nullable=False)
    auction_id = Column(Integer())
    site = Column(String())
    link = Column(String())
    name = Column(String())
    price = Column(String())
    modified = Column(Integer())
