#!/usr/bin/node
/**
 * Print three sentences using a loop.
 * Must use an array of string to store sentences.
 * Must print using "console.log".
 */
const myArr = ['C is fun', 'Python is cool', 'Javascript is amazing'];

let cnt = 0;

while (cnt < myArr.length) {
  console.log(myArr[cnt]);
  cnt++;
}
