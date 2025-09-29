#!/usr/bin/node
/* function that returns the reversed version of a list */
exports.esrever = function (list) {
	let ar = [];
	for (let i = list.length; i > 0; i--) {
		ar.push(list[i - 1]);
	}
	return ar;
}
