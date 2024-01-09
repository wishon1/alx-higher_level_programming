#!/usr/bin/node
/* script that prints a square */

const arg = parseInt(process.argv[2], 10);
if (isNaN(arg)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < arg; i++) {
    let line = '';
    for (let j = 0; j < arg; j++) {
      line += 'X';
    }
    console.log(line);
  }
}
