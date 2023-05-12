#!/usr/bin/node

const Squaree = require('./5-square');

class Square extends Squaree {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let str = '';
      for (let j = 0; j < this.width; j++) {
        str = str + c;
      }
      console.log(str);
    }
  }
}

module.exports = Square;
