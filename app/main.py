from fastapi import FastAPI, Depends
from app.predict import make_prediction
from app.jwt import verify_token, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from app.rate_limit import RateLimitMiddleware
from app.validation import PredictionInput
from datetime import timedelta

# Initialize FastAPI app
app = FastAPI()



#Skip this route if you are not implementing step 5
# Add rate limiting middleware to limit requests to 5 per minute
app.add_middleware(RateLimitMiddleware, throttle_rate=5)

# Root endpoint to confirm the API is running
@app.get("/")
def root():
    return {"message": "Welcome to the Secure Machine Learning API"}
#Skip this route if you are not implementing step 4
# This endpoint issues a token when valid credentials are provided
@app.post("/token")
def login():
    # Define the expiration time for the token (e.g., 30 minutes)
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)    
    # Generate the JWT token
    access_token = create_access_token(data={"sub": "user"}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}
# Prediction endpoint, requires a valid JWT token for authentication
# Additionally, the input data is validated using the PredictionInput model
@app.post("/predict")
def predict(input_data: PredictionInput, token: str = Depends(verify_token)):
    prediction = make_prediction(input_data.data)
    return {"prediction": prediction}