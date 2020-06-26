# Data

### flaskenv
'''
  FLASK_APP=web_app/create_app.py
  FLASK_ENV=development
'''
### __init__.py (majority was importing what I needed to make sure that Python was able to read and operate correctly).
'''
  def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    cors = CORS(app)
    app.register_blueprint(home_routes)
    app.register_blueprint(prediction_routes)
    app.register_blueprint(price_routes)
    return app
 if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
    
 '''
<<<<<<< HEAD

### I had some help in creating the prediction_routes.py but spent time making sure that the home and price_routes.py's were similar so that there were no major issues. From the beginning in setting up heroku and creating the app, there were some errors made along the way, but eventually I was able to figure out the problem and got the app up and running from a local perspective. In the end, we did everything, that as a group we could think of, to push a finished product to the front end so that we could connect ALL the dots but were unable to figure out the pickling issue we kept encountering. This was a massive project and I absolutely enjoyed working with Sam and Rourke. If we had one more day, I know we could have finished this with no issues. There were a ton of man hours that went into this. I am proud of the work that I did in helping create routes that were needed, creating and deploying a heroku app, and making sure that all the i's were dotted and that the t's were crossed.
=======
 
 ### I had some help in creating the prediction_routes.py but spent time making sure that the home and price_routes.py's
 ### were similar so that there were no major issues. From the beginning in setting up heroku and creating the app, there
 ### were some errors made along the way, but eventually I was able to figure out the problem and got the app up and running
 ### from a local perspective. In the end, we did everything, that as a group we could think of, to push a finished product
 ### to the front end so that we could connect ALL the dots but were unable to figure out the pickling issue we kept encountering.
 
 ### This was a massive project and I absolutely enjoyed working with Sam and Rourke. If we had one more day, I know we could have 
 ### finished this with no issues. There were a ton of man hours that went into this. I am proud of the work that I did in helping
 ### create routes that were needed, creating and deploying a heroku app, and making sure that all the i's were dotted and that the 
 ### t's were crossed.
 
  
  

>>>>>>> 8fb7dad05b1700fa8a6399e0042e7d55aca28769
