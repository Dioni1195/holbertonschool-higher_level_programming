#!/usr/bin/node
const myArgv = process.argv;
const firstNum = parseInt(myArgv[2]);
if (isNaN(firstNum)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + firstNum);
}
