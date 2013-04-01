from flask import Blueprint, render_template, request, g, redirect, url_for, flash, jsonify
from app.main import main

from app.models.base import Session
from app.models.auction import Auction

endpoint = Blueprint('endpoint', __name__)

@endpoint.route('/listing', methods=['POST'])
def get_auction_listing():
    import pdb; pdb.set_trace()
    return jsonify({'status': 'ok','data': 'data'})
