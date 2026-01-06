# Python base image
FROM python:3.10-slim

WORKDIR /app

COPY pyproject.toml .
COPY . .
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

CMD ["python", "-m", "src.ecommerce"]
