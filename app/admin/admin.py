from flask import Blueprint, render_template, request, g, redirect, url_for, flash, jsonify
from app.main import main

from app.models.base import Session
from app.models.auction import Auction
from app.models.auction_item import AuctionItem

from delorean import Delorean

admin = Blueprint('admin', __name__, static_folder='static')

@admin.route('/')
def index():
    dt = Delorean()
    auctions = Session().query(Auction).order_by(Auction.date.desc()).all()
    return render_template('admin/index.html', auctions=auctions, now=int(dt.epoch()))

@admin.route('/auction/<int:auction_id>/listing-prices', methods=['GET'])
def auction(auction_id):
    print AuctionItem.get_items_by_auction(1731540)
    return render_template('admin/auction.html')
