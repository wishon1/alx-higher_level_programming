#!/usr/bin/node
/* prints a message depending of the number of arguments passed */

const cmdArg = process.argv.length;

if (cmdArg <= 2) {
  console.log('No argument');
} else if (cmdArg === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
