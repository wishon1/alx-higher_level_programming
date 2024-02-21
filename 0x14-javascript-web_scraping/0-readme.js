#!/usr/bin/node

// import the file system module
const fileSys = require('fs');

// Extract the file path fromn the commmand-line arguement
const filePath = process.argv[2];

// read the content of the file using 'fs.readFile'
fileSys.readFile(filePath, 'utf-8', (error, data) => {
  // if an error occured during file reading, print the error obj
  if (error) {
    console.error('Error reading file:', error);
    return;
  }
  // if no error occur, print the content of the file
  console.log(data);
});
