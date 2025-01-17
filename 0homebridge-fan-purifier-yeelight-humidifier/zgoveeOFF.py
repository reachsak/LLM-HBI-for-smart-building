import requests
import uuid

# Define the URL and headers
url = 'https://openapi.api.govee.com/router/api/v1/device/control'
headers = {
    'Content-Type': 'application/json',
    'Govee-API-Key': 'c25ced64-9a33-4f9e-be3b-1232bd592045'
}

# Define the payload
payload = {
    "requestId": str(uuid.uuid4()),  # Generate a unique UUID for the request
    "payload": {
        "sku": "H7141",
        "device": "22:93:D4:AD:FC:FB:D4:49",
        "capability": {
            "type": "devices.capabilities.on_off",
            "instance": "powerSwitch",
            "value": 0  # Change to 1 to turn on
        }
    }
}

# Make the POST request
response = requests.post(url, headers=headers, json=payload)

# Print the response
print(response.status_code)
print(response.json())
