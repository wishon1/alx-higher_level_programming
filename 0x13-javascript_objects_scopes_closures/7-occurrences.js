#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  let counter = 0;
  while (i < list.length) {
    if (list[i] === searchElement) {
      counter = counter + 1;
    }
    i++;
  }

  return counter;
};
