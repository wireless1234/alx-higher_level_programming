#!/usr/bin/node
/**
 * Function that adds two numbers.
 * Get the two numbers from argument.
 * Print "NaN" if number not given.
 */
const { argv } = require('node:process');
function add (a, b) {
  const num1 = parseInt(a);
  const num2 = parseInt(b);
  if (num1 && num2) {
    console.log(num1 + num2);
  } else {
    console.log('NaN');
  }
}

add(argv[2], argv[3]);
