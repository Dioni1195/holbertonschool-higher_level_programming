#!/usr/bin/node
const request = require('request');
const myArgv = process.argv;
const fs = require('fs');

request(myArgv[2], function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    const bodyResponse = body;
    fs.writeFile(myArgv[3], bodyResponse, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
