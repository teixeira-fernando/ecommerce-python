# Ecommerce Python Application

This is a practice ecommerce application built in Python to learn and experiment with Python project structure, testing, and packaging.

## Features
- Modular folder structure (products, users, orders, cart, payments)
- Poetry for dependency management
- Dockerfile for containerization
- Initial code and unit tests for each module

## Getting Started

### Requirements
- Python 3.10+
- Poetry
- Docker (optional)

### Install dependencies
```
poetry install
```

### Run tests
```
poetry run pytest
```

### Run the app
```
poetry run python -m src.ecommerce
```

### Build and run with Docker
```
docker build -t ecommerce-python .
docker run --rm ecommerce-python
```

## Project Structure
```
src/ecommerce/app/products/   # Product logic
src/ecommerce/app/users/      # User logic
src/ecommerce/app/orders/     # Order logic
src/ecommerce/app/cart/       # Cart logic
src/ecommerce/app/payments/   # Payment logic
tests/                        # Unit tests
``
