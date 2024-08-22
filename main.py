from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

# FastAPIのインスタンスを作成
app = FastAPI()

# モデルのロード
model = joblib.load("./models/iris_model.pkl")

# 入力データのスキーマを定義
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# 推論エンドポイントを作成
@app.post("/predict/")
def predict(input_data: IrisInput):
    data = np.array([[input_data.sepal_length, input_data.sepal_width,
                      input_data.petal_length, input_data.petal_width]])
    
    # 予測
    prediction = model.predict(data)
    prediction_proba = model.predict_proba(data)
    
    # 特徴量の重要度
    feature_importances = model.feature_importances_
    
    return {
        "prediction": prediction[0],
        "prediction_proba": prediction_proba[0].tolist(),
        "feature_importances": feature_importances.tolist()
    }

