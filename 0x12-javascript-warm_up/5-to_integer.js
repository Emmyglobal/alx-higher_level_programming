#!/usr/bin/node
if (process.argv[2] || process.argv[3]) {
	console.log('My number: ' + process.argv.length);
} else {
	console.log('Not a number');
}
