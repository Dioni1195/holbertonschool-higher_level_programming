#!/usr/bin/node
const myArgv = process.argv;
if (myArgv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(myArgv[2]);
}
