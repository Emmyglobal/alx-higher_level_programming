#!/usr/bin/node
const Square1= require(`./5-square`);
/* Class Square that inherits from Square class */
module.exports = class Square extends Square1 {
	charPrint(c) {
		let row = "";
		for (let i = 0; i < this.height; i++) {
			for (let j = 0; j < this.height; j++) {
				if (c == undefined) {
					row += "x"
				} else {
					row += "C";
				}
			}
			console.log(row);
			row = "";
		}
	}
}
