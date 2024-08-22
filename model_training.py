# model_training.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

# データの読み込み
df = pd.read_csv("./data/iris.csv")
X = df.drop("variety", axis=1)
y = df["variety"]

# データの分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# モデルのトレーニング
model = RandomForestClassifier()
model.fit(X_train, y_train)

# テストデータでの予測
y_pred = model.predict(X_test)

# 結果の表示
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# モデルの保存
joblib.dump(model, "./models/iris_model.pkl")
