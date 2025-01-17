import requests

# Define the URL and headers
url = 'https://openapi.api.govee.com/router/api/v1/device/control'
headers = {
    'Content-Type': 'application/json',
    'Govee-API-Key': 'c25ced64-9a33-4f9e-be3b-1232bd592045'
}

# Define the payload for controlling work mode
payload = {
    "requestId": "1",
    "payload": {
        "sku": "H7141",
        "device": "22:93:D4:AD:FC:FB:D4:49",
        "capability": {
            "type": "devices.capabilities.work_mode",
            "instance": "workMode",
            "value": {
                "workMode": 1,
                "modeValue": 1
            }
        }
    }
}

# Make the POST request
response = requests.post(url, headers=headers, json=payload)

# Print the response
print(response.status_code)
print(response.json())
###set mode 1 to 8 , level of humidity