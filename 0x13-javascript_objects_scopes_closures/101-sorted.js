#!/usr/bin/node
/* mports a dictionary of occurrences by user id and computes a */
/* +dictionary of user ids by occurrence. */

const data = require('./101-data');
const dict = data.dict;

const usersByOccurrence = {};

for (const id in dict) {
  const occurrences = dict[id];

  if (!usersByOccurrence[occurrences]) {
    usersByOccurrence[occurrences] = [];
  }

  usersByOccurrence[occurrences].push(id);
}

console.log(usersByOccurrence);
