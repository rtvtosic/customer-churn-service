import uvicorn
import pandas as pd

from fastapi import FastAPI

from user_data import UserData
from ml_model import load_model


app = FastAPI()

@app.post("/predict/")
def predict_churn(user_data: UserData):
    # загрузка файла с моделью и пайплайном обработки данных
    model = load_model()
    data = pd.DataFrame([user_data.model_dump(by_alias=True)])

    proba = model.predict_proba(data)[:, 1][0]
    return {"churn_proba": round(proba, 2)}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
