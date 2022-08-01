#!/usr/bin/node
const number = parseInt(process.argv[2]);
let i;
if (isNaN(number)) {
  console.log('Missing size');
} else {
  for (i = 1; i <= number; i++) {
    console.log('X'.repeat(number));
  }
}
