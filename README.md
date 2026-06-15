# Partial Fraction Calculator API

A simple Flask API to calculate the value of `f(r) = 4 / ((r-1)(r+3))`.

This project was built for learning GitHub, Flask, and basic API error handling.

## How to Run
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `python app.py`
4. Open browser: `http://127.0.0.1:5000/calculate?r=5`

## API Endpoint
`GET /calculate?r=<integer>`

**Example Request:**
`/calculate?r=5`

**Example Success Response:**
```json
{
  "r": 5,
  "f(r)": 0.25
}
```

**Example Error Response:**
```json
{
  "error": "Division by zero: r cannot be 1 or -3"
}
```

## Tech Stack
- Python
- Flask

## Examples Added by mystery girl
1. Example 1: (x+1)/(x^2-1) 
2. Example 2: 1/(x(x+1))
