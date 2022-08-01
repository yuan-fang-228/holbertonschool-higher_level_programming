#!/usr/bin/node
const numberOfArgument = process.argv.length;
if (numberOfArgument <= 2) {
  console.log('No argument');
} else if (numberOfArgument === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
