const program = require('..');

program()
.command('hello', () => {
  console.log('hello world');
})
.command('help', () => {
  console.log('');
  console.log('- hello');
  console.log('- help');
})
.parse();