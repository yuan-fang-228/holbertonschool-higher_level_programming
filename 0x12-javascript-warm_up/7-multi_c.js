#!/usr/bin/node
const number = parseInt(process.argv[2]);
let i;
if (isNaN(number)) {
  console.log('Missing number of occurrences');
} else {
  for (i = 1; i <= number; i++) {
    console.log('C is fun');
  }
}
