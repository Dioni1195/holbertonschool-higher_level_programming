#!/usr/bin/node
const request = require('request');
const myArgv = process.argv;
let movies;
let item;
let count = 0;
request(myArgv[2], function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    movies = JSON.parse(body).results;
    for (item of movies) {
      if (item.characters.includes('https://swapi.co/api/people/18/')) {
        ++count;
      }
    }
    console.log(count);
  }
});
