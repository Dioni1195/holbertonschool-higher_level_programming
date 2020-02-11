#!/usr/bin/node
const request = require('request');
const myArgv = process.argv;

request(myArgv[2],{qs: {completed: true}},function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    for (let item of JSON.parse(body)) {
      console.log(item.)
    }
  }
});
