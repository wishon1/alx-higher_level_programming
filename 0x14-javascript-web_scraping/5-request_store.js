#!/usr/bin/node

// Import the request module
const request = require('request');

// Import the file system module
const fs = require('fs');

// Extract the URL to request from the command line arguments
const urlToRequest = process.argv[2];

// Extract the file path to store the body response from the command line arguments
const filePath = process.argv[3];

// Make an HTTP GET request to the specified URL
request(urlToRequest, (error, response, body) => {
  // If there's an error during the request, log it
  if (error) {
    console.error(error);
  } else {
    // Write the response body to the file
    fs.writeFile(filePath, body, 'utf-8', (error) => {
      // If there's an error during writing to the file, log it
      if (error) {
        console.error(error);
      }
    });
  }
});
