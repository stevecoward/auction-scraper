from flask import Blueprint, render_template, request, g, redirect, url_for, flash, jsonify
from app.main import main

from app.models.base import Session
from app.models.auction import Auction

from delorean import Delorean

admin = Blueprint('admin', __name__, static_folder='static')

@admin.route('/')
def index():
    auctions = Session().query(Auction).order_by(Auction.date.desc()).all()
    dt = Delorean()
    return render_template('admin/index.html', auctions=auctions, now=int(dt.epoch()))
