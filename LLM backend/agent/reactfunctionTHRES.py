

from flask import Flask, request, jsonify
import time
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


import subprocess
import os
import uuid
import requests
from yeelight import Bulb
from pydantic import BaseModel



def set_smart_light_brightness_to_percentage(inner_thoughts: str, percentage: int) -> str:
    """
    Set the brightness of the Yeelight between 1 to 100 percent.

    Parameters:
        inner_thoughts (str): Inner thoughts to return alongside the action.
        percentage (int): percentage of brightness to set to.

    Returns:
        str: A message indicating the action taken.
    """
    bulb_ip = "192.168.31.171"
    bulb = Bulb(bulb_ip)
    bulb.set_brightness(percentage)
    return f"{inner_thoughts} Brightness set to {percentage}%."


def set_air_purifier_level_to_value(inner_thoughts: str, speed_value: int) -> str:
    """
    Set the fan speed by executing the JavaScript file and passing the value as an argument.

    Parameters:
        inner_thoughts (str): Inner thoughts to return alongside the action.
        speed_value (int): The fan speed to set (between 1 and 14).

    Returns:
        str: A message indicating the action taken.
    """
    if speed_value < 1 or speed_value > 10:
        return f"Invalid fan speed value. Please provide a value between 1 and 14."

    try:
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
        speed_value (int): The smart fan speed to set (between 1 and 10).

    Returns:
        str: A message indicating the action taken.
    """
    if speed_value < 0 or speed_value > 10:
        return f"Invalid smart fan speed value. Please provide a value between 1 and 3."

    try:
        result = subprocess.run(["node", "control_smart_fan_speed.js", str(speed_value)], capture_output=True, text=True)

        if result.returncode != 0:
            return f"Failed to set smart fan speed: {result.stderr}"
        
        return f"{inner_thoughts} Smart fan speed set to {speed_value}. Command output: {result.stdout}"

    except Exception as e:
        return f"An error occurred while setting the smart fan speed: {str(e)}"


def set_humidifier_level(inner_thoughts: str, humidity_value: int) -> str:
    """
    Set the humidity level of the smart device.

    Parameters:
        inner_thoughts (str): Inner thoughts to return alongside the action.
        humidity_value (int): Desired humidity level (0-100).

    Returns:
        str: A message indicating the action taken and the API response.
    """
    if not (0 <= humidity_value <= 100):
        return f"{inner_thoughts} Invalid humidity value: {humidity_value}. It must be between 0 and 100."

    url = 'https://test-openapi.api.govee.com/router/api/v1/device/control'
    headers = {
        'Content-Type': 'application/json',
        'Govee-API-Key': os.getenv('c25ced64-9a33-4f9e-be3b-1232bd592045')
    }

    payload = {
        "requestId": str(uuid.uuid4()),
        "payload": {
            "sku": "H7141",
            "device": "22:93:D4:AD:FC:FB:D4:49",
            "capability": {
                "type": "devices.capabilities.range",
                "instance": "humidity",
                "value": humidity_value
            }
        }
    }

    try:
        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            return f"{inner_thoughts} Humidity set to {humidity_value}%. API Response: {response.json()}"
        else:
            return f"Failed to set humidity. Status code: {response.status_code}, Response: {response.json()}"

    except requests.exceptions.RequestException as e:
        return f"An error occurred while setting humidity: {str(e)}"


import random

import random

def adjust_appliance_based_on_comfort_threshold(inner_thoughts: str, 
                                                humidity_level: int, co2_level: int, 
                                                temperature: int, light_level: int, 
                                                min_humidity: int, max_humidity: int, 
                                                min_temperature: int, max_temperature: int, 
                                                min_co2: int, max_co2: int, min_light: int, max_light: int) -> dict:
    """
    Adjusts smart appliances based on real-time data and comfort threshold values.

    Parameters:
        inner_thoughts (str): A message indicating the reasoning behind the adjustment.
        humidity_level (int): The current humidity level in the environment.
        co2_level (int): The current CO2 level in the environment.
        temperature (int): The current temperature in the environment.
        light_level (int): The current light level in the environment.
        min_humidity (int): The minimum threshold for humidity.
        max_humidity (int): The maximum threshold for humidity.
        min_temperature (int): The minimum threshold for temperature.
        max_temperature (int): The maximum threshold for temperature.
        min_co2 (int): The minimum acceptable CO2 level.
        max_co2 (int): The maximum acceptable CO2 level.
        min_light (int): The minimum acceptable light intensity.
        max_light (int): The maximum acceptable light intensity.

    Returns:
         dict: A dictionary containing the levels for the appliances (humidifier, air purifier, fan, light).
    """
    # Adjust appliance levels based on the provided parameters and thresholds
    humidifier_level = 0
    air_purifier_level = 0
    fan_speed = 0
    light_brightness = 0

    # Humidity Adjustment
    if humidity_level < min_humidity:
        humidifier_level = random.randint(6, 10)
    elif humidity_level > max_humidity:
        humidifier_level = random.randint(1, 5)

    # Air Purifier Adjustment (CO2 level-based)
    if co2_level < min_co2:
        air_purifier_level = random.randint(1, 5)
    elif co2_level > max_co2:
        air_purifier_level = random.randint(6, 10)

    # Fan Speed Adjustment (Temperature-based)
    if temperature > max_temperature:
        fan_speed = random.randint(6, 10)
    elif temperature < min_temperature:
        fan_speed = random.randint(1, 5)

    # Light Intensity Adjustment
    if light_level < min_light:
        light_brightness = random.randint(50, 100)
    elif light_level > max_light:
        light_brightness = random.randint(1, 30)

    print(f"I will set humidifier to level {humidifier_level}")
    print(f"I will set air purifier to level {air_purifier_level}")
    print(f"I will set fan speed to level {fan_speed}")
    print(f"I will set light brightness to level {light_brightness}%")
    
    # Return appliance adjustments
    responses = {}

    try:
        responses["humidifier"] = set_humidifier_level("Setting humidifier", humidifier_level)
    except Exception as e:
        print(f"Error adjusting humidifier: {e}")
    
    try:
        responses["air_purifier"] = set_air_purifier_level_to_value("Setting air purifier", air_purifier_level)
    except Exception as e:
        print(f"Error adjusting air purifier: {e}")
    
    try:
        responses["fan"] = set_smart_fan_speed("Setting smart fan", fan_speed)
    except Exception as e:
        print(f"Error adjusting fan: {e}")
    
    try:
        responses["light"] = set_smart_light_brightness_to_percentage("Setting light brightness", light_brightness)
    except Exception as e:
        print(f"Error adjusting light: {e}")

    return responses



DynamicSampleModel1 = create_dynamic_model_from_function(adjust_appliance_based_on_comfort_threshold)



function_tools = [LlamaCppFunctionTool(DynamicSampleModel1)]
function_tool_registry = LlamaCppAgent.get_function_tool_registry(function_tools)
system_prompt = "You are an intelligent AI assistant for managing a smart home environment. Your roles is to look at the envrionmental data and adjust the smart buildign appliance accoridngly to the level predefined\n"
main_model = LlamaCppEndpointSettings(
    completions_endpoint_url="http://127.0.0.1:8080/completion"
)
llama_cpp_agent = LlamaCppAgent(main_model, debug_output=True,
                                system_prompt=system_prompt + function_tool_registry.get_documentation(),
                                predefined_messages_formatter_type=MessagesFormatterType.CHATML)

import requests

# Function to get the summary from the API
def get_summary():
    url = "http://127.0.0.1:6000/api/summary"  # Adjust URL if hosted elsewhere
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        return data.get("summary", "No summary available")
    except requests.exceptions.RequestException as e:
        return f"Error fetching summary: {e}"

# Function to process the summary using the AI model
def process_summary(summary):
    ai_response = llama_cpp_agent.get_chat_response(summary, temperature=0.3, function_tool_registry=function_tool_registry)
    return str(ai_response[0]['return_value'])

if __name__ == '__main__':
    while True:
        summary = get_summary()  # Extract summary from the API
        print("Extracted Summary:")
        print(summary)
        
        ai_response = process_summary(summary)  # Process the summary with the AI model
        print("AI Response:")
        print(ai_response)
        
        time.sleep(30)  # Wait for 30 seconds before running the loop again

#64538121593627479219236717456296040253649251070565921025083761489207682213087

###reactfunctionOCC.py
###RRRRROCCUPANCY.py