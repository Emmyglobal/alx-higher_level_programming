#!/usr/bin/node
/* A class Rectangle that defines a rectangle. */
module.exports = class Rectangle {
  /* constructor takes in 2 arguments w and h */
  constructor (w, h) {
    /* checks if width and height values are greater than equal to 0 */
    if (w > 0 && h > 0) {
    /* assigns the given value to its respective variable */
      [this.width, this.height] = [w, h];
    }
  }

  print () {
    /* loop thru the height of the rectangle */
    for (let i = 0; i < this.height; i++) {
      /* print out 'X' repeating it the number of it's width times */
      console.log('X'.repeat(this.width));
    }
  }
};
