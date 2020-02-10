#!/usr/bin/node
const lang = 'C is fun';
const myArgv = process.argv;
let num = myArgv[2];
if (myArgv.length === 2) {
  console.log('Missing number of occurrences');
}
while (num > 0) {
  console.log(lang);
  --num;
}
