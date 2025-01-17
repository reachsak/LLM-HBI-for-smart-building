
buildingautomationcontractabi = [ { "anonymous": False, "inputs": [ { "indexed": False, "internalType": "uint256", "name": "maxCO2Level", "type": "uint256" } ], "name": "MaxCO2LevelUpdated", "type": "event" }, { "anonymous": False, "inputs": [ { "indexed": False, "internalType": "uint256", "name": "maxHumidity", "type": "uint256" } ], "name": "MaxHumidityUpdated", "type": "event" }, { "anonymous": False, "inputs": [ { "indexed": False, "internalType": "uint256", "name": "maxLuxLevel", "type": "uint256" } ], "name": "MaxLuxLevelUpdated", "type": "event" }, { "anonymous": False, "inputs": [ { "indexed": False, "internalType": "int256", "name": "maxTemperature", "type": "int256" } ], "name": "MaxTemperatureUpdated", "type": "event" }, { "anonymous": False, "inputs": [ { "indexed": False, "internalType": "uint256", "name": "minCO2Level", "type": "uint256" } ], "name": "MinCO2LevelUpdated", "type": "event" }, { "anonymous": False, "inputs": [ { "indexed": False, "internalType": "uint256", "name": "minHumidity", "type": "uint256" } ], "name": "MinHumidityUpdated", "type": "event" }, { "anonymous": False, "inputs": [ { "indexed": False, "internalType": "uint256", "name": "minLuxLevel", "type": "uint256" } ], "name": "MinLuxLevelUpdated", "type": "event" }, { "anonymous": False, "inputs": [ { "indexed": False, "internalType": "int256", "name": "minTemperature", "type": "int256" } ], "name": "MinTemperatureUpdated", "type": "event" }, { "inputs": [], "name": "getMaxCO2Level", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "getMaxHumidity", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "getMaxLuxLevel", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "getMaxTemperature", "outputs": [ { "internalType": "int256", "name": "", "type": "int256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "getMinCO2Level", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "getMinHumidity", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "getMinLuxLevel", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "getMinTemperature", "outputs": [ { "internalType": "int256", "name": "", "type": "int256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "maxCO2Level", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "maxHumidity", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "maxLuxLevel", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "maxTemperature", "outputs": [ { "internalType": "int256", "name": "", "type": "int256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "minCO2Level", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "minHumidity", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "minLuxLevel", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "minTemperature", "outputs": [ { "internalType": "int256", "name": "", "type": "int256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "_maxCO2Level", "type": "uint256" } ], "name": "setMaxCO2Level", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "_maxHumidity", "type": "uint256" } ], "name": "setMaxHumidity", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "_maxLuxLevel", "type": "uint256" } ], "name": "setMaxLuxLevel", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "int256", "name": "_maxTemperature", "type": "int256" } ], "name": "setMaxTemperature", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "_minCO2Level", "type": "uint256" } ], "name": "setMinCO2Level", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "_minHumidity", "type": "uint256" } ], "name": "setMinHumidity", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "_minLuxLevel", "type": "uint256" } ], "name": "setMinLuxLevel", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "int256", "name": "_minTemperature", "type": "int256" } ], "name": "setMinTemperature", "outputs": [], "stateMutability": "nonpayable", "type": "function" }]
buildingautomationcontract_address = "0x02a37bB103fFb6C4b19043296b9454DcA324BaC0"
from web3 import Web3
web3 = Web3(Web3.HTTPProvider("https://sepolia.infura.io/v3/29ed729d7617400ab427b75b16c31c63"))

from flask import Flask, request, jsonify
from web3 import Web3
import requests
import json
from llama_cpp_agent.llm_agent import LlamaCppAgent
from llama_cpp_agent.providers.llama_cpp_endpoint_provider import LlamaCppEndpointSettings
from llama_cpp_agent.messages_formatter import MessagesFormatterType
from llama_cpp_agent.function_calling import LlamaCppFunctionTool
from llama_cpp_agent.gbnf_grammar_generator.gbnf_grammar_from_pydantic_models import create_dynamic_model_from_function
from flask_cors import CORS
from yeelight import Bulb
from datetime import datetime
import subprocess
import requests
import uuid
import os
import uuid
import subprocess
import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)


def set_fanspeed_humidity_airpurifier_and_light(inner_thoughts: str, fan_speed: int, purifier_speed: int, humidity_level: int, lux: int) -> str:
    """
    Set the settings for the smart fan, air purifier, humidity level, and light brightness.

    Parameters:
        inner_thoughts (str): Inner thoughts to return alongside the action.
        fan_speed (int): Speed for the smart fan (1-3).
        purifier_speed (int): Speed for the air purifier (1-14).
        humidity_level (int): Desired humidity level (0-100).
        lux (int): Brightness for the smart light (1-100%).

    Returns:
        str: A message indicating the actions taken and their results.
    """

    results = []

    # Set smart fan speed
    if fan_speed < 1 or fan_speed > 3:
        results.append(f"Invalid smart fan speed value: {fan_speed}. Please provide a value between 1 and 3.")
    else:
        try:
            result = subprocess.run(["node", "control_smart_fan_speed.js", str(fan_speed)], capture_output=True, text=True)
            if result.returncode != 0:
                results.append(f"Failed to set smart fan speed: {result.stderr}")
            else:
                results.append(f"{inner_thoughts} Smart fan speed set to {fan_speed}. Command output: {result.stdout}")
        except Exception as e:
            results.append(f"An error occurred while setting the smart fan speed: {str(e)}")

    # Set air purifier motor speed
    if purifier_speed < 1 or purifier_speed > 14:
        results.append(f"Invalid air purifier speed value: {purifier_speed}. Please provide a value between 1 and 14.")
    else:
        url = 'https://test-openapi.api.govee.com/router/api/v1/device/control'
        api_key = "c25ced64-9a33-4f9e-be3b-1232bd592045"
        
        if not api_key:
            return "API key is not set. Please check your environment variables."

        headers = {
            'Content-Type': 'application/json',
            'Govee-API-Key': api_key
        }

        payload = {
            "requestId": str(uuid.uuid4()),
            "payload": {
                "sku": "H7141",
                "device": "22:93:D4:AD:FC:FB:D4:49",
                "capability": {
                    "type": "devices.capabilities.range",
                    "instance": "fan",
                    "value": purifier_speed
                }
            }
        }

        try:
            response = requests.post(url, headers=headers, json=payload)
            if response.status_code == 200:
                results.append(f"{inner_thoughts} Air purifier motor speed set to {purifier_speed}. API Response: {response.json()}")
            else:
                results.append(f"Failed to set air purifier motor speed. Status code: {response.status_code}, Response: {response.json()}")
        except requests.exceptions.RequestException as e:
            results.append(f"An error occurred while setting air purifier motor speed: {str(e)}")

    # Set humidity level
    if not (0 <= humidity_level <= 100):
        results.append(f"{inner_thoughts} Invalid humidity value: {humidity_level}. It must be between 0 and 100.")
    else:
        url = 'https://test-openapi.api.govee.com/router/api/v1/device/control'
        api_key = "c25ced64-9a33-4f9e-be3b-1232bd592045"
        
        if not api_key:
            return "API key is not set. Please check your environment variables."

        headers = {
            'Content-Type': 'application/json',
            'Govee-API-Key': api_key
        }

        payload = {
            "requestId": str(uuid.uuid4()),
            "payload": {
                "sku": "H7141",
                "device": "22:93:D4:AD:FC:FB:D4:49",
                "capability": {
                    "type": "devices.capabilities.range",
                    "instance": "humidity",
                    "value": humidity_level
                }
            }
        }

        try:
            response = requests.post(url, headers=headers, json=payload)
            if response.status_code == 200:
                results.append(f"{inner_thoughts} Humidity set to {humidity_level}%. API Response: {response.json()}")
            else:
                results.append(f"Failed to set humidity. Status code: {response.status_code}, Response: {response.json()}")
        except requests.exceptions.RequestException as e:
            results.append(f"An error occurred while setting humidity: {str(e)}")

    # Set smart light brightness
    if not (1 <= lux <= 100):
        results.append(f"{inner_thoughts} Invalid light brightness value: {lux}. It must be between 1 and 100.")
    else:
        results.append(set_brightness_to_percentage1(inner_thoughts, lux))

    return "\n".join(results)

def set_brightness_to_percentage1(inner_thoughts: str, percentage: int) -> str:
    """
    Set the brightness of the Yeelight between 1 to 100 percent.

    Parameters:
        inner_thoughts (str): Inner thoughts to return alongside the action.
        percentage (int): Percentage of brightness to set (1-100).

    Returns:
        str: A message indicating the action taken.
    """
    bulb_ip = "192.168.31.171" 
    try:
        bulb = Bulb(bulb_ip)
        bulb.set_brightness(percentage)
        return f"{inner_thoughts} Brightness set to {percentage}%."
    except Exception as e:
        return f"An error occurred while setting brightness: {str(e)}"

def get_baseline_comfort_environmetal_condition_room():
    """
    Fetches the current min and max of baseline comfort environmetal conditon parameter including temparature, humidity, co2, lux .

    Returns:
        float: The temparature, humidity, co2, lux.
    """
    contract = web3.eth.contract(address=buildingautomationcontract_address, abi=buildingautomationcontractabi)
    min_temp = contract.functions.getMinTemperature().call()
    max_temp = contract.functions.getMaxTemperature().call()
    min_lux = contract.functions.getMinLuxLevel().call()
    max_lux = contract.functions.getMaxLuxLevel().call()
    min_co2 = contract.functions.getMinCO2Level().call()
    max_co2 = contract.functions.getMaxCO2Level().call()
    min_humidity = contract.functions.getMinHumidity().call()
    max_humidity = contract.functions.getMaxHumidity().call()
    
    return (
        f"The minimum temperature is {min_temp}°C and maximum temperature is {max_temp}°C.\n"
        f"The minimum lux level is {min_lux} lux and maximum lux level is {max_lux} lux.\n"
        f"The minimum CO2 level is {min_co2} ppm and maximum CO2 level is {max_co2} ppm.\n"
        f"The minimum humidity is {min_humidity}% and maximum humidity is {max_humidity}%."
    )

def get_room_environmetal_condition():
    """
    Fetches the current temparature, humidity, co2, luxfrom the my space.

    Returns:
        float: The current temparature, humidity, co2, lux.
    """
    api_url = "http://localhost:8000/api/sensor"
    response = requests.get(api_url)
    data = response.json()
    temperature = data['temperature']
    co2 = data['co2']
    lux = data['lux']
    humidity = data['humidity']
    return (
        f"The room temperature is {temperature}°C.\n"
        f"The CO2 level is {co2} ppm.\n"
        f"The lux level is {lux} lux.\n"
        f"The humidity is {humidity}%."
    )

def get_baseline_comfort_temperature():
    """
    Fetches the current min and max temperature .

    Returns:
        float: The current temperature.
    """
    contract = web3.eth.contract(address=buildingautomationcontract_address, abi=buildingautomationcontractabi)
    min_temp = contract.functions.getMinTemperature().call()
    max_temp = contract.functions.getMaxTemperature().call()
    return f"The min temparature is {min_temp} degree and max temparature is {max_temp }"

def get_room_temperature():
    """
    Fetches the current temperature from the my apartment.

    Returns:
        float: The current temperature.
    """
    api_url = "http://localhost:8000/api/sensor"
    response = requests.get(api_url)
    data = response.json()
    temperature = data['temperature']
    return f"The room temparature is {temperature} degree "

def set_fanspeed_humidity_and_air_purifier_device_settings(inner_thoughts: str, fan_speed: int, purifier_speed: int, humidity_level: int) -> str:
    """
    Set the settings for the smart fan, air purifier, and humidity level.

    Parameters:
        inner_thoughts (str): Inner thoughts to return alongside the action.
        fan_speed (int): Speed for the smart fan (1-3).
        purifier_speed (int): Speed for the air purifier (1-14).
        humidity_level (int): Desired humidity level (0-100).

    Returns:
        str: A message indicating the actions taken and their results.
    """

    results = []

    # Set smart fan speed
    if fan_speed < 1 or fan_speed > 3:
        results.append(f"Invalid smart fan speed value: {fan_speed}. Please provide a value between 1 and 3.")
    else:
        try:
            result = subprocess.run(["node", "control_smart_fan_speed.js", str(fan_speed)], capture_output=True, text=True)
            if result.returncode != 0:
                results.append(f"Failed to set smart fan speed: {result.stderr}")
            else:
                results.append(f"{inner_thoughts} Smart fan speed set to {fan_speed}. Command output: {result.stdout}")
        except Exception as e:
            results.append(f"An error occurred while setting the smart fan speed: {str(e)}")

    # Set air purifier motor speed
    if purifier_speed < 1 or purifier_speed > 14:
        results.append(f"Invalid air purifier speed value: {purifier_speed}. Please provide a value between 1 and 14.")
    else:
        url = 'https://test-openapi.api.govee.com/router/api/v1/device/control'
        api_key = os.getenv('c25ced64-9a33-4f9e-be3b-1232bd592045')
        
        if not api_key:
            return "API key is not set. Please check your environment variables."

        headers = {
            'Content-Type': 'application/json',
            'Govee-API-Key': api_key
        }

        payload = {
            "requestId": str(uuid.uuid4()),
            "payload": {
                "sku": "H7141",
                "device": "22:93:D4:AD:FC:FB:D4:49",
                "capability": {
                    "type": "devices.capabilities.range",
                    "instance": "fan",
                    "value": purifier_speed
                }
            }
        }

        try:
            response = requests.post(url, headers=headers, json=payload)
            if response.status_code == 200:
                results.append(f"{inner_thoughts} Air purifier motor speed set to {purifier_speed}. API Response: {response.json()}")
            else:
                results.append(f"Failed to set air purifier motor speed. Status code: {response.status_code}, Response: {response.json()}")
        except requests.exceptions.RequestException as e:
            results.append(f"An error occurred while setting air purifier motor speed: {str(e)}")

    # Set humidity level
    if not (0 <= humidity_level <= 100):
        results.append(f"{inner_thoughts} Invalid humidity value: {humidity_level}. It must be between 0 and 100.")
    else:
        url = 'https://test-openapi.api.govee.com/router/api/v1/device/control'
        api_key = os.getenv('c25ced64-9a33-4f9e-be3b-1232bd592045')
        
        if not api_key:
            return "API key is not set. Please check your environment variables."

        headers = {
            'Content-Type': 'application/json',
            'Govee-API-Key': api_key
        }

        payload = {
            "requestId": str(uuid.uuid4()),
            "payload": {
                "sku": "H7141",
                "device": "22:93:D4:AD:FC:FB:D4:49",
                "capability": {
                    "type": "devices.capabilities.range",
                    "instance": "humidity",
                    "value": humidity_level
                }
            }
        }

        try:
            response = requests.post(url, headers=headers, json=payload)
            if response.status_code == 200:
                results.append(f"{inner_thoughts} Humidity set to {humidity_level}%. API Response: {response.json()}")
            else:
                results.append(f"Failed to set humidity. Status code: {response.status_code}, Response: {response.json()}")
        except requests.exceptions.RequestException as e:
            results.append(f"An error occurred while setting humidity: {str(e)}")

    return "\n".join(results)




def turn_on_humidifier(inner_thoughts: str) -> str:
    """
    Turn on the smart humidifier by making an API request.

    Parameters:
        inner_thoughts (str): Inner thoughts to return alongside the action.

    Returns:
        str: A message indicating the action taken and the response from the API.
    """
    # Define the URL and headers
    url = 'https://openapi.api.govee.com/router/api/v1/device/control'
    headers = {
        'Content-Type': 'application/json',
        'Govee-API-Key': 'c25ced64-9a33-4f9e-be3b-1232bd592045'  # Replace with your Govee API Key
    }

    # Define the payload
    payload = {
        "requestId": str(uuid.uuid4()),  # Generate a unique UUID for the request
        "payload": {
            "sku": "H7141",  # Replace with your humidifier SKU
            "device": "22:93:D4:AD:FC:FB:D4:49",  # Replace with your humidifier device ID
            "capability": {
                "type": "devices.capabilities.on_off",
                "instance": "powerSwitch",
                "value": 1  # 1 to turn on
            }
        }
    }

    try:
        # Make the POST request
        response = requests.post(url, headers=headers, json=payload)

        # Check the response status
        if response.status_code == 200:
            return f"{inner_thoughts} Humidifier turned on. API Response: {response.json()}"
        else:
            return f"Failed to turn on the humidifier. Status code: {response.status_code}, Response: {response.json()}"

    except Exception as e:
        return f"An error occurred while turning on the humidifier: {str(e)}"
    


import os

def set_humidity_level(inner_thoughts: str, humidity_value: int) -> str:
    """
    Set the humidity level of the smart device.

    Parameters:
        inner_thoughts (str): Inner thoughts to return alongside the action.
        humidity_value (int): Desired humidity level (0-100).

    Returns:
        str: A message indicating the action taken and the API response.
    """
    # Ensure the humidity value is within the valid range
    if not (0 <= humidity_value <= 100):
        return f"{inner_thoughts} Invalid humidity value: {humidity_value}. It must be between 0 and 100."

    url = 'https://test-openapi.api.govee.com/router/api/v1/device/control'
    headers = {
        'Content-Type': 'application/json',
        'Govee-API-Key': os.getenv('c25ced64-9a33-4f9e-be3b-1232bd592045')  # Use an environment variable for security
    }

    payload = {
        "requestId": str(uuid.uuid4()),  # Generate a unique UUID for the request
        "payload": {
            "sku": "H7141",  # Replace with your device SKU
            "device": "22:93:D4:AD:FC:FB:D4:49",  # Replace with your device ID
            "capability": {
                "type": "devices.capabilities.range",
                "instance": "humidity",
                "value": humidity_value
            }
        }
    }

    try:
        # Make the POST request
        response = requests.post(url, headers=headers, json=payload)

        # Check the response status
        if response.status_code == 200:
            return f"{inner_thoughts} Humidity set to {humidity_value}%. API Response: {response.json()}"
        else:
            return f"Failed to set humidity. Status code: {response.status_code}, Response: {response.json()}"

    except requests.exceptions.RequestException as e:
        return f"An error occurred while setting humidity: {str(e)}"

def turn_off_humidifier(inner_thoughts: str) -> str:
    """
    Turn off the smart humidifier by making an API request.

    Parameters:
        inner_thoughts (str): Inner thoughts to return alongside the action.

    Returns:
        str: A message indicating the action taken and the response from the API.
    """
    # Define the URL and headers
    url = 'https://openapi.api.govee.com/router/api/v1/device/control'
    headers = {
        'Content-Type': 'application/json',
        'Govee-API-Key': 'c25ced64-9a33-4f9e-be3b-1232bd592045'  # Replace with your Govee API Key
    }

    # Define the payload
    payload = {
        "requestId": str(uuid.uuid4()),  # Generate a unique UUID for the request
        "payload": {
            "sku": "H7141",  # Replace with your humidifier SKU
            "device": "22:93:D4:AD:FC:FB:D4:49",  # Replace with your humidifier device ID
            "capability": {
                "type": "devices.capabilities.on_off",
                "instance": "powerSwitch",
                "value": 0  # 1 to turn off
            }
        }
    }

    try:
        # Make the POST request
        response = requests.post(url, headers=headers, json=payload)

        # Check the response status
        if response.status_code == 200:
            return f"{inner_thoughts} Humidifier turned on. API Response: {response.json()}"
        else:
            return f"Failed to turn off the humidifier. Status code: {response.status_code}, Response: {response.json()}"

    except Exception as e:
        return f"An error occurred while turning on the humidifier: {str(e)}"


def turn_on_air_purifier(inner_thoughts: str) -> str:
    """
    Turn on the smart air purifier by executing the JavaScript file.

    Parameters:
        inner_thoughts (str): Inner thoughts to return alongside the action.

    Returns:
        str: A message indicating the action taken.
    """
    try:
        # Execute the JS script to turn on the air purifier
        result = subprocess.run(["node", "turn_on_air_purifier.js"], capture_output=True, text=True)

        if result.returncode != 0:
            return f"Failed to turn on the air purifier: {result.stderr}"
        
        return f"{inner_thoughts} Air purifier turned on. Command output: {result.stdout}"

    except Exception as e:
        return f"An error occurred while turning on the air purifier: {str(e)}"

def turn_off_air_purifier(inner_thoughts: str) -> str:
    """
    Turn off the smart air purifier by executing the JavaScript file.

    Parameters:
        inner_thoughts (str): Inner thoughts to return alongside the action.

    Returns:
        str: A message indicating the action taken.
    """
    try:
        # Execute the JS script to turn off the air purifier
        result = subprocess.run(["node", "turn_off_air_purifier.js"], capture_output=True, text=True)

        if result.returncode != 0:
            return f"Failed to turn off the air purifier: {result.stderr}"
        
        return f"{inner_thoughts} Air purifier turned off. Command output: {result.stdout}"

    except Exception as e:
        return f"An error occurred while turning off the air purifier: {str(e)}"

def turn_on_smart_fan(inner_thoughts: str) -> str:
    """
    Turn on the smart fan with speed level 1 by executing the JavaScript file.

    Parameters:
        inner_thoughts (str): Inner thoughts to return alongside the action.

    Returns:
        str: A message indicating the action taken.
    """
    try:
        # Execute the JS script to turn on the smart fan with speed level 1
        result = subprocess.run(["node", "turn_on_smart_fan.js"], capture_output=True, text=True)

        if result.returncode != 0:
            return f"Failed to turn on the smart fan: {result.stderr}"
        
        return f"{inner_thoughts} Smart fan turned on with speed level 1. Command output: {result.stdout}"

    except Exception as e:
        return f"An error occurred while turning on the smart fan: {str(e)}"
    
def turn_off_smart_fan(inner_thoughts: str) -> str:
    """
    Turn off the smart fan by executing the JavaScript file.

    Parameters:
        inner_thoughts (str): Inner thoughts to return alongside the action.

    Returns:
        str: A message indicating the action taken.
    """
    try:
        # Execute the JS script to turn off the smart fan
        result = subprocess.run(["node", "turn_off_smart_fan.js"], capture_output=True, text=True)

        if result.returncode != 0:
            return f"Failed to turn off the smart fan: {result.stderr}"
        
        return f"{inner_thoughts} Smart fan turned off. Command output: {result.stdout}"

    except Exception as e:
        return f"An error occurred while turning off the smart fan: {str(e)}"
    
    
def set_air_purifier_motor_speed_to_value(inner_thoughts: str, speed_value: int) -> str:
    """
    Set the fan speed by executing the JavaScript file and passing the value as an argument.

    Parameters:
        inner_thoughts (str): Inner thoughts to return alongside the action.
        speed_value (int): The fan speed to set (between 1 and 14).

    Returns:
        str: A message indicating the action taken.
    """
    if speed_value < 1 or speed_value > 14:
        return f"Invalid fan speed value. Please provide a value between 1 and 14."

    try:
        # Execute the JS script and pass the speed_value as an argument
        result = subprocess.run(["node", "control_fan_speed.js", str(speed_value)], capture_output=True, text=True)

        if result.returncode != 0:
            return f"Failed to set fan speed: {result.stderr}"
        
        return f"{inner_thoughts} Fan speed set to {speed_value}. Command output: {result.stdout}"

    except Exception as e:
        return f"An error occurred while setting the fan speed: {str(e)}"

def set_smart_fan_speed(inner_thoughts: str, speed_value: int) -> str:
    """
    Set the smart fan speed by executing the JavaScript file and passing the value as an argument.

    Parameters:
        inner_thoughts (str): Inner thoughts to return alongside the action.
        speed_value (int): The smart fan speed to set (between 1 and 3).

    Returns:
        str: A message indicating the action taken.
    """
    if speed_value < 1 or speed_value > 3:
        return f"Invalid smart fan speed value. Please provide a value between 1 and 3."

    try:
        # Execute the JS script and pass the speed_value as an argument
        result = subprocess.run(["node", "control_smart_fan_speed.js", str(speed_value)], capture_output=True, text=True)

        if result.returncode != 0:
            return f"Failed to set smart fan speed: {result.stderr}"
        
        return f"{inner_thoughts} Smart fan speed set to {speed_value}. Command output: {result.stdout}"

    except Exception as e:
        return f"An error occurred while setting the smart fan speed: {str(e)}"
    
def get_time_and_date_info(inner_thoughts: str) -> str:
    """
    Provide the current time, date, and day of the week.

    Parameters:
        inner_thoughts (str): Inner thoughts to return alongside the information.

    Returns:
        str: A message with the current time, date, and day of the week.
    """
    now = datetime.now()  # Get the current local date and time
    current_time = now.strftime("%H:%M:%S")  # Format the time in HH:MM:SS
    current_date = now.strftime("%Y-%m-%d")  # Format the date as YYYY-MM-DD
    day_of_week = now.strftime("%A")  # Get the full name of the day (e.g., Monday)
    
    # Return the formatted message with inner thoughts
    return f"{inner_thoughts} It's currently {current_time} on {day_of_week}, {current_date}."

def turn_on_light(inner_thoughts: str, command: str) -> str:
    """
    Control the Yeelight bulb.

    Parameters:
        inner_thoughts (str): Inner thoughts to return alongside the action.
        command (str): The command to execute, either "turn on" or "turn off".
        
    Returns:
        str: A message indicating the action taken.
    """
    bulb_ip = "192.168.31.171"  # IP address of the Yeelight bulb
    bulb = Bulb(bulb_ip)
    if command == "turn off":
        bulb.turn_off()
        return f"{inner_thoughts} Light turned off."
    elif command == "turn on":
        bulb.turn_on()
        return f"{inner_thoughts} Light turned on."
    else:
        return "Invalid command. Please provide 'turn on' or 'turn off'."

def turn_off_light(inner_thoughts: str, command: str) -> str:
    """
    Control the Yeelight bulb.

    Parameters:
        inner_thoughts (str): Inner thoughts to return alongside the action.
        command (str): The command to execute, either "turn on" or "turn off".
        
    Returns:
        str: A message indicating the action taken.
    """
    bulb_ip = "192.168.31.171"  # IP address of the Yeelight bulb
    bulb = Bulb(bulb_ip)
    if command == "turn off":
        bulb.turn_off()
        return f"{inner_thoughts} Light turned off."
    elif command == "turn on":
        bulb.turn_on()
        return f"{inner_thoughts} Light turned on."
    else:
        return "Invalid command. Please provide 'turn on' or 'turn off'."
def set_brightness_to_percentage(inner_thoughts: str, percentage: int) -> str:
    """
    Set the brightness of the Yeelight betwwen 1 to 100 percent.

    Parameters:
        inner_thoughts (str): Inner thoughts to return alongside the action.
        percentage (int): percentage of brightness to set to.

    Returns:
        str: A message indicating the action taken.
    """
    bulb_ip = "192.168.31.171" 
    bulb = Bulb(bulb_ip)
    bulb.set_brightness(percentage)
    return f"{inner_thoughts} Brightness set to the percentage."

def turn_on_light_and_get_time_info(inner_thoughts: str, command: str) -> str:
    """
    Control the Yeelight bulb.

    Parameters:
        inner_thoughts (str): Inner thoughts to return alongside the action.
        command (str): The command to execute, either "turn on" or "turn off".
        
    Returns:
        str: A message indicating the action taken.
    """
    bulb_ip = "192.168.31.171"  # IP address of the Yeelight bulb
    bulb = Bulb(bulb_ip)
    
    # Call get_time_and_date_info to include time and date info
    time_info = get_time_and_date_info(inner_thoughts)

    if command == "turn off":
        bulb.turn_off()
        return f"{time_info} Light turned off."
    elif command == "turn on":
        bulb.turn_on()
        return f"{time_info} Light turned on."
    else:
        return "Invalid command. Please provide 'turn on' or 'turn off'."
  
  
  
import random
import time
import threading

def fetch_occupancy_data() -> int:
    """
    Simulate fetching occupancy data from a server.
    Returns a random occupancy value between 1 and 10.
    """
    return random.randint(1, 10)  

def adjust_fan_speed_humidity_and_air_purifier(occupancy: int, inner_thoughts: str) -> None:
    """
    Adjust the smart home devices based on occupancy.
    If occupancy is less than 5, decrease settings; if greater than 5, increase settings.
    """
    if occupancy < 5:
        fan_speed, purifier_speed, humidity_level = 1, 1, 30  # Example values for decrease
        print(f"{inner_thoughts} - Occupancy is {occupancy}: Decreasing settings.")
    else:
        fan_speed, purifier_speed, humidity_level = 3, 14, 50  # Example values for increase
        print(f"{inner_thoughts} - Occupancy is {occupancy}: Increasing settings.")
    
    result = set_fanspeed_humidity_and_air_purifier_device_settings(inner_thoughts, fan_speed, purifier_speed, humidity_level)
    print(result)


def adjust_light(occupancy: int, inner_thoughts: str) -> None:
    """
    Adjust the smart home devices based on occupancy.
    If occupancy is less than 5, decrease settings; if greater than 5, increase settings.
    """
    if occupancy < 5:
        fan_speed, purifier_speed, humidity_level = 1, 1, 10  # Example values for decrease
        print(f"{inner_thoughts} - Occupancy is {occupancy}: Decreasing settings.")
    else:
        fan_speed, purifier_speed, humidity_level = 3, 14, 90  # Example values for increase
        print(f"{inner_thoughts} - Occupancy is {occupancy}: Increasing settings.")
    
    result = set_brightness_to_percentage(inner_thoughts, humidity_level)
    print(result)
    
def monitor_occupancy(inner_thoughts: str)-> str:
    """
    Continuously monitor occupancy and adjust smart home settings accordingly.

    Parameters:
        inner_thoughts (str): Inner thoughts or context for the adjustments being made.
    """
    while True:
        occupancy = fetch_occupancy_data()
        adjust_light(occupancy, inner_thoughts)
        time.sleep(30)  # Wait for 1 minute before checking again
        
def occupancy_based_autonomous_building_(inner_thoughts: str)-> str:
    """
    You are an AI agent for an autonomous building. You will need to Continuously monitor occupancy of the physical space with smart appliance setpoint and performance and adjust smart home appliance settings accordingly. If there are more people, increase the setpoint of air purifier and fan speed. If less people, decrease the setpoint accordingly
    Parameters:
        inner_thoughts (str): Inner thoughts or context for the adjustments being made.
    """
    while True:
        occupancy = fetch_occupancy_data()
        adjust_fan_speed_humidity_and_air_purifier(occupancy, inner_thoughts)
        time.sleep(30)  # Wait for 1 minute before checking again
        
        
def adjust_fan_speed_humidity_and_air_purifier_and_light(min_temp: int, max_temp: int, min_lux: int, max_lux: int, min_co2: int, max_co2: int, min_humidity: int, max_humidity: int, temperature: int, co2: int, lux: int, humidity: int, inner_thoughts: str) -> None:
    """
    Adjust the smart home devices based on environmental conditions.
    
    You are an AI agent for an autonomous building. You need Continuously monitor environmental variables such as temperature, humidity, light, and CO2 levels from the room.
    Adjust smart home settings accordingly:
    - If temperature < min_temp, increase fan speed.
    - If lux < min_lux, increase brightness.
    - If CO2 < min_co2, increase air purifier speed.
    - If humidity < min_humidity, increase humidity level.

    Parameters:
        min_temp, max_temp (int): Minimum and maximum temperature limits.
        min_lux, max_lux (int): Minimum and maximum light (lux) levels.
        min_co2, max_co2 (int): Minimum and maximum CO2 levels.
        min_humidity, max_humidity (int): Minimum and maximum humidity levels.
        temperature, co2, lux, humidity (int): Current environmental readings.
        inner_thoughts (str): A string to append to any output message.
    """
    
    # Default settings
    fan_speed, purifier_speed, humidity_level, light_brightness = 1, 1, 30, 10  # Example initial values

    # Adjust fan speed based on temperature
    if temperature < min_temp:
        fan_speed = 3  # Increase fan speed
        print(f"{inner_thoughts} - Temperature is below {min_temp}°C: Increasing fan speed to {fan_speed}.")
    elif temperature > max_temp:
        fan_speed = 1  # Decrease fan speed
        print(f"{inner_thoughts} - Temperature is above {max_temp}°C: Decreasing fan speed to {fan_speed}.")

    # Adjust brightness based on lux levels
    if lux < min_lux:
        light_brightness = 90  # Increase brightness
        print(f"{inner_thoughts} - Lux level is below {min_lux}: Increasing brightness to {light_brightness}.")
    elif lux > max_lux:
        light_brightness = 25  # Decrease brightness
        print(f"{inner_thoughts} - Lux level is above {max_lux}: Decreasing brightness to {light_brightness}.")

    # Adjust air purifier based on CO2 levels
    if co2 < min_co2:
        purifier_speed = 14  # Increase purifier speed
        print(f"{inner_thoughts} - CO2 level is below {min_co2} ppm: Increasing purifier speed to {purifier_speed}.")
    elif co2 > max_co2:
        purifier_speed = 1  # Decrease purifier speed
        print(f"{inner_thoughts} - CO2 level is above {max_co2} ppm: Decreasing purifier speed to {purifier_speed}.")

    # Adjust humidity level
    if humidity < min_humidity:
        humidity_level = 50  # Increase humidity
        print(f"{inner_thoughts} - Humidity is below {min_humidity}%: Increasing humidity level to {humidity_level}%.")
    elif humidity > max_humidity:
        humidity_level = 30  # Decrease humidity
        print(f"{inner_thoughts} - Humidity is above {max_humidity}%: Decreasing humidity level to {humidity_level}%.")

    # Call function to apply the settings
    result = set_fanspeed_humidity_airpurifier_and_light(inner_thoughts, fan_speed, purifier_speed, humidity_level, light_brightness)
    print(result)


        
def environmental_comfort_based_autonomous_building_(inner_thoughts: str)-> str:
    """
    You are an AI agent for an autonomous building. You need to Continuously monitor environmental variables such as temperature, humidity, light, and CO2 levels from the room which is the temperature,co2,lux,humidity against the environmental comfort parameters retrieved from the blockchain which are the min max variable. 
    and adjust smart home settings accordingly. if temperature < min_temp, then increase fan speed, if lux < min_lux then increase brighness, if co2 < min_co2 then increase air purifier motor, if humidity < min_humidity then increase humidity

    Parameters:
        inner_thoughts (str): Inner thoughts or context for the adjustments being made.
    
    Returns:
        str: A summary of the actions taken based on environmental comfort.
    """
    while True:
  
        contract = web3.eth.contract(address=buildingautomationcontract_address, abi=buildingautomationcontractabi)
        min_temp = contract.functions.getMinTemperature().call()
        max_temp = contract.functions.getMaxTemperature().call()
        min_lux = contract.functions.getMinLuxLevel().call()
        max_lux = contract.functions.getMaxLuxLevel().call()
        min_co2 = contract.functions.getMinCO2Level().call()
        max_co2 = contract.functions.getMaxCO2Level().call()
        min_humidity = contract.functions.getMinHumidity().call()
        max_humidity = contract.functions.getMaxHumidity().call()
        
        
        api_url = "http://localhost:8000/api/sensor"
        response = requests.get(api_url)
        data = response.json()
        temperature = data['temperature']
        co2 = data['co2']
        lux = data['lux']
        humidity = data['humidity']
        adjust_fan_speed_humidity_and_air_purifier_and_light(min_temp,max_temp,min_lux,max_lux,min_co2,max_co2,min_humidity,max_humidity,temperature,co2,lux,humidity,  inner_thoughts)
        time.sleep(30)  # Wait for 1 minute before checking again



DynamicSampleModel1 = create_dynamic_model_from_function(get_time_and_date_info)
DynamicSampleModel2 = create_dynamic_model_from_function(set_brightness_to_percentage)
DynamicSampleModel3 = create_dynamic_model_from_function(turn_off_light, "turn off")
DynamicSampleModel4 = create_dynamic_model_from_function(turn_on_light, "turn on")

DynamicSampleModel5 = create_dynamic_model_from_function(set_smart_fan_speed)
DynamicSampleModel6 = create_dynamic_model_from_function(turn_off_smart_fan, "turn off")
DynamicSampleModel7 = create_dynamic_model_from_function(turn_on_smart_fan, "turn on")

DynamicSampleModel8 = create_dynamic_model_from_function(set_air_purifier_motor_speed_to_value)
DynamicSampleModel9 = create_dynamic_model_from_function(turn_off_air_purifier, "turn off")
DynamicSampleModel10 = create_dynamic_model_from_function(turn_on_air_purifier, "turn on")

DynamicSampleModel11 = create_dynamic_model_from_function(turn_off_humidifier, "turn off")
DynamicSampleModel12 = create_dynamic_model_from_function(turn_on_humidifier, "turn on")
DynamicSampleModel13 = create_dynamic_model_from_function(set_humidity_level)
DynamicSampleModel14 = create_dynamic_model_from_function(set_fanspeed_humidity_and_air_purifier_device_settings)

DynamicSampleModel15 = create_dynamic_model_from_function(turn_on_light_and_get_time_info)
DynamicSampleModel16 = create_dynamic_model_from_function(monitor_occupancy)
DynamicSampleModel17 = create_dynamic_model_from_function(occupancy_based_autonomous_building_)

DynamicSampleModel18 = create_dynamic_model_from_function(get_room_temperature)
DynamicSampleModel19 = create_dynamic_model_from_function(get_baseline_comfort_temperature)


DynamicSampleModel20 = create_dynamic_model_from_function(get_baseline_comfort_environmetal_condition_room)
DynamicSampleModel21 = create_dynamic_model_from_function(get_room_environmetal_condition)
DynamicSampleModel22 = create_dynamic_model_from_function(environmental_comfort_based_autonomous_building_)


function_tools = [LlamaCppFunctionTool(DynamicSampleModel3), LlamaCppFunctionTool(DynamicSampleModel4),LlamaCppFunctionTool(DynamicSampleModel2),LlamaCppFunctionTool(DynamicSampleModel1),LlamaCppFunctionTool(DynamicSampleModel5),LlamaCppFunctionTool(DynamicSampleModel6),LlamaCppFunctionTool(DynamicSampleModel7),LlamaCppFunctionTool(DynamicSampleModel8),LlamaCppFunctionTool(DynamicSampleModel9),LlamaCppFunctionTool(DynamicSampleModel10),LlamaCppFunctionTool(DynamicSampleModel11),LlamaCppFunctionTool(DynamicSampleModel12),LlamaCppFunctionTool(DynamicSampleModel13),LlamaCppFunctionTool(DynamicSampleModel14),LlamaCppFunctionTool(DynamicSampleModel15),LlamaCppFunctionTool(DynamicSampleModel16),LlamaCppFunctionTool(DynamicSampleModel17),LlamaCppFunctionTool(DynamicSampleModel18),LlamaCppFunctionTool(DynamicSampleModel19),LlamaCppFunctionTool(DynamicSampleModel20),LlamaCppFunctionTool(DynamicSampleModel21),LlamaCppFunctionTool(DynamicSampleModel22)]
function_tool_registry = LlamaCppAgent.get_function_tool_registry(function_tools)
system_prompt = "You are an intelligent AI assistant for managing a smart home environment. Your primary role is to facilitate control over various smart devices, enhancing user comfort and convenience. You can turn on and off the humidifier, set specific humidity levels, and manage the air purifier, including adjusting its motor speed. Additionally, you can operate the smart fan, allowing users to turn it on or off and set desired speed levels. You also control the lighting by turning lights on and off and adjusting brightness to fit the user’s needs. Furthermore, you can provide the current time, date, and day of the week, integrating these details into your interactions. As you execute these tasks, communicate your inner thoughts to clarify actions and enhance user engagement. Your goal is to ensure a seamless and intuitive experience for managing the smart home.\n"
main_model = LlamaCppEndpointSettings(
    completions_endpoint_url="http://127.0.0.1:8080/completion"
)
llama_cpp_agent = LlamaCppAgent(main_model, debug_output=True,
                                system_prompt=system_prompt + function_tool_registry.get_documentation(),
                                predefined_messages_formatter_type=MessagesFormatterType.CHATML)

app = Flask(__name__)
CORS(app)

@app.route('/process_input', methods=['POST'])
def process_input():
    user_input = request.json.get('input')  # Assuming input is sent as JSON {"input": "user input here"}
    # Process user input using AI model
    ai_response = llama_cpp_agent.get_chat_response(user_input, temperature=0.3, function_tool_registry=function_tool_registry)
   
    return str(ai_response[0]['return_value'])

if __name__ == '__main__':
    app.run(host='localhost', port=1234, debug=True) 

#64538121593627479219236717456296040253649251070565921025083761489207682213087