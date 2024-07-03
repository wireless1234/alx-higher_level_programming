#!/usr/bin/node
/**
 * Finds second largest integer from list.
 * List gotten from arguments.
 */
const { argv } = require('node:process');

let max = parseInt(argv[2]);
let prevmax = max;
if (argv.length < 4) {
  console.log(0);
} else {
  argv.forEach((arg) => {
    if (arg > max) {
      prevmax = max;
      max = arg;
    }
  });
  console.log(prevmax);
}
