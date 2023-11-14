#!/usr/bin/node
/*  prints My number: <first argument converted in integer> */

const args = process.argv;
const x = parseInt(args[2]);
if (x) {
  console.log('My number: ' + args[2]);
    }
else {
  console.log('Not a number');
}
