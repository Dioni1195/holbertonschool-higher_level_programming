#!/usr/bin/node
const squarePre = require('./5-square');

class Square extends squarePre {
  charPrint (c) {
    if (c !== undefined) {
      let num = this.height;
      while (num > 0) {
        console.log(c.repeat(this.width));
        --num;
      }
    } else {
      super.print();
    }
  }
}

module.exports = Square;
