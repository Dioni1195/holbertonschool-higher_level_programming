#!/usr/bin/node
exports.esrever = function (list) {
  const tsil = [];
  let item;
  for (item = list.length - 1; item >= 0; item--) {
    tsil.push(list[item]);
  }
  return tsil;
};
