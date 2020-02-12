#!/usr/bin/node
const request = require('request');
const myArgv = process.argv;
const myObj = {};

request(myArgv[2], { qs: { completed: true } }, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    for (const item of JSON.parse(body)) {
      myObj[item.userId] = 0;
    }
    for (const item of JSON.parse(body)) {
      myObj[item.userId] += 1;
    }
    console.log(myObj);
  }
});
