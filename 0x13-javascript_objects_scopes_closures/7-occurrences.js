#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  if (searchElement !== undefined) {
    let item;
    let count = 0;
    for (item of list) {
      if (item === searchElement) {
        count += 1;
      }
    }
    return count;
  }
};
