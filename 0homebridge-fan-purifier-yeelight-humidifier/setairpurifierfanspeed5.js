//miot send 192.168.31.55 -t 7bf220e5040480b95871b31ed1ceecb8 set_properties '[{"siid":9,"piid":11,"value":10}]'
const { exec } = require("child_process");

// Replace the IP address, token, siid, piid, and value with your device's details
const ipAddress = "192.168.31.55";
const token = "7bf220e5040480b95871b31ed1ceecb8";
const siid = 9;
const piid = 11;
const value = 7;
///1 to 14 fanspeed
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
