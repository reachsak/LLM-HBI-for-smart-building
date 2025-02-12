from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

# Comfort thresholds
COMFORT_THRESHOLDS = {
    "temperature": {"min": 20.0, "max": 27.0},
    "humidity": {"min": 40.0, "max": 100.0},
    "lux": {"min": 50.0, "max": 150.0},
    "co_level": {"min": 0.0, "max": 50.0}
}

# Fixed sensor and device data
def get_sensor_data():
    return {
        "timestamp": datetime.now().isoformat(),
        "temperature": 35.5,
        "humidity": 45.0,
        "co_level": 30.0,
        "lux": 250.0,
        "occupancy": 25,
        "smart_devices": {
            "fan": 5,
            "humidifier": 7,
            "air_purifier": 6,
            "light": 75
        },
        "comfort_thresholds": COMFORT_THRESHOLDS
    }

def get_conditions_assessment(data):
    assessment = []
    thresholds = COMFORT_THRESHOLDS
    
    if data['temperature'] < thresholds['temperature']['min']:
        assessment.append("Temperature is below comfort threshold")
    elif data['temperature'] > thresholds['temperature']['max']:
        assessment.append("Temperature is above comfort threshold")
    else:
        assessment.append("Temperature is within comfort range")
    
    if data['humidity'] < thresholds['humidity']['min']:
        assessment.append("Humidity is below comfort threshold")
    elif data['humidity'] > thresholds['humidity']['max']:
        assessment.append("Humidity is above comfort threshold")
    else:
        assessment.append("Humidity is within comfort range")
    
    if data['lux'] < thresholds['lux']['min']:
        assessment.append("Light level is too low")
    elif data['lux'] > thresholds['lux']['max']:
        assessment.append("Light level is too high")
    else:
        assessment.append("Light level is optimal")
    
    if data['co_level'] > thresholds['co_level']['max']:
        assessment.append("CO levels are above safety threshold")
    elif data['co_level'] > (thresholds['co_level']['max'] * 0.8):
        assessment.append("CO levels are elevated but safe")
    else:
        assessment.append("CO levels are safe")
    
    return " and ".join(assessment) + "."

def get_summary():
    data = get_sensor_data()
    devices = data['smart_devices']
    thresholds = COMFORT_THRESHOLDS
    
    summary = f"""
Use the function Occupancy based automation.....
AI Assistant Instruction:

You are an AI assistant designed to autonomously control building operations based on occupancy levels. You will manage the operation of the smart humidifier, smart air purifier, and smart fan, each operating on a scale from 0 to 10.

NOW see the Room Status Overview below, Note you don't need to set all the appliane at the same level, it can be diferent but within those range of level defined:
-------------------
The room currently has {data['occupancy']} people present.

    """
    return summary.strip()

@app.route('/api/sensors', methods=['GET'])
def get_readings():
    return jsonify(get_sensor_data())

@app.route('/api/thresholds', methods=['GET'])
def get_thresholds():
    return jsonify(COMFORT_THRESHOLDS)

@app.route('/api/summary', methods=['GET'])
def get_text_summary():
    return jsonify({"summary": get_summary()})

@app.route('/api/sensors/<sensor_type>', methods=['GET'])
def get_specific_reading(sensor_type):
    data = get_sensor_data()
    
    if sensor_type in data['smart_devices']:
        return jsonify({sensor_type: data['smart_devices'][sensor_type]})
    elif sensor_type in data:
        return jsonify({sensor_type: data[sensor_type]})
    
    return jsonify({"error": "Sensor or device type not found"}), 404

@app.route('/api/smart-devices', methods=['GET'])
def get_device_states():
    data = get_sensor_data()
    return jsonify(data['smart_devices'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000, debug=True)

### browser
# http://localhost:8080/api/sensors