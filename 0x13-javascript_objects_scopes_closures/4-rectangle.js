#!/usr/bin/node
/* Class rectangle that defines a rectangle */
module.exports = class Rectangle {
	constructor (w, h) {
		if (w > 0 && h > 0) {
			this.width = w;
			this.height = h;
		} else {
			return (`Rectangle ${{}}`);
		}
	}
		/* prints the rectangle using character X */
		print() {
			let row = "";
			for (let i = 0; i < this.height; i++) {
				for (let j = 0; j < this.width; j++) {
					row += "X";
				}
				console.log(row);
				row = "";
			}
		}

		/* exchanges the width and the height */
		rotate() {
			let temp = this.width;
			this.width = this.height;
			this.height = temp;
		}

		/* multiplies the width and the height by 2 */
		double() {
			this.width *= 2;
			this.height *= 2;
		}
};
