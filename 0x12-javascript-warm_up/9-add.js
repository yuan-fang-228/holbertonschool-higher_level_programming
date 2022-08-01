#!/usr/bin/node
function add (a, b) {
  return (a + b);
}
const number1 = parseInt(process.argv[2]);
const number2 = parseInt(process.argv[3]);
if (isNaN(number1) || isNaN(number2)) {
  console.log('NaN');
} else {
  console.log(add(number1, number2));
}
