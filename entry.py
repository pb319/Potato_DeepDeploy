from fastapi import FastAPI
from enum import Enum
app = FastAPI()

# Creating First Enrty Point
# @app.get("/hello/{name}")
# async def hello(name):
#     return f"Hi {name}, Welcome to FatAPI"

class AvailableCuisines(str,Enum):
    x = "indian"
    y = "american"
    z = "italian"

food_items = {"indian":["Somosa","Dosa"],
              "american":["Hot Dog","apple Pie"],
              "italian": ["Pizza","Sussie"]}


# Creating DictionaryEntry Points
@app.get("/get_items/{cuisine}")
async def get_items(cuisine: AvailableCuisines):
    return food_items.get(cuisine)

