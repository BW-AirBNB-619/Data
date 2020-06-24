from flask import Blueprint, render_template

prediction_routes = Blueprint('prediction_routes', __name__)

@prediction_routes('/prediction', methods=['GET', 'POST'])
def prediction():
    """ GET user input then Predicts """

    user_features = requests.json('https://pray-this-works.herokuapp.com/')
    # This returns a dict from Front End
    user_features = user_features.text.strip('[]')
    print(user_features)


    xgb_model = pickle.load(open('model.pkl', 'rb'))

    sample = {'neighbourhood_group', 'neighbourhood', 'latitude', 'longitude', 'room_type',
              'minimum_nights', 'number_of_reviews', 'calculated_host_listing_count',
              'availability_365'
                }

    # Transforms the json received from users
    data = transform_json(sample)
    df = encode_data(data)

    prediction = xgb_model.predict(df)
    predict_dict = {}
    predict_dict['Optimal Price'] = round(float(prediction[0]), 2)

    # Stores predict_dict in the session, so it can be gotten from /data
    # session['price'] = predict_dict

    return jsonify(predict_dict)


@prediction_routes('/prediction', methods=['POST']) #Getting data posted to us
@price_routes('/price/getprice', methods=['GET']) #Serving Data
def data():
    price = session.get('price')

    return jsonify(price)


    return app