#!/usr/bin/node
/**
 * Print factorial of number.
 * Must use recursive function.
 * Factorial of NaN is "1".
 */
const { argv } = require('node:process');
function factorial (a) {
  let n = parseInt(a);
  if (isNaN(n) || n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

const fact = factorial(argv[2]);
console.log(fact);
