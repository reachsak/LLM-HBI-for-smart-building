import requests

# Define the URL and headers
url = 'https://test-openapi.api.govee.com/router/api/v1/device/control'
headers = {
    'Content-Type': 'application/json',
    'Govee-API-Key': 'c25ced64-9a33-4f9e-be3b-1232bd592045'
}

# Define the payload for controlling humidity
payload = {
    "requestId": "1",
    "payload": {
        "sku": "H7141",
        "device": "22:93:D4:AD:FC:FB:D4:49",
        "capability": {
            "type": "devices.capabilities.range",
            "instance": "humidity",
            "value": 40
        }
    }
}

# Make the POST request
response = requests.post(url, headers=headers, json=payload)

# Print the response
print(response.status_code)
print(response.json())
