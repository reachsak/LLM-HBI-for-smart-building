

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

def adjust_appliance_levels(inner_thoughts: str, occupancy: int) -> dict:
    """
    Adjusts the levels of appliances (humidifier, air purifier, fan, and light) based on occupancy.

    Parameters:
        inner_thoughts (str): The internal thoughts or reasoning behind the appliance adjustments.
        occupancy (int): The number of people in the space.

    Returns:
        dict: A dictionary containing the levels for the appliances (humidifier, air purifier, fan, light).
    """
    # Initialize appliance levels
    humidifier_level = 0
    air_purifier_level = 0
    fan_speed = 0
    light_brightness = 0

    # Apply appliance settings based on occupancy
    if occupancy == 0:
        humidifier_level = 0
        air_purifier_level = 0
        fan_speed = 0
        light_brightness = 0
    elif 1 <= occupancy <= 5:
        humidifier_level = random.randint(1, 3)
        air_purifier_level = random.randint(1, 3)
        fan_speed = random.randint(1, 3)
        light_brightness = random.randint(1, 30)
    elif 5 < occupancy <= 10:
        humidifier_level = random.randint(4, 6)
        air_purifier_level = random.randint(4, 6)
        fan_speed = random.randint(4, 6)
        light_brightness = random.randint(31, 70)
    elif 10 < occupancy <= 20:
        humidifier_level = random.randint(7, 9)
        air_purifier_level = random.randint(7, 9)
        fan_speed = random.randint(7, 9)
        light_brightness = random.randint(71, 100)
    else:
        humidifier_level = 10
        air_purifier_level = 10
        fan_speed = 10
        light_brightness = 100

    # Print the inner thoughts and appliance adjustments
    print(f"{inner_thoughts}")
    print(f"I will adjust the humidifier level to {humidifier_level}.")
    print(f"I will adjust the air purifier level to {air_purifier_level}.")
    print(f"I will adjust the fan speed to {fan_speed}.")
    print(f"I will adjust the light brightness to {light_brightness}.")

    # Apply appliance level adjustments with error handling
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



DynamicSampleModel1 = create_dynamic_model_from_function(adjust_appliance_levels)



function_tools = [LlamaCppFunctionTool(DynamicSampleModel1)]
function_tool_registry = LlamaCppAgent.get_function_tool_registry(function_tools)
system_prompt = "You are an intelligent AI assistant for managing a smart home environment. Your roles is to look at the occupancy level and adjust the smart buildign appliance accoridngly to the level predefined\n"
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