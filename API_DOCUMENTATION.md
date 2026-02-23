# API REST Documentation - Brazilian Wage Forecasting

## Overview

RESTful API providing wage projections for Brazil based on macroeconomic parameters.

**Base URL:** `http://localhost:5000/api` (local) or `https://your-domain.com/api` (production)

**Version:** 1.0.0  
**Author:** Vitor Ramos dos Santos  
**License:** MIT

---

## Authentication

Currently, no authentication required. API is publicly accessible.

---

## Endpoints

### 1. Health Check

**GET** `/api/health`

Check if API is running.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2026-02-19T10:30:00",
  "version": "1.0.0"
}
```

---

### 2. Get Historical Data

**GET** `/api/data/historical`

Retrieve historical wage data for Brazil (2012-2025).

**Query Parameters:**
- `start_year` (optional): Filter from year (integer)
- `end_year` (optional): Filter to year (integer)

**Example Request:**
```bash
curl "http://localhost:5000/api/data/historical?start_year=2020"
```

**Response:**
```json
{
  "data": [
    {
      "ano": 2020,
      "rendimento_real": 3226,
      "horas_semanais": 40.0,
      "rendimento_hora": 18.63
    },
    ...
  ],
  "count": 5
}
```

---

### 3. Predict Wage for Scenario

**POST** `/api/predict/scenario`

Calculate projected 2026 wage based on economic parameters.

**Request Body:**
```json
{
  "desemprego": 7.0,
  "pib": 2.0,
  "inflacao": 5.5,
  "sm_real": 2.0
}
```

**Parameters:**
- `desemprego` (float, required): Unemployment rate (5-15%)
- `pib` (float, required): GDP growth (-2 to 5%)
- `inflacao` (float, required): Inflation rate (3-10%)
- `sm_real` (float, required): Real minimum wage gain (0-5%)

**Example Request:**
```bash
curl -X POST http://localhost:5000/api/predict/scenario \
  -H "Content-Type: application/json" \
  -d '{
    "desemprego": 8.0,
    "pib": 1.5,
    "inflacao": 6.0,
    "sm_real": 1.5
  }'
```

**Response:**
```json
{
  "salario_projetado": 902.45,
  "variacao_vs_2024_pct": -2.96,
  "decomposicao": {
    "desemprego_pp": -2.80,
    "pib_pp": 0.45,
    "salario_minimo_pp": 0.60,
    "inflacao_pp": -1.50
  },
  "parametros": {
    "desemprego": 8.0,
    "pib": 1.5,
    "inflacao": 6.0,
    "sm_real": 1.5
  }
}
```

---

### 4. Run Monte Carlo Simulation

**POST** `/api/predict/monte_carlo`

Run probabilistic simulation with multiple scenarios.

**Request Body:**
```json
{
  "n_simulacoes": 1000,
  "parametros": {
    "desemprego_media": 7.5,
    "desemprego_std": 1.5,
    "pib_media": 2.0,
    "pib_std": 1.0,
    "inflacao_media": 5.5,
    "inflacao_std": 1.0,
    "sm_real_media": 2.0,
    "sm_real_std": 0.8
  }
}
```

**Parameters:**
- `n_simulacoes` (int, optional): Number of simulations (default: 1000, max: 10000)
- `parametros` (object, optional): Distribution parameters for each economic variable

**Example Request:**
```bash
curl -X POST http://localhost:5000/api/predict/monte_carlo \
  -H "Content-Type: application/json" \
  -d '{
    "n_simulacoes": 5000
  }'
```

**Response:**
```json
{
  "n_simulacoes": 5000,
  "estatisticas": {
    "media": 914.52,
    "mediana": 913.20,
    "desvio_padrao": 28.35,
    "p5": 870.45,
    "p95": 960.18,
    "prob_queda_pct": 48.5,
    "prob_ganho_pct": 51.5,
    "prob_queda_5pct_pct": 18.2
  },
  "parametros_utilizados": {
    "desemprego": {"media": 7.5, "std": 1.5},
    "pib": {"media": 2.0, "std": 1.0},
    "inflacao": {"media": 5.5, "std": 1.0},
    "sm_real": {"media": 2.0, "std": 0.8}
  }
}
```

---

### 5. Get Stress Test Results

**GET** `/api/scenarios/stress_test`

Retrieve pre-computed extreme scenario results.

**Example Request:**
```bash
curl http://localhost:5000/api/scenarios/stress_test
```

**Response:**
```json
{
  "scenarios": [
    {
      "Cenario": "Crise Severa",
      "Salario": 827.45,
      "Variacao_pct": -11.1,
      "Desemprego": 12.0,
      "PIB": -2.0,
      "Inflacao": 8.0
    },
    ...
  ],
  "count": 4
}
```

---

### 6. API Information

**GET** `/api/info`

Get API metadata and model parameters.

**Response:**
```json
{
  "name": "Brazil Wage Forecasting API",
  "version": "1.0.0",
  "author": "Vitor Ramos dos Santos",
  "description": "REST API for wage projections based on macroeconomic parameters",
  "endpoints": {
    "/api/health": "Health check",
    "/api/data/historical": "Get historical wage data",
    "/api/predict/scenario": "Predict wage for given scenario (POST)",
    "/api/predict/monte_carlo": "Run Monte Carlo simulation (POST)",
    "/api/scenarios/stress_test": "Get stress test scenarios",
    "/api/info": "This endpoint"
  },
  "model_parameters": {
    "base_2024": 930,
    "elasticity_unemployment": -2.0,
    "elasticity_gdp": 0.3,
    "elasticity_minimum_wage": 0.4,
    "elasticity_inflation": -0.5
  }
}
```

---

## Error Handling

All endpoints return appropriate HTTP status codes:

- `200 OK`: Successful request
- `400 Bad Request`: Invalid parameters
- `404 Not Found`: Endpoint does not exist
- `500 Internal Server Error`: Server error

**Error Response Format:**
```json
{
  "error": "Description of error"
}
```

---

## Running the API Locally

### Requirements

```bash
pip install flask flask-cors pandas numpy
```

### Start Server

```bash
cd scripts
python api_rest.py
```

Server will start on `http://localhost:5000`

---

## Deployment

### Option 1: Heroku

1. Create `Procfile`:
```
web: python scripts/api_rest.py
```

2. Deploy:
```bash
git add .
git commit -m "Add API"
git push heroku main
```

### Option 2: AWS Lambda

Use AWS API Gateway + Lambda with Zappa:

```bash
pip install zappa
zappa init
zappa deploy production
```

### Option 3: Docker

Create `Dockerfile`:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "scripts/api_rest.py"]
```

Build and run:
```bash
docker build -t wage-api .
docker run -p 5000:5000 wage-api
```

---

## Rate Limiting

Currently no rate limiting. For production, implement:
- Flask-Limiter (Python)
- Nginx rate limiting (reverse proxy)
- API Gateway limits (AWS)

Recommended: 100 requests/minute per IP

---

## CORS Configuration

API allows cross-origin requests from any domain.

For production, restrict to specific domains in `api_rest.py`:

```python
CORS(app, resources={r"/api/*": {"origins": "https://yourdomain.com"}})
```

---

## Model Details

### Wage Projection Formula

```
Projected_Wage = Base_2024 × (1 + Total_Impact/100)

Where:
Total_Impact = 
    -2.0 × (Unemployment - 6.6) +
     0.3 × GDP_Growth +
     0.4 × Min_Wage_Gain +
    -0.5 × (Inflation - 3.0)
```

### Elasticities

Based on regression analysis of historical data (2012-2024):

- **Unemployment:** -2.0 (each 1pp increase → 2% wage decrease)
- **GDP:** 0.3 (each 1% GDP growth → 0.3% wage increase)
- **Minimum Wage:** 0.4 (40% pass-through to median wage)
- **Inflation:** -0.5 (inflation above 3% erodes real gains)

---

## Examples

### Python

```python
import requests

# Single scenario
response = requests.post('http://localhost:5000/api/predict/scenario', json={
    'desemprego': 8.0,
    'pib': 2.0,
    'inflacao': 6.0,
    'sm_real': 2.0
})

result = response.json()
print(f"Projected wage: R$ {result['salario_projetado']:.2f}")
```

### JavaScript

```javascript
fetch('http://localhost:5000/api/predict/scenario', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({
    desemprego: 8.0,
    pib: 2.0,
    inflacao: 6.0,
    sm_real: 2.0
  })
})
.then(res => res.json())
.then(data => console.log(`Projected wage: R$ ${data.salario_projetado.toFixed(2)}`));
```

### cURL

```bash
# Health check
curl http://localhost:5000/api/health

# Get historical data
curl "http://localhost:5000/api/data/historical?start_year=2020"

# Predict scenario
curl -X POST http://localhost:5000/api/predict/scenario \
  -H "Content-Type: application/json" \
  -d '{"desemprego": 8.0, "pib": 2.0, "inflacao": 6.0, "sm_real": 2.0}'

# Monte Carlo
curl -X POST http://localhost:5000/api/predict/monte_carlo \
  -H "Content-Type: application/json" \
  -d '{"n_simulacoes": 1000}'
```

---

## Support

For issues or questions:
- Email: vitorramossantos8@gmail.com
- GitHub: [Repository Issues](https://github.com/Vitor2316/Projeto-analise-de-dados-Brasil/issues)

---

## Changelog

**v1.0.0 (2026-02-19)**
- Initial release
- All endpoints operational
- Model validated against historical data

---

## License

MIT License - See LICENSE file for details

