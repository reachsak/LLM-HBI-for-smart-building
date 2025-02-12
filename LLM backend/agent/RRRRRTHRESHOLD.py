from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

# Comfort thresholds
COMFORT_THRESHOLDS = {
    "temperature": {"min": 20.0, "max": 27.0},
    "humidity": {"min": 40.0, "max": 100.0},
    "lux": {"min": 50.0, "max": 150.0},
    "co_level": {"min": 0.0, "max": 59.0}
}

# Fixed sensor and device data
def get_sensor_data():
    return {
        "timestamp": datetime.now().isoformat(),
        "temperature": 35,
        "humidity": 45,
        "co_level": 30,
        "lux": 250,
        "occupancy": 10,
        "smart_devices": {
            "fan": 5,
            "humidifier": 7,
            "air_purifier": 6,
            "light": 75
        },
        "comfort_thresholds": COMFORT_THRESHOLDS
    }


def get_summary():
    data = get_sensor_data()
    devices = data['smart_devices']
    thresholds = COMFORT_THRESHOLDS
    
    summary = f"""
Use the function threshold-based automation.....

- Temperature: {data['temperature']}°C 
(Min Temperature : {thresholds['temperature']['min']}°C, 
Max Temperature: {thresholds['temperature']['max']}°C)
- Humidity: {data['humidity']}% 
(Min Humidity: {thresholds['humidity']['min']}%, 
Max Humidity: {thresholds['humidity']['max']}%)
- CO Level: {data['co_level']} PPM 
(Min CO Level: {thresholds['co_level']['min']} PPM, 
Max CO Level: {thresholds['co_level']['max']} PPM)
- Light Level: {data['lux']} Lux 
(Min Light Level: {thresholds['lux']['min']} Lux, 
Max Light Level: {thresholds['lux']['max']} Lux)
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