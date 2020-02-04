#!/usr/bin/node
const myArgv = process.argv;
let num = parseInt(myArgv[2]);
if (isNaN(num)) {
  console.log('Missing size');
}
while (num > 0) {
  console.log('X'.repeat(myArgv[2]));
  --num;
}
