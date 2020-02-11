#!/usr/bin/node
const fs = require('fs');
const myArgv = process.argv;
if (myArgv[2] !== undefined && myArgv[3] !== undefined) {
  fs.writeFile(myArgv[2], myArgv[3], 'utf8', (err) => {
    if (err) {
      console.log(err);
    }
  });
}
