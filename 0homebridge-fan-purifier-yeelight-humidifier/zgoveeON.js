const fetch = require("node-fetch"); // You might need to install this if you are running the script in a Node.js environment
const { v4: uuidv4 } = require("uuid"); // UUID generation library

// Define the URL and headers
const url = "https://openapi.api.govee.com/router/api/v1/device/control";
const headers = {
  "Content-Type": "application/json",
  "Govee-API-Key": "c25ced64-9a33-4f9e-be3b-1232bd592045",
};

// Define the payload
const payload = {
  requestId: uuidv4(), // Generate a unique UUID for the request
  payload: {
    sku: "H7141",
    device: "22:93:D4:AD:FC:FB:D4:49",
    capability: {
      type: "devices.capabilities.on_off",
      instance: "powerSwitch",
      value: 1, // Change to 1 to turn on
    },
  },
};

// Make the POST request
fetch(url, {
  method: "POST",
  headers: headers,
  body: JSON.stringify(payload),
})
  .then((response) => response.json())
  .then((data) => {
    console.log("Status Code:", data.statusCode);
    console.log("Response:", data);
  })
  .catch((error) => {
    console.error("Error:", error);
  });
