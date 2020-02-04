#!/usr/bin/node
const myArgv = process.argv;
let newArray;
let maxNum;
const defArray = [];

if (myArgv[2] === undefined) {
  console.log(0);
} else if (myArgv[2] !== undefined && myArgv[3] === undefined) {
  console.log(0);
} else {
  newArray = myArgv.slice(2);
  maxNum = Math.max(...newArray);
  for (const i of newArray) {
    if (maxNum !== parseInt(i)) {
      defArray.push(parseInt(i));
    }
  }
  console.log(Math.max(...defArray));
}
