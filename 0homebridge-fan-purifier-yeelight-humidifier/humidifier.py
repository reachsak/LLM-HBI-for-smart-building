import requests
import subprocess

# Define the IP address, token, service instance ID (siid), property instance ID (piid), and default value
ip_address = "192.168.31.55"
token = "7bf220e5040480b95871b31ed1ceecb8"
siid = 9
piid = 11
default_value = 5

# Function to retrieve humidity value from the REST API server
def get_humidity():
    try:
        response = requests.get("http://reachsak.pakgekite.com")
        data = response.json()
        humidity = data.get("humidity")
        return humidity
    except Exception as e:
        print("Error retrieving humidity:", e)
        return None

# Function to set fan speed based on humidity threshold
def set_fan_speed(humidity, threshold=40):
    if humidity is None:
        print("Cannot set fan speed. Humidity data is not available.")
        return
    if humidity < threshold:
        print(f"Humidity is below threshold ({threshold}%). Setting fan speed to high.")
        # Define the command to adjust fan speed
        command = f"miot send {ip_address} -t {token} set_properties '[{{\"siid\":{siid},\"piid\":{piid},\"value\":{default_value}}}]'"
        # Execute the command to adjust fan speed
        subprocess.run(command, shell=True)
    else:
        print("Humidity is within the threshold. No action needed.")

# Main function
def main():
    humidity = get_humidity()
    set_fan_speed(humidity)

# Entry point of the script
if __name__ == "__main__":
    main()
