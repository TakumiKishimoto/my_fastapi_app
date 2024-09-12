# Iris予測API

このAPIは、Irisの花の特徴量に基づいてその種類を予測します。事前に学習されたRandomForestモデルを使用しています。

## プロジェクト構成

```
├── models/
│   └── iris_model.pkl  # 学習済みのRandomForestモデル
├── main.py             # FastAPIアプリケーションのメインスクリプト
├── pyproject.toml      # Poetryによる依存関係管理ファイル
├── poetry.lock         # Poetryのロックファイル
└── README.md           # このREADMEファイル
```

## インストール手順

1. リポジトリをクローンします。

    ```bash
    git clone <リポジトリURL>
    cd <プロジェクトディレクトリ>
    ```

2. Poetryを使用して依存関係をインストールします。

    ```bash
    poetry install
    ```

3. 仮想環境に入ります。

    ```bash
    poetry shell
    ```

## APIの使用方法

1. アプリケーションを起動します。

    ```bash
    uvicorn main:app --reload
    ```

2. ブラウザまたはPostmanなどのツールを使用して、以下のエンドポイントにアクセスします。

### `POST /predict/`

Irisの特徴量を入力し、予測を行います。

#### リクエストフォーマット

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

#### レスポンスフォーマット

```json
{
  "prediction": "setosa",
  "prediction_proba": [0.9, 0.05, 0.05],
  "feature_importances": [0.25, 0.1, 0.4, 0.25]
}
```

## モデルについて

このプロジェクトでは、`iris_model.pkl`として保存された学習済みのRandomForestモデルを使用しています。