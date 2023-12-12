#!/usr/bin/node
/**
 * A class representing a square, inheriting from the rectangle class.
 */
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
