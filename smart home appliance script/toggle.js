// miot send 192.168.31.55 -t 7bf220e5040480b95871b31ed1ceecb8 action '{"aiid":1,"in":[],"siid":2}'

const { exec } = require("child_process");

// Replace the IP address and token with your device's IP and token
const ipAddress = "192.168.31.55";
const token = "7bf220e5040480b95871b31ed1ceecb8";

// Define the command to execute
const command = `miot send ${ipAddress} -t ${token} action '{"aiid":1,"in":[],"siid":2}'`;

// Execute the command
exec(command, (error, stdout, stderr) => {
  if (error) {
    console.error(`Error executing command: ${error}`);
    return;
  }
  console.log(`Command output: ${stdout}`);
});

/// read the documentation here
//https://home.miot-spec.com/spec?type=urn%3Amiot-spec-v2%3Adevice%3Aair-purifier%3A0000A007%3Azhimi-cpa4%3A1

// miot send 192.168.31.55 -t 7bf220e5040480b95871b31ed1ceecb8 action '{"aiid":1,"in":[],"siid":2}'

//miot send 192.168.31.55 -t 7bf220e5040480b95871b31ed1ceecb8 get_properties '[{"siid":4,"piid":3}]'

//check fan speed
//miot send 192.168.31.55 -t 7bf220e5040480b95871b31ed1ceecb8 get_properties '[{"siid":9,"piid":1}]'
//set fan speed
//miot send 192.168.31.55 -t 7bf220e5040480b95871b31ed1ceecb8 '[{"siid":9,"piid":1,"value":1000}]'
// miot send 192.168.31.55 -t 7bf220e5040480b95871b31ed1ceecb8 get_properties '[{"siid":3,"piid":4}]'
