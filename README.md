# my-fastapi-app

このプロジェクトは、FastAPI を使用して構築されたシンプルなウェブアプリケーションです。

## セットアップ方法

```shell
uv sync
```

## 使用方法

アプリケーションを起動するには、以下のコマンドを実行します。

```
uv run uvicorn app.main:app --reload
```

ブラウザで `http://127.0.0.1:8000` にアクセスすると、アプリケーションが表示されます。

## API エンドポイント

- `/`: アプリケーションのルートエンドポイントです。
- `/docs`: 自動生成された API ドキュメントにアクセスできます。

## ライセンス

このプロジェクトは MIT ライセンスの下で提供されています。

## 開発方法

```shell
# ビルド
docker compose build
# 起動
docker compose up
# 削除
docker compose down

# Dockerを使わずにAPIを起動
uv run uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload
```
