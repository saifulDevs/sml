import pickle
import numpy as np
# Load the model
with open("app/model.pkl", "rb") as f:
   model = pickle.load(f)
# Make Predictions
def make_prediction(data):
   arr = np.array(data).reshape(1, -1)  # Reshape input to 2D
   return int(model.predict(arr)[0])  #Return the predicted flower