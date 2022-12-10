import json
import requests


api_url = "https://tq0synffgb.execute-api.us-east-1.amazonaws.com"
id = "12345"


# Test the PUT /items route
response = requests.put(f"{api_url}/items", json={
    "id": id,
    "price": 12345,
    "name": "myitem"
})
print(f"PUT /items: {response.status_code}")

# Test the GET /items/{id} route
response = requests.get(f"{api_url}/items/{id}")
print(f"GET /items/{{id}}: {response.status_code}")


# Test the GET /items route
response = requests.get(f"{api_url}/items")
print(f"GET /items: {response.status_code}")


# Test the DELETE /items/{id} route
response = requests.delete(f"{api_url}/items/{id}")
print(f"DELETE /items/{{id}}: {response.status_code}")



