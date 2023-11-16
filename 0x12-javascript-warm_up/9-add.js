#!/usr/bin/node
/* A script that prints the addition of 2 integers */

const args = process.argv;
const arg1 = parseInt(args[2]);
const arg2 = parseInt(args[3]);
console.log(add(arg1, arg2));
function add(a, b) {
  return a + b;
}
