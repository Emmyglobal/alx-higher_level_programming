#!/usr/bin/node
/* Prints a square */

const args = process.argv;
const num = parseInt(args[2]);
if (!num) {
  console.log('Missing size');
} else {
  for (let i = 1; i <= num; i++) {
    console.log('X'.repeat(num));
  }
}
