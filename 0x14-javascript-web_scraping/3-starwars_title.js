#!/usr/bin/node
const request = require('request');
const myArgv = process.argv;
let url = 'https://swapi.co/api/films/';
if (myArgv[2] !== undefined) {
  url += myArgv[2];
  request(url, function (error, response, body) {
    if (error) {
      console.error('error:', error);
    } else {
      console.log(JSON.parse(body).title);
    }
  });
}
