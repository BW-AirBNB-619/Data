import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
import category_encoders as ce
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("AB_NYC_2019.csv")

def accum(neighbourhood_group,
          neighbourhood,
          latitude,	
          longitude, 
          room_type,	
          minimum_nights,	
          number_of_reviews,	
          calculated_host_listings_count,	
          availability_365, 
          df):

    """
    Aggregates information the model will run predictions
    on into a Pandas DataFrame for use in the predict function.
    """

    data = {"neighbourhood_group": neighbourhood_group,
            "neighbourhood": neighbourhood,
            "latitude": latitude,
            "longitude": longitude,
            "room_type": room_type,
            "minimum_nights": minimum_nights,
            "number_of_reviews": number_of_reviews,
            "calculated_host_listings_count": calculated_host_listings_count,
            "availability_365": availability_365}
    
    # Info DataFrame
    info = pd.DataFrame(data, index=[0])

    # Append
    new_df = pd.concat([df, info], axis=0)
    
    return new_df


def preprocessing(df):
  """
  Preprocesses the data.

  Input: DataFrame

  Output: X_train, X_test, y_train, y_test
  """
  # Copying DF
  dfx = df.copy()

  ## EDA
  # Dropping Columns
  dfx.drop(columns=["host_name", "last_review", "reviews_per_month"], inplace = True)

  # Removing -- Custom Outliers
  dfx = dfx[(dfx["price"] > 0) & 
            (dfx["price"] < 10000)]
  
  # New Column -- 'log_price'
  dfx["log_price"] = np.log(dfx["price"].values)


  # Target and Features
  target = "log_price"
  features = ["neighbourhood_group",
              "neighbourhood",
              "latitude",
              "longitude",
              "room_type",
              "minimum_nights",
              "number_of_reviews",
              "calculated_host_listings_count",
              "availability_365"]
  
  # X Features Matrix
  X = dfx[features]

  # y taregt vector
  y = dfx[target]
  
  # Mapping - 'room_type'
  room_type_dict = {"Shared room":1, "Private room":2, "Entire home/apt":3}
  X.iloc[:, 4].map(room_type_dict)


  # Train Test Split
  X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                      test_size=.2,
                                                      random_state=42)

  # Preprocess Pipeline -- OrdinalEncoder and StandardScaler
  preprocess = make_pipeline(
      ce.OrdinalEncoder(),
      StandardScaler()
  )

  # Fit Transform and Transform Training and Testing Data
  X_train = preprocess.fit_transform(X_train)
  X_test = preprocess.transform(X_test)

  # Create DataFrame for X Matrices
  X_train_df = pd.DataFrame(X_train, columns=features) 
  X_test_df = pd.DataFrame(X_test, columns=features)

  # Return
  return X_train, y_train


# Unused functions

def predict(X_train, model):
  """
  Creates training predictions according the pickled model
  which is fed into it.
  """

# Training Prediction
  train_pred = model.predict([X_train[-1]])

  return np.exp(train_pred)


def rfr_function(X_train, y_train):
  
  # Instantiate Model
  rfr = RandomForestRegressor()
  
  # Fit
  model = rfr.fit(X_train[:-1], y_train[:-1])
  
  # # Training Prediction
  # train_pred = rfr.predict([X_train[-1]])

  # Return: np.exp(train_pred)
  return model


def df_maker(y_vector, y_pred_vector):
  
  # Training Data
  log_price = pd.DataFrame(y_vector, columns=["log_price"])
  log_price_pred = pd.DataFrame(y_pred_vector, columns=["log_price_pred"])

  unlog_price = np.exp(log_price.values)
  unlog_price = pd.DataFrame(unlog_price, columns=["unlog_price"])

  unlog_pred_price = np.exp(log_price_pred.values)
  unlog_pred_price = pd.DataFrame(unlog_pred_price, columns=["unlog_pred_price"])


  df_logs = pd.concat([log_price, log_price_pred, unlog_price, unlog_pred_price], 
                       axis=1)
  
  return df_logs