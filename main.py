from fastapi import FastAPI, HTTPException
import numpy as np
import tensorflow as tf
from pydantic import BaseModel, conlist
from utils.preprocess import preprocess_input


app = FastAPI()

model = tf.keras.models.load_model('models/model3.h5')



class ForexInput(BaseModel):
    data: conlist(conlist(float, min_length=21, max_length=21), min_length=10, max_length=10) # type: ignore



@app.post("/predict")
async def predict(forex_input: ForexInput):
    try:
        # Preprocess the input data
        processed_data = preprocess_input(forex_input.data)
        
        # Make prediction 
        prediction = model.predict(processed_data)
        
        # Extract and return the forecasted value
        forecast = float(prediction[0][0])
        return {"forecast": forecast}
    
    except ValueError as e:
        return {"detail": str(e)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

     