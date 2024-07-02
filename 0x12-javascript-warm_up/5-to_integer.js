#!/usr/bin/node
/**
 * Print "My number: <first argument converted to integer>".
 * if argument cannot be converted print "Not a number".
 * Print using "console.log".
 */
const { argv } = require('node:process');

if (argv[2] && !isNaN(argv[2])) {
  console.log(`My number: ${parseInt(argv[2])}`);
} else {
  console.log('Not a number');
}
