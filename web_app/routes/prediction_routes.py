from flask import Blueprint, render_template
from flask import Flask, request, jsonify
from airbnb_functions import preprocessing, xgboost_function, df_maker
import requests


prediction_routes = Blueprint('prediction_routes', __name__)


@prediction_routes.route('/prediction', methods=['POST'])
def prediction():
    request_data = request.get_json(force=True)
    print(type(request_data))
    neighborhood_group = request_data["neighborhood_group"]
    neighborhood =request_data["neighborhood"]
    latitude =request_data["latitude"]
    longitude =request_data["longitude"]
    room_type =request_data["room_type"]
    minimum_nights =request_data["minimum_nights"]
    number_of_reviews =request_data["number_of_reviews"]
    calculated_host_listing_count =request_data["calculated_host_listing_count"]
    availability_365 =request_data["availability_365"]

    model = load(open("model.pkl", "rb"))

    df = pd.read_csv('AB_NYC_2019.csv')

    X_train_df, X_test_df, X_train, X_test, y_train, y_test = preprocessing(df)


    return X_train_df.to_json(orient='records')

@prediction_routes.route('/test', methods=['GET'])
def test():
    neighborhood_group = "Staten Island" 
    neighborhood = "Port Richmond"
    latitude = 40.615542
    longitude = -74.14331
    room_type = "Private room"
    minimum_nights = 10
    number_of_reviews = 0
    calculated_host_listing_count = 0
    availability_365 = 60
    post = {"neighborhood_group": neighborhood_group}
    post = {"neighborhood": neighborhood}
    post = {"latitude": latitude}
    post = {"longitude": longitude}
    post = {"room_type": room_type}
    post = {"minimum_nights": minimum_nights}
    post = {"number_of_reviews": number_of_reviews}
    post = {"calculated_host_listing_count": calculated_host_listing_count}
    post = {"availability_365": availability_365}

    URL = "http://127.0.0.1:5000/prediction"

    req = requests.post(URL, json=post)
    return req.text
    