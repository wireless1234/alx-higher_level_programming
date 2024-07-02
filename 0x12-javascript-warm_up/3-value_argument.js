#!/usr/bin/node
/**
 * Prints argument passed to it.
 * Can not use "var" or "length".
 * Print using "console.log".
 */
const { argv } = require('node:process');

if (argv[2]) {
  console.log(argv[2]);
} else {
  console.log('No argument');
}
