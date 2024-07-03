#!/usr/bin/node
/**
 * Print "C is fun".
 * Number of times is given in first argument.
 * Print “Missing number of occurrences” if missing.
 */
const { argv } = require('node:process');

let cnt = 0;

if (argv[2] && !isNaN(argv[2])) {
  while (cnt < argv[2]) {
    console.log('C is fun');
    cnt++;
  }
} else {
  console.log('Missing number of occurrences');
}
