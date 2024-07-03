#!/usr/bin/node
/**
 * Print a square using character "X".
 * first argument is size of square.
 * If it is not available, print "Missing size".
 */
const { argv } = require('node:process');

let cnt1 = 0;

if (argv[2] && !isNaN(argv[2])) {
  while (cnt1 < argv[2]) {
    let myStr = '';
    let cnt2 = 0;
    while(cnt2 < argv[2]) {
      myStr += 'X';
      cnt2++;
    }
    console.log(myStr);
    cnt1++;
  }
} else {
  console.log('Missing size');
}
