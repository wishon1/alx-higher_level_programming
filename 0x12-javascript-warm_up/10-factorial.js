#!/usr/bin/node
/* computes and prints a factorial */

function factorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const arg = parseInt(process.argv[2], 10);

if (isNaN(arg)) {
  console.log(1); // Factorial of NaN is 1
} else {
  const result = factorial(arg);
  console.log(result);
}
