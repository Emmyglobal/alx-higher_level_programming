#!/usr/bin/node
/*imports a dictionary of occurrences by user id and computes a dictionary*/

const dict = require('./101-data.js').dict;
const newDict = {};

for (const userId in dict) {
	const occurrence = dict[userId];
	if (!newDict[occurrence]){
		newDict[occurrence] = [];
	}
	newDict[occurrence].push(userId);
}

console.log(newDict);
