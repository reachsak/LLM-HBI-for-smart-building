import csv
import json
import time
import requests
import ipfshttpclient

# Connect to IPFS
client = ipfshttpclient.connect()

# IPNS key name
IPNS_KEY_NAME = "my_timeseries_data"

# Function to fetch latitude data from the REST API
def fetch_latitude():
    try:
        response = requests.get("https://api.wheretheiss.at/v1/satellites/25544")
        data = response.json()
        latitude = data.get("latitude")
        if latitude is None:
            raise ValueError("Latitude data not found in API response")
        return latitude
    except Exception as e:
        print("Failed to fetch latitude data:", e)
        return None

# Function to retrieve CSV file from IPFS using IPNS
def retrieve_csv_from_ipfs():
    try:
        ipns_record = client.name_resolve(IPNS_KEY_NAME)
        cid = ipns_record['Path']
        csv_data = client.cat(cid).decode()
        return csv_data
    except ipfshttpclient.exceptions.ErrorResponse as e:
        print("Failed to retrieve CSV file from IPFS using IPNS:", e)
        return None

# Function to append latitude data to CSV data
def append_to_csv(csv_data, latitude):
    rows = csv_data.strip().split('\n')
    timestamp = int(time.time())
    rows.append(f"{timestamp},{latitude}")
    return '\n'.join(rows)

# Function to upload CSV data to IPFS
def upload_csv_to_ipfs(csv_data):
    res = client.add_bytes(csv_data.encode())
    cid = res['Hash']
    print(f"Added updated CSV file to IPFS with CID: {cid}")
    return cid

# Function to publish IPNS record
def publish_ipns(cid):
    res = client.name_publish(cid, key=IPNS_KEY_NAME)
    print(f"Published IPNS record: {res['Name']} -> {res['Value']}")

# Main loop
while True:
    latitude = fetch_latitude()
    
    if latitude is not None:
        csv_data = retrieve_csv_from_ipfs()
        if csv_data is not None:
            updated_csv_data = append_to_csv(csv_data, latitude)
            updated_cid = upload_csv_to_ipfs(updated_csv_data)
            publish_ipns(updated_cid)
        else:
            # Handle case where CSV file retrieval fails
            print("Failed to retrieve CSV file. Skipping update.")
    else:
        # Handle case where latitude fetch fails
        print("Failed to fetch latitude data. Skipping update.")
    
    time.sleep(30)  # Wait for 30 seconds before collecting more data
