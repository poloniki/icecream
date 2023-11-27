from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hellow_world():
    return {"greeting": "Hi!!"}


@app.get("/predict")
def predict(temp: int = 1, num: int = 2):
    prediction = round(10 + int(temp) * 1.5 + int(num) * 0.4)
    return {"prediction": prediction}
