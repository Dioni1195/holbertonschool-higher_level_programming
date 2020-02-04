#!/usr/bin/node
const myArgv = process.argv;
let num = myArgv[2];
if (myArgv.length === 2) {
  console.log('Missing size');
}
while (num > 0) {
  console.log('X'.repeat(myArgv[2]));
  --num;
}
