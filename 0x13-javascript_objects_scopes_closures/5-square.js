#!/usr/bin/node
const Rectangle = require(`./4-rectangle`);
/* Class Square that inherits from Rectangle class */
module.exports = class Square extends Rectangle {
	constructor(size) {
		super(size, size);
	}
}
