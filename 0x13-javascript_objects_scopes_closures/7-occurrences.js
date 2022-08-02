#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  let index = 0;
  for (index = 0; index < list.length; index++) {
    if (list[index] === searchElement) {
      count++;
    }
  }
  return (count);
};
