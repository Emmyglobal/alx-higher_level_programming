#!/usr/bin/node
/* class Square which inherits from Rectangle class */
module.exports = class Square extends require('./4-rectangle.js') {
  constructor (size) {
    super(size, size);
  }
};
