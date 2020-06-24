from flask import Blueprint


price_routes = Blueprint('price_routes', __name__)


@price_routes.route('/price', methods=["GET"])
def price():
    return price.predict