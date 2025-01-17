const io = require("mijia-io");

// Resolve a device, specifying the token (see below for how to get the token)
io.device({
  address: "127.0.0.1",
  token: "00000000000000000000000000000000",
})
  .then(async (device) => {
    console.log(device);
  })
  .catch((err) => console.error("Error connecting to device:", err));
