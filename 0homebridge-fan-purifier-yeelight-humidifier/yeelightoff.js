"use strict";

const { Bulb } = require("yeelight.io");

const l1 = new Bulb("192.168.31.171");

l1.on("connected", (light) => {
  console.log(`connected to ${light.ip}`);
  light.toggle();
  light.disconnect();
});

l1.on("disconnected", (light) => {
  console.log(`disconnected with ${light.ip}`);
});

l1.on("error", (light, err) => {
  console.error(`error [${err.message}] occur on ${light.ip}`);
  light.disconnect();
});

l1.connect();
