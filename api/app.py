from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import config.config as config
import config.model as model

# Define FastAPI app
app = FastAPI()

# Load configuration and initialize the model
def initialize():
    config.initialize_config_file()
    model.initialize_model()

@app.on_event("startup")
async def on_startup():
    initialize()

@app.post("/predict/")
async def predict(request: dict[str, int]):
    # Convert request data to DataFrame
    new_data = pd.DataFrame([request])

    try:
        # Perform prediction
        prediction = model.clf.predict(new_data)
        prediction_proba = model.clf.predict_proba(new_data)

        # Return results
        return {
            "prediction": True if prediction[0] == 1 else False,
            "compromised_probability": f"{prediction_proba[0][1]:.2f}",
            "uncompromised_probability": f"{prediction_proba[0][0]:.2f}"
        }

    except Exception as e:
        # Raise HTTP Exception with error details
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def read_root():
    return {"message": "It works!"}
