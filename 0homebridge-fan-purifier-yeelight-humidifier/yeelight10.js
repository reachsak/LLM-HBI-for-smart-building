const { Bulb } = require("yeelight.io");

const l1 = new Bulb("192.168.31.171");

l1.on("connected", (light) => {
  console.log(`connected to ${light.ip}`);
  l1.brightness(10);
});
l1.connect();
//l1.disconnect();
