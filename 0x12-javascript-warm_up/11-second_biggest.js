#!/usr/bin/node
/* searches the second biggest integer in the list of arguments */

const args = process.argv.slice(2).map(Number);
const sorted = args.sort((a, b) => a - b);
if (args == false || args.length == 1) {
	console.log(0);
} else {
	console.log(sorted[args.length - 2]);
}
