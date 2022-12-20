#!/usr/bin/node

const sum = parseInt(process.argv[2]) + parseInt(process.argv[3]);

if (parseInt(process.argv[2]) && parseInt(process.argv[3])) {
  console.log(sum);
} else {
	console.log('NaN');
}
