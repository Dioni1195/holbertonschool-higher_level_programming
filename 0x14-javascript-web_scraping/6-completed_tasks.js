#!/usr/bin/node
const request = require('request');
const myArgv = process.argv;
const myObj = {
  1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0
};

request(myArgv[2], { qs: { completed: true } }, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    for (const item of JSON.parse(body)) {
      myObj[item.userId] += 1;
    }
    console.log(myObj);
  }
});
