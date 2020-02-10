#!/usr/bin/node
const myArgv = process.argv;
const num = parseInt(myArgv[2]);
function factorial (a) {
  if (a === 0 || a === 1) {
    return 1;
  }
  return factorial(a - 1) * a;
}
if (isNaN(num)) {
  console.log(1);
} else {
  console.log(factorial(num));
}
