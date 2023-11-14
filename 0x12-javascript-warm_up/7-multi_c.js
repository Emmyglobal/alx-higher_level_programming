#!/usr/bin/node
/* prints x times “C is fun” */

const args = process.argv;
const x = parseInt(args[2]);
if (!x) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
