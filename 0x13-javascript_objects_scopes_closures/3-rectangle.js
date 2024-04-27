#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0) {
      if (typeof h === 'number' && h > 0) {
        this.width = w;
        this.height = h;
      }
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
