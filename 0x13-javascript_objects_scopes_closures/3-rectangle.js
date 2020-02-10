#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let num = this.height;
    while (num > 0) {
      console.log('X'.repeat(this.width));
      --num;
    }
  }
}

module.exports = Rectangle;
