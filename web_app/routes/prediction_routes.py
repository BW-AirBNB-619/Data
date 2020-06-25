from flask import Blueprint, render_template
from flask import Flask, request, jsonify
from airbnb_functions import preprocessing, rfr_function, accum
import requests
import pandas as pd 



prediction_routes = Blueprint('prediction_routes', __name__)


@prediction_routes.route('/prediction', methods=['POST'])
def prediction():
    request_data = request.get_json(force=True)
    print(type(request_data))
    neighbourhood_group = request_data["neighbourhood_group"]
    neighbourhood =request_data["neighbourhood"]
    latitude =request_data["latitude"]
    longitude =request_data["longitude"]
    room_type =request_data["room_type"]
    minimum_nights =request_data["minimum_nights"]
    number_of_reviews =request_data["number_of_reviews"]
    calculated_host_listings_count =request_data["calculated_host_listings_count"]
    availability_365 =request_data["availability_365"]


    df = pd.read_csv('AB_NYC_2019.csv')

    new_df = accum(neighbourhood_group, neighbourhood, latitude, longitude, room_type, minimum_nights,
                   number_of_reviews, calculated_host_listings_count, availability_365, df) 

    X_train_df, X_test_df, X_train, X_test, y_train, y_test = preprocessing(new_df)
    pred = rfr_function(X_train, y_train)
    pred = pd.DataFrame(pred, columns=['price'])
    
    return pred.to_json(orient='records')


@prediction_routes.route('/test', methods=['GET'])
def test():
    neighbourhood_group = "Staten Island" 
    neighbourhood = "Port Richmond"
    latitude = 40.615542
    longitude = -74.14331
    room_type = "Private room"
    minimum_nights = 10
    number_of_reviews = 0
    calculated_host_listings_count = 0
    availability_365 = 60
    post = {"neighbourhood_group": neighbourhood_group, "neighbourhood": neighbourhood,
            "latitude": latitude, "longitude": longitude, "room_type": room_type,
            "minimum_nights": minimum_nights, "number_of_reviews": number_of_reviews,
            "calculated_host_listings_count": calculated_host_listings_count,
            "availability_365": availability_365}

    # URL = "http://127.0.0.1:5000/prediction"

    URL = "https://its-the-end-of-the-world.herokuapp.com/prediction"

    req = requests.post(URL, json=post)
    return req.text
    