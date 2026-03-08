# Trade Opportunities API

This project is a FastAPI-based API that provides market research and trade opportunity insights.

It allows users to retrieve trade opportunity data through REST API endpoints.

## Tech Stack

- Python
- FastAPI
- Uvicorn

## Installation

Clone the repository:

git clone https://github.com/sindhukuppili777/trade_opportunities_api-.git

Navigate to the project folder:

cd trade_opportunities_api-

Install dependencies:

pip install -r requirements.txt

## Run the Application

Start the server using:

uvicorn main:app --reload

The server will start at:

http://127.0.0.1:8000

## API Documentation

FastAPI automatically provides API documentation.

Swagger UI:
http://127.0.0.1:8000/docs

ReDoc:
http://127.0.0.1:8000/redoc

## Authentication

The API uses a simple authorization header.

Example header:

Authorization: secret123

The API will work when this header is included in the request.

## Project Structure

trade_opportunities_api-
│
├── main.py
├── requirements.txt
└── README.md

## Author

Sindhu