const miio = require("miio");
const devices = miio.devices({
  cacheTime: 300, // 5 minutes. Default is 1800 seconds (30 minutes)
});

devices.on("available", (reg) => {
  if (!reg.token) {
    console.log(reg.id, "hides its token");
    return;
  }

  const device = reg.device;
  if (!device) {
    console.log(reg.id, "could not be connected to");
    return;
  }

  // Do something useful with the device
});

devices.on("unavailable", (reg) => {
  if (!reg.device) return;

  // Do whatever you need here
});

devices.on("error", (err) => {
  // err.device points to info about the device
  console.log("Something went wrong connecting to device", err);
});
