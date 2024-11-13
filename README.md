# Forex Forecast API

## Overview

The **Forex Forecast API** is a FastAPI application designed to provide accurate forex forecasting using machine learning models. The API leverages a trained LSTM (Long Short-Term Memory) model to predict future forex rates based on historical data. It is deployed on Heroku using Docker for containerization.

- 🌐 **Live Deployment**: [Forex Forecast API](https://forex-forecast-fde2872e4c4d.herokuapp.com/)

---

## Features

- 📈 **Forex Rate Prediction**: Predict forex rates using an advanced LSTM model.
- 🔍 **Interactive API Documentation**: Explore and test the API endpoints using Swagger UI at `/docs` and ReDoc at `/redoc`.
- ⚡ **Fast and Scalable**: Built with FastAPI, ensuring high performance and scalability.
- 🐳 **Containerized Deployment**: Deployed as a Docker container on Heroku for ease of scaling and portability.

---

## API Endpoints

### **Base URL**: [`https://<your-heroku-app>.herokuapp.com`](https://<your-heroku-app>.herokuapp.com)

| Method | Endpoint      | Description                          |
|--------|---------------|--------------------------------------|
| POST   | `/predict`    | Predict future forex rates.          |
| GET    | `/docs`       | Swagger UI for interactive API docs. |
| GET    | `/redoc`      | ReDoc for API documentation.         |

### Request Example for `/predict`

```json
{
  "data": [
    [0.1, 0.2, 0.3, ..., 0.21],  // 1st time step
    [0.3, 0.4, 0.5, ..., 0.21],  // 2nd time step
    // ... 10 time steps in total
  ]
}
```

### Response Example
{
  "forecast": 1.2345
}


### Project Structure

project/
├── app/
│   ├── main.py            # Entry point for the FastAPI app
│   ├── utils/
│   │   └── preprocess.py  # Preprocessing logic for input data
│   ├── models/
│   │   └── lstm_model.h5  # Pretrained LSTM model
├── Dockerfile             # Docker configuration
├── requirements.txt       # Python dependencies
└── Procfile               # Heroku process definition

