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
};
