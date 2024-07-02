#!/usr/bin/node
/*
 * Checks number of arguments passed.
 * If no argument print "No argument".
 * If one argument print "Argument found".
 * If more than one argument print "Arguments found".
 */
const { argv } = require('node:process');

if (argv.length === 2) {
  console.log('No argument');
} else if (argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
