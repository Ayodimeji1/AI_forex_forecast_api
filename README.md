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
```
{
  "forecast": 1.2345
}
```

### Project Structure
```
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
```
### Installation and Usage

Prerequisites
Python 3.9+
Docker
Heroku CLI

### Local development
**1. Clone the repository**
```
git clone https://github.com/your-username/forex-forecast-api.git
cd forex-forecast-api
```
**2. Create virtual Environment and Install Dependencies**
```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
**3. Run the FastAPI app:**
```
uvicorn app.main:app --reload

```
**4. Access the API:**
```
Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
```
### Docker Deployment
**1. Build the Docker image:**
```
docker build -t forex-forecast .
```
**2. Run the Docker container:**
```
docker run -p 8000:8000 forex-forecast
```
### Deploy to Heroku
1. Log in to Heroku and set up the app:
```
heroku login
heroku create forex-forecast --stack=container

```
### Push the Docker image to Heroku:
```
heroku container:push web -a forex-forecast
heroku container:release web -a forex-forecast
```

### Open the app:
```
heroku open -a forex-forecast
```
**Deployed URL: https://forex-forecast-fde2872e4c4d.herokuapp.com/**

### Technologies Used
**Python**: Core programming language.
**FastAPI**: Framework for building the API.
**TensorFlow**: Machine learning library for LSTM model.
**Docker**: Containerization for deployment.
**Heroku**: Cloud platform for hosting.

### Contributing
1. Fork the repository.
2. Create a new branch:
```
git checkout -b feature-name
```
3. Commit changes:
```
git commit -m "Add new feature"
```
4. Push to the branch:
```
git push origin feature-name
```
5. Open a pull request.

### License
This project is licensed under the MIT License. See the LICENSE file for details.
