#!/usr/bin/node
const request = require('request');
const myArgv = process.argv;
const fs = require('fs');
const userIds = [1, 2 , 3, 4, 5, 6, 7, 8, 9, 10]
let ret_obj = {};
for (let user of userIds) {
  request(myArgv[2],{qs: {userId: user, completed: true}},function (error, response, body) {
    if (error) {
      console.error('error:', error);
    } else {
      ret_obj[user] = JSON.parse(body).length;
    }
  });
}

setTimeout(function(){
  console.log(ret_obj);
},2000)
