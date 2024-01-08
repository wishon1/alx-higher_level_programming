#!/usr/bin/node
/* prints two arguments passed to it, in the following format: “ is ” */

const arg1 = process.argv[2];
const arg2 = process.argv[3];
const len = process.argv.length;

if (len === 4 && arg2 !== undefined) {
  console.log(arg1 + ' is ' + arg2);
} else if (len === 3 && arg2 === undefined) {
  console.log(arg1 + ' is undefined');
} else {
  console.log('undefined is undefined');
}
