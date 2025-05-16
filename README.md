 # SecureGateway

A production-ready, secure payment tokenization microservice built with FastAPI. This project simulates how a modern fintech service (like Stripe or VGS) handles sensitive cardholder data using encryption, identity-based access control, and API design best practices.

## Features

- Tokenizes sensitive credit card data using UUIDs and Fernet encryption
- Stores encrypted data securely in a PostgreSQL database hosted on GCP Cloud SQL
- Role-based access control via JWT and FastAPI’s dependency injection
- Real-time Prometheus metrics and JSON-structured logging for observability
- Fully tested with Pytest and automated CI/CD pipeline using GitHub Actions

## Tech Stack

- FastAPI & Uvicorn (API framework)
- PostgreSQL (database)
- SQLAlchemy (ORM)
- cryptography (Fernet encryption)
- PyJWT (authentication)
- Prometheus + prometheus-fastapi-instrumentator (metrics)
- Pytest (unit testing)
- GitHub Actions (CI/CD)
- Docker (optional containerization)

## Folder Structure
```
SecureGateway/
│
├── app/
│ ├── main.py # Entry point for FastAPI app
│ ├── models/ # Pydantic request schemas and SQLAlchemy models
│ ├── routes/ # API endpoints
│ ├── services/ # Business logic (tokenization, auth)
│ ├── database/ # DB connection and session
│ ├── logging_config.py # JSON logger config
│
├── tests/ # Pytest test cases
├── scripts/ # Utility scripts (e.g., create_tables.py)
├── requirements.txt # Python dependencies
├── .env # Environment variables (not committed)
├── .github/workflows/ # GitHub Actions CI/CD config
└── README.md
```


## 🔐 Security

- All card data is encrypted at rest using Fernet symmetric encryption.
- Only authenticated users with the "processor" role can access the /tokenize route.
- JWT tokens are expected in the Authorization: Bearer <token> header.

Example JWT Payload:

```
json
{
  "sub": "user-123",
  "role": "processor",
  "exp": 1714000000
}
```

## Running Tests

Make sure you have Python 3.11+ installed.

1. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Run tests:
```
pytest -v
```

## CI/CD

All pushes to main trigger GitHub Actions to:

Install dependencies

Lint and run tests

Fail the build if tests or formatting fail

See .github/workflows/main.yaml for details.

## Author
Jesus Gonzalez – UCSD Computer Science Undergraduate


