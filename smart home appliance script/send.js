// Node.js side: index.js
const axios = require("axios");

// Function to send temperature data to Flask API
function sendTemperatureToFlask(temperature) {
  const data = { temperature };

  axios
    .post("http://localhost:4000/temperature", data)
    .then((response) => {
      console.log("Server response:", response.data);
    })
    .catch((error) => {
      console.error("Error communicating with Flask server:", error);
    });
}

// Example: Simulate changing temperature every 10 seconds and send to Flask API
setInterval(() => {
  const temperature = Math.random() * 100; // Generate random temperature data
  sendTemperatureToFlask(temperature);
}, 5000); // Change temperature every 10 seconds
