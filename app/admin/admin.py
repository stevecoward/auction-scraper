from flask import Blueprint, render_template, request, g, redirect, url_for, flash, jsonify
from app.main import main

admin = Blueprint('admin', __name__, static_folder='static', url_prefix='/admin')

@admin.route('/')
def index():
    return render_template('admin/index.html')
