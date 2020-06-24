from flask import Blueprint, render_template

prediction_routes = Blueprint('prediction_routes', __name__)


@prediction_routes.route('/prediction', methods=["POST"])
def prediction():
    return prediction.predict