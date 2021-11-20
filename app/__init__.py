from flask import *

def create_app():
    app = Flask(__name__)
    #
    from .views import bp
    app.register_blueprint(bp)
    #
    return app