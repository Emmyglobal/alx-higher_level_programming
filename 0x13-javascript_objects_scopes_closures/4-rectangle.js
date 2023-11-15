#!/usr/bin/node
/* a class Rectangle that defines a rectangle */
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { [this.width, this.height] = [w, h]; }
  }

  print () {
    /* loop thru the height of the rectangle */
    for (let i = 0; i < this.height; i++) {
      /* print out 'X' repeating it the number of it's width times */
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    /* switch  property values to rotate */
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    /* doubling the variable values */
    [this.width, this.height] = [this.width * 2, this.height * 2];
  }
};
