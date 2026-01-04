- Curl commands to test FAST API app

curl "http://localhost:8000/convert?from_currency=USD&to_currency=EUR&amount=100"
curl "http://localhost:8000/convert?from_currency=EUR&to_currency=USD&amount=50"

Test Error - 
curl "http://localhost:8000/convert?from_currency=GBP&to_currency=USD&amount=100"