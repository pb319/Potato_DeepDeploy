from fastapi import FastAPI, File, UploadFile
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf


MODEL = tf.keras.models.load_model("/home/prasun/GitDemo/Potato_DeepDeploy/1.keras")
CLASS_NAMES = ['Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy']

#Instantiating Class 
app = FastAPI()
endpoint = "http://localhost:8501/v1/models/potato_models/"

@app.get("/ping")
async def ping():
    return "FastApi Server Running"

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    
    #Reading The File
    image = read_file_as_image(await file.read())
    image_batch = np.expand_dims(image,0)
    predictions = MODEL.predict(image_batch)
    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])

    return {
        "predicted_class": predicted_class,
        # "confidence": float(confidence)
    }
  

if __name__ == "__main__":
    uvicorn.run(app, host = "localhost", port = 8000)
