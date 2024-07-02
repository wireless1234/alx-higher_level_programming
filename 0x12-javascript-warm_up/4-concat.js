#!/usr/bin/node
/**
 * Prints "argument 1 is argument 3".
 * You can not use var.
 * You must use "console.log".
 */
const { argv } = require('node:process');

console.log(`${argv[2]} is ${argv[3]}`);
