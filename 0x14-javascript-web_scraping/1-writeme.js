#!/usr/bin/node

// import the require module to read from file
const fileSystem = require('fs');

// read input from the commandline and store in variable
const filePath = process.argv[2];
const str = process.argv[3];

fileSystem.writeFile(filePath, str, 'utf-8', error => {
  if (error) {
    console.log(error);
  }
});
