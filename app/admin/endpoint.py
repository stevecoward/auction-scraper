from flask import Blueprint, render_template, request, g, redirect, url_for, flash, jsonify
from app.main import main
from app.utilities import request_to_dict

from app.models.base import Session
from app.models.auction import Auction

endpoint = Blueprint('endpoint', __name__)

@endpoint.route('/listing', methods=['GET'])
def get_auction_listing():
    data = request_to_dict(request.values)
    if 'listing_id' in data and data['listing_id'] != 0:
        row = Session().query(Auction.listing).filter(Auction.id == data['listing_id']).first()
        if row:
            return jsonify({
                'status': 'ok',
                'data': row.listing
            })
    
    return jsonify({'status': 'error','message': 'invalid/no listing'})

@endpoint.route('/listing/update', methods=['POST'])
def update_auction_listing():
    data = request_to_dict(request.values)
    if 'id' in data and data['id'] != 0:
        data.update({'dirty': 0})
        auction_record = Auction(**data)
        try:
            auction_record.update()
            return jsonify({'status': 'ok'})
        except:
            pass

    return jsonify({'status': 'error','message': 'failed to update listing.'})
