- Seed database with exchange rates
uv run seed_rates.py

- Curl commands to test FAST API app

curl "http://localhost:8000/convert?from_currency=USD&to_currency=EUR&amount=100"

curl "http://localhost:8000/convert?from_currency=EUR&to_currency=USD&amount=50"

curl "http://localhost:8000/convert?from_currency=USD&to_currency=JPY&amount=1000"

Test Error - 
-- Currency code too short (must be 3 chars)
curl "http://localhost:8000/convert?from_currency=US&to_currency=EUR&amount=100"

-- Amount must be > 0
  curl "http://localhost:8000/convert?from_currency=USD&to_currency=EUR&amount=-50"

-- Missing required parameter
curl "http://localhost:8000/convert?from_currency=USD&to_currency=EUR"