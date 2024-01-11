#!/usr/bin/node
/* mports an array and computes a new array. */

const array = require('./100-data');

const newArray = array.list;

const mapList = newArray.map((value, index) => value * index);

console.log(newArray);
console.log(mapList);
