#!/usr/bin/node
const fs = require('fs');
const myArgv = process.argv;
if (myArgv[2] !== undefined) {
  fs.readFile(myArgv[2], 'utf8', (err, data) => {
    if (err) {
      console.log(err);
    } else {
      console.log(data);
    }
  });
}
