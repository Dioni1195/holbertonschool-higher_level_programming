#!/usr/bin/node
const myArgv = process.argv;
if (myArgv[2] === undefined) {
  console.log('No argument');
} else if (myArgv[2] !== undefined && myArgv[3] === undefined) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
