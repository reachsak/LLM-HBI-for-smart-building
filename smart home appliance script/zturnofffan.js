//miot send 192.168.31.55 -t 337a18704c32b99bb926e21c60bcf474 set_properties '[{"siid":9,"piid":11,"value":10}]'
const { exec } = require("child_process");

// Replace the IP address, token, siid, piid, and value with your device's details
const ipAddress = "192.168.31.49";
const token = "337a18704c32b99bb926e21c60bcf474";
const siid = 2;
const piid = 1;
const value = 0; // change between 1 to 4 for speed level

// Define the command to execute
const command = `miot send ${ipAddress} -t ${token} set_properties '[{"siid":${siid},"piid":${piid},"value":${value}}]'`;

// Execute the command
exec(command, (error, stdout, stderr) => {
  if (error) {
    console.error(`Error executing command: ${error}`);
    return;
  }
  console.log(`Command output: ${stdout}`);
});

//https://home.miot-spec.com/spec?type=urn:miot-spec-v2:device:fan:0000A005:zhimi-za3:1
