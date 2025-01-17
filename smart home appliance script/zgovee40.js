const fetch = require("node-fetch"); // You might need to install this if you are running the script in a Node.js environment
const { v4: uuidv4 } = require("uuid"); // UUID generation library

// Define the URL and headers
const url = "https://openapi.api.govee.com/router/api/v1/device/control";
const headers = {
  "Content-Type": "application/json",
  "Govee-API-Key": "c25ced64-9a33-4f9e-be3b-1232bd592045",
};

// Define the payload for controlling humidity
const payload = {
  requestId: uuidv4(), // Generate a unique UUID for the request
  payload: {
    sku: "H7141",
    device: "22:93:D4:AD:FC:FB:D4:49",
    capability: {
      type: "devices.capabilities.range",
      instance: "humidity",
      value: 40, // Set the humidity level (1 to 100)
    },
  },
};

// Make the POST request
fetch(url, {
  method: "POST",
  headers: headers,
  body: JSON.stringify(payload),
})
  .then((response) => {
    return response.json().then((data) => ({
      status: response.status,
      body: data,
    }));
  })
  .then(({ status, body }) => {
    console.log("Status Code:", status);
    console.log("Response:", body);
  })
  .catch((error) => {
    console.error("Error:", error);
  });
