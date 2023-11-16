#!/usr/bin/node
/* Computes and prints a factorial */

const args = process.argv;
const input = parseInt(args[2]);
console.log(fact(input));
function fact (n) {
  if (n === 0 || isNaN(n)) {
    return 1;
  } else {
    return n * fact(n - 1);
  }
}
