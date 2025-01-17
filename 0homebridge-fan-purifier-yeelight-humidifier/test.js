const miio = require("miio");

miio
  .device({ address: "127.0.0.1", token: "00000000000000000000000000000000" })
  .then((device) => console.log("Connected to", device))
  .catch((err) => handleErrorHere);
