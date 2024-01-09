#!/usr/bin/node
/* prints x times “C is fun” */

const arg = parseInt(process.argv[2], 10);

if (isNaN(arg)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 1; i <= arg; i++) {
    console.log('C is fun');
  }
}
