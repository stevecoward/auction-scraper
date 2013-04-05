#!/usr/bin/env python
from flask import Flask, redirect, url_for
from flask.ext.bootstrap import Bootstrap

from datetime import datetime
from delorean import Delorean, parse

main = Flask(__name__)
main.config.from_pyfile('../misc/app.cfg')

# load flask-bootstrap middleware
Bootstrap(main)

main.config['BOOTSTRAP_USE_MINIFIED'] = True
main.config['BOOTSTRAP_USE_CDN'] = True
main.config['BOOTSTRAP_FONTAWESOME'] = True

import admin
admin.register_to(main)

from app.models.base import Session
from app.models.auction_item import AuctionItem

def format_date(date):
    return date.strftime("%a %B %d, %I:%M %p")

def epoch(date):
    dt = Delorean(datetime=date, timezone='US/Eastern')
    return int(dt.epoch())

def has_listing_prices(auction_id):
    return True if Session().query(AuctionItem).filter(AuctionItem.auction_id == auction_id).count() > 0 else False

@main.teardown_request
def teardown_request(exception=None):
    try:
        Session.remove()
    except:
        pass

@main.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('admin.index'))

main.jinja_env.filters['has_listing_prices'] = has_listing_prices
main.jinja_env.filters['format_date'] = format_date
main.jinja_env.filters['epoch'] = epoch
