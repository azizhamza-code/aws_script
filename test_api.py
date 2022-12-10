import json
import requests


api_url = "https://tq0synffgb.execute-api.us-east-1.amazonaws.com"


# Define the URL of the API Gateway

# Test the DELETE /items/{id} route
response = requests.delete(f"{api_url}/items/{id}")
assert response.status_code == 200
assert response.json() == f"Deleted item {id}"

# Test the GET /items/{id} route
response = requests.get(f"{api_url}/items/{id}")
assert response.status_code == 200
assert response.json() == {
    "id": id,
    "price": 12345,
    "name": "myitem"
}

# Test the GET /items route
response = requests.get(f"{api_url}/items")
assert response.status_code == 200
assert response.json() == [{
    "id": id,
    "price": 12345,
    "name": "myitem"
}]

# Test the PUT /items route
response = requests.put(f"{api_url}/items", json={
    "id": id,
    "price": 12345,
    "name": "myitem"
})
assert response.status_code == 200
assert response.json() == f"Put item {id}"