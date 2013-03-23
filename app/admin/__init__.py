import admin

def register_to(app):
    app.register_blueprint(admin.admin)
