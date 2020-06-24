import logging
from web_app.routes.home_routes import home_routes
from web_app.routes.prediction_routes import prediction_routes
from web_app.routes.price_routes import price_routes
from . import settings, routes
from flask import Flask
from flask_cors import CORS


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    cors = CORS(app, resources={r"/*": {"origins": "*"}})
    logging.getLogger('flask_cors').level = logging.DEBUG
    app.register_blueprint(home_routes)
    app.register_blueprint(prediction_routes)
    app.register_blueprint(price_routes)
    return app


if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
