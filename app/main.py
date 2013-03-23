#!/usr/bin/env python
from flask import Flask, redirect, url_for
from flask.ext.bootstrap import Bootstrap

main = Flask(__name__)
Bootstrap(main)

main.config['BOOTSTRAP_USE_MINIFIED'] = True
main.config['BOOTSTRAP_USE_CDN'] = True
main.config['BOOTSTRAP_FONTAWESOME'] = True

import admin
admin.register_to(main)

@main.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('admin.index'))
