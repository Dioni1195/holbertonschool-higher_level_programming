#!/usr/bin/node
const request = require('request');
const myArgv = process.argv;
let movies;
let item;
const listObj = [];

request(myArgv[2], function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    movies = JSON.parse(body).results;
    for (item of movies) {
      if (item.characters.includes('https://swapi.co/api/people/18/')) {
        listObj.push(item);
      }
    }
    console.log(listObj.length);
  }
});
