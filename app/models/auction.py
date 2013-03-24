from sqlalchemy import Column, Integer, String, DateTime, Boolean
from base import Base, Session
from app.main import main

class Auction(Base):
    __tablename__ = 'auctions'

    id = Column(Integer(), primary_key=True, nullable=False)
    auctioneer = Column(String())
    contact_number = Column(String())
    date = Column(DateTime())
    location = Column(String())
    link = Column(String())
    listing = Column(String())
    dirty = Column(Boolean(), nullable=False)
