#!/usr/bin/node
/*  prints My number: <first argument converted in integer> */

const args = process.argv;
if (typeof args[2] === 'number') {
  parseInt(args[2], 10);
  console.log('My number: ' + args[2]);
    }
else {
  console.log('Not a number');
}
