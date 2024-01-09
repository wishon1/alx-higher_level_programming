#!/usr/bin/node
/* increments and calls a function. */

function addMeMaybe (num, func) {
  num++;
  func(num);
}

module.exports.addMeMaybe = addMeMaybe;
