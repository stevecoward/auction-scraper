import admin
import endpoint

def register_to(app):
    app.register_blueprint(admin.admin, url_prefix='/admin')
    app.register_blueprint(endpoint.endpoint, url_prefix='/admin/json')
