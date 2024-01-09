#!/usr/bin/node

let index = 2;
let iterator;
let numbersList;
let resultArray;

if (process.argv.length < 4) {
  console.log(0);
} else {
  numbersList = [];
  while (process.argv[index] !== undefined) {
    numbersList.push(parseInt(process.argv[index]));
    index++;
  }

  numbersList.sort((a, b) => b - a);

  resultArray = [numbersList[0]];
  iterator = 1;
  while (numbersList[iterator]) {
    if (numbersList[iterator - 1] !== numbersList[iterator]) {
      resultArray.push(parseInt(numbersList[iterator]));
    }
    iterator++;
  }
  console.log(resultArray[1]);
}
