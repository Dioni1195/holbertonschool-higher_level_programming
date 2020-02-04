#!/usr/bin/node
const myArgv = process.argv;
let newArray;
if (myArgv[2] === undefined) {
  console.log(0);
} else if (myArgv[2] !== undefined && myArgv[3] === undefined) {
  console.log(0);
} else {
  newArray = myArgv.slice(2).sort().reverse();
  console.log(newArray[1]);
}
