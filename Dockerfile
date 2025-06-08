FROM python:3.10-slim-bookworm

WORKDIR /home

COPY pyproject.toml .

RUN pip install --no-cache-dir uv \
    && uv pip install --system --no-cache-dir -r pyproject.toml

COPY ./app /home/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
