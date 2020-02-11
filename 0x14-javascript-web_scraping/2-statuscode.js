#!/usr/bin/node
const request = require('request');
const myArgv = process.argv;
if (myArgv[2] !== undefined) {
  request(myArgv[2], function (error, response, body) {
    if (error) {
      console.error('error:', error);
    } else {
      console.log('code:', response.statusCode);
    }
  });
}
