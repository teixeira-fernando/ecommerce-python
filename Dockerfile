# Python base image
FROM python:3.10-slim

WORKDIR /app

COPY pyproject.toml .
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY . .

CMD ["python", "-m", "src.ecommerce"]
